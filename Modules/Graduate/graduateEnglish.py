import json, os, sys, copy, datetime, requests, webbrowser
from tools import claude_ai, get_json_data, write_json_data, trans_youdao, get_csv, chatanywhere_ai, word_count
from initiation import limiter
from flask import Blueprint, render_template, request, jsonify
from flasgger import swag_from

bp = Blueprint('graduate english', __name__)

# 全局变量来存储索引映射和排序后的文章列表
index_mapping = {}
sorted_essays = []

@bp.route('/grad/eng', methods=['GET'])
@limiter.limit("5 per minute")
def eng():
    global g
    g = essayGenerator()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    visitRawData = get_json_data('Statics/Others/visit.json')
    visitRawData['英语'][1]['访问时间'].append(now)
    visitRawData['英语'][0] = len(visitRawData['英语'][1]['访问时间'])
    write_json_data(visitRawData, jsonFileName='Statics/Others/visit.json')
    return render_template('Statics/Html/graduateEnglish.html')


def essayGenerator():
    global essay, index_mapping, sorted_essays
    essayEnglish = get_json_data('Statics/Others/essayEnglish.json')
    essay = essayEnglish['essay']
    # 根据 clicked 值排序
    sorted_essays = sorted(enumerate(essay), key=lambda x: x[1].get('clicked', 0), reverse=True)
    # 创建索引映射
    index_mapping = {new_index: original_index for new_index, (original_index, _) in enumerate(sorted_essays)}
    
    a = 0
    while a < len(sorted_essays):
        yield [item[1] for item in sorted_essays[a:a+3]]
        a += 3


@bp.route('/eng/essay', methods=['GET', 'POST'])
def essay():
    global g
    reset = request.form['reset']
    print(reset)
    if reset == 'yes':
        g = essayGenerator()
    try:
        k = next(g)
        return jsonify(k)
    except StopIteration:
        return '已没有内容'


@bp.route('/eng/clicked', methods=['POST'])
def click_count():
    sorted_index = int(request.form['essayIndex'])
    original_index = index_mapping.get(sorted_index)
    
    if original_index is not None:
        essay_data = get_json_data('Statics/Others/essayEnglish.json')
        if 0 <= original_index < len(essay_data['essay']):
            essay_data['essay'][original_index]['clicked'] += 1
            write_json_data(essay_data, 'Statics/Others/essayEnglish.json')
            return 'Success'
    
    return 'Invalid essay index', 400


@bp.route('/eng/aiGenerateEssay', methods=['GET', 'POST'])
@swag_from({
    'tags': ['AI Generate Essay'],
    'summary': 'AI Generate Essay',
    'description': 'AI Generate Essay', 
    # 'parameters': [
    #     {
    #         'name': 'user_id',
    #         'in': 'query',
    #         'type': 'integer'
    #     }
    # ],
    'responses': {
        '200': {
            'description': 'Success' 
        }
    }
})
def ai_generate_essay():
    generateEssayPrompt = """
        完全换一个title和content，并且计算每一个paragraph的字数输出为wordCount的值，按照这个json格式再生成一篇新的不少于300字的三段作文(title不能是换一种说法，需要完全换一个主题。不要说除了json格式以外的内容):
        {
            "whoCreated": "claudeAI",
            "title": "Balancing Study and Extracurricular Activities",
            "content": [
                {
                    "paragraph": "For university students, balancing academics and extracurricular activities can be challenging. While focusing on studies is important, participating in hobbies and social activities also provides benefits.",
                    "wordCount": 86
                },
                {
                    "paragraph": "Extracurriculars allow students to take a break from intense study routines. Joining sports teams, clubs and community service promotes physical health, social connections and teamwork skills. Leadership roles in organizations also build self-confidence. However, taking on too many extracurriculars can distract from academics.",
                    "wordCount": 117
                },
                {
                    "paragraph": "Therefore, students should carefully choose 1-2 extracurriculars aligned with personal interests and schedule them responsibly around study time. Focus should remain on maintaining strong grades, while allotting some time for hobbies and relationships. With proper balance, the university experience will be fulfilling both inside and outside the classroom.",
                    "wordCount": 117
                }
            ],
            "totalWordCount": 259,
            "clicked": 0
        }
    """
    print(generateEssayPrompt)
    result = chatanywhere_ai(generateEssayPrompt)
    jsonResult = json.loads(result)
    print(jsonResult)
    jsonResult['totalWordCount'] = 0
    for i in jsonResult['content']:
        num = int(word_count(i["paragraph"]))
        i["wordCount"] = num
        print('total: ' + str(jsonResult['totalWordCount']))
        jsonResult['totalWordCount'] += num
    content = get_json_data('Statics/Others/essayEnglish.json')
    content['essay'].append(jsonResult)
    write_json_data(content, 'Statics/Others/essayEnglish.json')
    print(jsonResult)
    return result


@bp.route('/eng/rewrite', methods=['POST', 'GET'])
def rewrite():
    rewriteContent = request.form['rewriteContent']
    content = chatanywhere_ai('用英语高级词汇换一种说法重写一遍（不要换行，不要空格，不要说别的）: ' + rewriteContent)
    print(content)
    return content


@bp.route('/eng/trans', methods=['POST', 'GET'])  # AI translate
def trans():
    transContent = request.form['transContent']
    print(transContent)
    try:
        content = chatanywhere_ai('直接把这个翻译成中文（不要换行，不要空格，不要说别的）: ' + transContent)
        return content
    except:
        transContentList = transContent.split('.')
        content = ''
        for i in transContentList:
            con = trans_youdao(i)
            if con.endswith('。'):
                content += con
            else:
                content += con + '。'
        return content
    

@bp.route('/eng/transWord', methods=['POST', 'GET'])  # AI translate
def trans_word():
    from sqlalchemy import create_engine, Column, String, Integer
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.declarative import declarative_base

    # 创建数据库引擎
    engine = create_engine('sqlite:///Database/dictionary.db')

    # 创建会话
    Session = sessionmaker(bind=engine)
    session = Session()

    # 创建基类
    Base = declarative_base()

    # 定义词典模型
    class Dictionary(Base):
        __tablename__ = 'dictionary'

        id = Column(Integer, primary_key=True)
        original_word = Column(String)
        translation = Column(String)

        def __repr__(self):
            return f"<Dictionary(original_word='{self.original_word}', translation='{self.translation}')>"

    # 创建数据库表
    Base.metadata.create_all(engine)

    # 添加词汇
    selectedText = request.form['selectedText']
    print(selectedText)
    result = trans_youdao(selectedText)
    session.add(Dictionary(original_word=selectedText, translation=result))
    session.commit()

    # 查询词汇
    # words = session.query(Dictionary).all()
    # for word in words:
    #     print(word)
    
    return result


@bp.route('/eng/recommand', methods=['POST', 'GET'])  # AI translate
def essay_recommand():
    None


if __name__ == '__main__':
    essayEnglish = get_json_data('Statics/Others/essayEnglish.json')
    print(essayEnglish)
