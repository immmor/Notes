import json, os, sys, copy, datetime, requests, webbrowser
from tools import claude_ai, get_json_data, write_json_data, trans_youdao, get_csv, chatanywhere_ai, word_count
from flask import Blueprint, render_template, request, jsonify
from flasgger import swag_from

bp = Blueprint('graduate english', __name__)


@bp.route('/eng', methods=['GET'])
def eng():
    g = essayGenerator()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    visitRawData = get_json_data('Statics/Others/visit.json')
    visitRawData['英语'][1]['访问时间'].append(now)
    visitRawData['英语'][0] = len(visitRawData['英语'][1]['访问时间'])
    write_json_data(visitRawData, jsonFileName='Statics/Others/visit.json')
    return render_template('Statics/Html/graduateEnglish.html')


def essayGenerator():
    essayEnglish = get_json_data('Statics/Others/essayEnglish.json')
    essay = essayEnglish['essay']
    a = 0
    while a + 3 <= len(essay) - 2:
        yield essay[a], essay[a+1], essay[a+2]
        a += 3
    yield essay[a:]


@bp.route('/essay', methods=['GET', 'POST'])
def essay():
    global g
    reset = request.form['reset']
    print(reset)
    if reset == 'yes':
        g = essayGenerator()
    try:
        k = list(next(g))
        return jsonify(k)
    except StopIteration:
        return '已没有内容'


@bp.route('/aiGenerateEssay', methods=['GET', 'POST'])
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
        换一个title和content，并且计算每一个paragraph的字数输出为wordCount的值，按照这个json格式再生成一篇新的不少于300字的三段作文(不要说除了json格式以外的内容):
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
            "totalWordCount": 259
        }
    """
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


@bp.route('/rewrite', methods=['POST', 'GET'])
def rewrite():
    rewriteContent = request.form['rewriteContent']
    content = chatanywhere_ai('用英语高级词汇换一种说法重写一遍（不要换行，不要空格，不要说别的）: ' + rewriteContent)
    print(content)
    return content


@bp.route('/trans', methods=['POST', 'GET'])  # AI translate
def trans():
    transContent = request.form['transContent']
    try:
        content = chatanywhere_ai('直接把这个翻译成中文（不要换行，不要空格，不要说别的）: ' + transContent)
        print(content)
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