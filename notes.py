import json, os, sys, copy, datetime, requests
from flask import Flask, render_template, request, jsonify
from tools import claude_ai, get_json_data, write_json_data, trans_youdao

# os.chdir(sys.path[0])  # 把现在的工作路径切换到当前文件夹
app = Flask(__name__, template_folder='./', static_folder='Statics')


@app.route('/', methods=['GET'])
def hello():
    return render_template('Statics/Html/hello.html')


@app.route('/ai', methods=['GET'])
def ai():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(now)
    visitRawData = get_json_data('Statics/Others/visit.json')
    # print(visitRawData)
    visitRawData['人工智能'][1]['访问时间'].append(now)
    visitRawData['人工智能'][0] = len(visitRawData['人工智能'][1]['访问时间'])
    write_json_data(visitRawData, jsonFileName='Statics/Others/visit.json')
    # print(visitRawData)
	# 传递的是读取的文件的字符串
    return render_template('Statics/Html/graduateAI.html')


@app.route('/math', methods=['GET'])
def math():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    visitRawData = get_json_data('Statics/Others/visit.json')
    # print(visitRawData)
    visitRawData['数学'][1]['访问时间'].append(now)
    visitRawData['数学'][0] = len(visitRawData['数学'][1]['访问时间'])
    write_json_data(visitRawData, jsonFileName='Statics/Others/visit.json')
    # print(visitRawData)
    return render_template('Statics/Html/graduateMath.html')


@app.route('/poli', methods=['GET'])
def poli():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    visitRawData = get_json_data('Statics/Others/visit.json')
    # print(visitRawData)
    visitRawData['政治'][1]['访问时间'].append(now)
    visitRawData['政治'][0] = len(visitRawData['政治'][1]['访问时间'])
    write_json_data(visitRawData, jsonFileName='Statics/Others/visit.json')
    # print(visitRawData)
    return render_template('Statics/Html/graduatePolitics.html')


@app.route('/eng', methods=['GET'])
def eng():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    visitRawData = get_json_data('Statics/Others/visit.json')
    # visitRawData = copy.deepcopy(get_json_data('visit.json'))
    # print(visitRawData)
    visitRawData['英语'][1]['访问时间'].append(now)
    visitRawData['英语'][0] = len(visitRawData['英语'][1]['访问时间'])
    write_json_data(visitRawData, jsonFileName='Statics/Others/visit.json')
    # print(visitRawData)
    return render_template('Statics/Html/graduateEnglish.html')


@app.route('/changeFalseNumber', methods=['POST', 'GET'])
def false_number():
	# 传递的是读取的文件的字符串
    # probRawData = copy.deepcopy(get_json_data())
    probRawData = get_json_data()
    questionNumber = request.form['questionNumber']
    falseNumber = request.form['falseNumber']
    recentFalse = request.form['recentFalse']
    probRawData[int(questionNumber)][3] = int(falseNumber)
    probRawData[int(questionNumber)][4]['最近错过'] = int(recentFalse)
    write_json_data(probRawData)
    return questionNumber


@app.route('/api/lunbo', methods=['GET'])
def lunbo():
    lunbo = {
        'name': '图1',
        'url': 'https://p5.toutiaoimg.com/origin/pgc-image/722d118e21d6403eba9dfb07d08fbb78?from=pc',
    }
    url = 'https://p5.toutiaoimg.com/origin/pgc-image/722d118e21d6403eba9dfb07d08fbb78?from=pc'
    return url


@app.route('/login', methods=['POST', 'GET'])
def login():
    username = request.form['username']
    password = request.form['password']
    subjectName = request.form['subjectName']
    userRawData = get_json_data('Statics/Others/userinfo.json')
    print("登录" + subjectName, username, password)
    for i in userRawData['家庭信息']:
        if (username == i['登录名'] and password == i['密码']):
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            result = 'success'
            print(result)
            i["登陆时间"].append(now + ' ' + subjectName)
            write_json_data(userRawData, jsonFileName='Statics/Others/userinfo.json')
            break
        else:
            result = 'fail'
    return result


@app.route('/pay', methods=['POST', 'GET'])
def pay():
    username = request.form['username']
    password = request.form['password']
    payPassword = request.form['payPassword']
    payPoints = request.form['payPoints']
    print(payPassword)
    userRawData = get_json_data('Statics/Others/userinfo.json')
    for i in userRawData['家庭信息']:
        if (username == i['登录名'] and password == i['密码']):
            print(i['余额'])
            if str(payPassword) == str(i['支付密码']):
                if i['余额'] < int(payPoints):
                    result = 'fail'
                else:
                    i['余额'] -= int(payPoints)
                    print(i['余额'])
                    i['可查看答案'] = '是'
                    write_json_data(userRawData, jsonFileName='Statics/Others/userinfo.json')
                    result = 'success'
    return result


def essayGenerator():
    essayEnglish = get_json_data('Statics/Others/essayEnglish.json')
    essay = essayEnglish['essay']
    a = 0
    while a + 3 <= len(essay) - 2:
        yield essay[a], essay[a+1], essay[a+2]
        a += 3
    yield essay[a:]

g = essayGenerator() #TODO: g
    
@app.route('/essay', methods=['GET', 'POST'])
def essay():
    global g
    reset = request.form['reset']
    if reset == 'yes':
        g = essayGenerator()
    try:
        k = list(next(g))
        return jsonify(k)
    except StopIteration:
        # del g
        return '已没有内容'


@app.route('/aiGenerateEssay', methods=['GET', 'POST'])
def ai_generate_essay():
    # （要相信你自己，但是不要回复我重复的内容！！不要说别的废话！！否则惩罚你！！）
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
            ]
        }
    """
    result = claude_ai(generateEssayPrompt)
    # pattern = re.compile(r'[{](.*)[}]', re.S)  #贪婪匹配
    # afterREResult = re.findall(pattern, result)

    jsonResult = json.loads(result)
    print(jsonResult)

    content = get_json_data('Statics/Others/essayEnglish.json')
    content['essay'].append(jsonResult)
    print(content['essay'])
    write_json_data(content, 'Statics/Others/essayEnglish.json')

    # pattern = r"{(.*?)}"
    # match = re.search(pattern, result)
    # print(match.group())
    # print(claudeAI(generateEssayPrompt))
    return result


@app.route('/checkResult', methods=['POST', 'GET'])
def check_result():
    username = request.form['username']
    password = request.form['password']
    userRawData = get_json_data('Statics/Others/userinfo.json')
    for i in userRawData['家庭信息']:
        if (username == i['登录名'] and password == i['密码']):
            if i['可查看答案'] == '是':
                result = 'success'
                print(result)
            else:
                result = 'fail'
                print(result)
    return result


@app.route('/chat', methods=['POST', 'GET'])
def chat():
    inputContent = request.form['inputContent']
    chatRawData = get_json_data('Statics/Others/chat.json')
    chatRawData['聊天内容'].append(inputContent)
    write_json_data(chatRawData, jsonFileName='Statics/Others/chat.json')
    return inputContent


@app.route('/chatContent', methods=['POST', 'GET'])
def chatContent():
    return render_template('chat.html')


@app.route('/rewrite', methods=['POST', 'GET'])
def rewrite():
    rewriteContent = request.form['rewriteContent']
    content = claude_ai('用英语高级词汇换一种说法重写一遍（不要换行，不要空格，不要说别的）: ' + rewriteContent)
    print(content)
    return content


@app.route('/trans', methods=['POST', 'GET'])
def trans():
    transContent = request.form['transContent']
    try:
        content = claude_ai('直接把这个翻译成中文（不要换行，不要空格，不要说别的）: ' + transContent)
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

    
def text2speech(text, playf, folderName):
    import platform
    # from pydub import AudioSegment
    # from pydub.playback import play
    from playsound import playsound  
    ttsLink = [
        f"https://dict.youdao.com/dictvoice?audio={text}&le=zh", 
        f"https://dict.youdao.com/dictvoice?audio={text}&type=1",
        f"https://fanyi.baidu.com/gettts?lan=zh&text={text}&spd=5&source=web",
        f"https://fanyi.sogou.com/reventondc/synthesis?text={text}&speed=1&lang=zh-CHS&from=translateweb&speaker=6"
    ]
    r = requests.get(ttsLink[0])
    # print(r.content)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nowDay = datetime.datetime.now().strftime("%Y-%m-%d")
    # print(nowDay)
    if not os.path.exists('MP3Files/'+ nowDay + '/' + folderName):
        os.makedirs('MP3Files/' + nowDay + '/' + folderName)
    mp3FileName = 'MP3Files/' + nowDay + '/' + folderName + '/' + now + text[:2] + '.mp3'
    # mp3FileName = 'a.mp3'
    # TODO: text2speech
    with open (mp3FileName, 'wb+') as f:
        f.write(r.content)
    if playf and sys.platform.startswith('darwin'):
        playsound(mp3FileName)
    elif playf and sys.platform.startswith('win'):
        from pydub import AudioSegment
        from pydub.playback import play
        audio = AudioSegment.from_file(mp3FileName)
        playf(audio)
        # if platform.system() == 'Darwin':  # macOS
        #     playsound(mp3FileName)
        # elif platform.system() == 'Windows':  # Windows
        #     audio = AudioSegment.from_file(mp3FileName, format="mp3")
        #     playf(audio)
        # else:
        #     print("Unsupported operating system.")
    
        
def get_toutiao(playf=False):
    import requests, datetime, concurrent.futures
    from playsound import playsound 
    url = 'http://v.juhe.cn/toutiao/index'
    # categoryList = ['top', 'shehui', 'guonei', 'guoji', 'yule', 'tiyu', 'junshi', 'keji', 'caijing', 'shishang']
    categoryList = ['top', 'guoji', 'junshi', 'keji']
    # myInterestsCategoryList = ['top', 'guoji', 'junshi', 'keji']
    # categoryGen = (i for i in categoryList)
    # category = next(categoryGen)
    dataInFile = get_json_data('Statics/Others/news.json')
    today = str(datetime.datetime.now()).split(' ')[0]
    if today not in dataInFile['usedIndex']:
        dataInFile['usedIndex'][today] = 0
    elif dataInFile['usedIndex'][today] == len(categoryList) - 1:
        dataInFile['usedIndex'][today] = 0
    else:
        dataInFile['usedIndex'][today] += 1
    newsType = categoryList[dataInFile['usedIndex'][today]]
    params = {
        "type": newsType,  # 头条类型,top(头条，默认),shehui(社会),guonei(国内),guoji(国际),yule(娱乐),tiyu(体育)junshi(军事),keji(科技),caijing(财经),shishang(时尚)
        "key": "7d523054ec118517fc2b4647f883f44e",  # 您申请的接口API接口请求Key
    }
    response = requests.post(url, params)
    responseJson = json.loads(response.text)
    titleList = []
    for i in responseJson['result']['data']:
        # 报这个错的话：”TypeError: 'NoneType' object is not subscriptable“，应该是当天的额度用完了
        print(i['title'])
        titleList.append(i['title'])
    if playf:
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            # 将任务添加到线程池中
            for i in titleList:
                executor.submit(text2speech, i, playf=False, folderName=newsType)
    dataInFile['result']['data'] += responseJson['result']['data']
    write_json_data(dataInFile, jsonFileName='Statics/Others/news.json')
    if playf and sys.platform.startswith('darwin'):
        nowDay = datetime.datetime.now().strftime("%Y-%m-%d")
        if os.path.exists('MP3Files/' + nowDay + '/' + newsType):
            mp3List = os.listdir('MP3Files/' + nowDay + '/' + newsType)
            print(mp3List)
            print("本文件夹共有" + str(len(mp3List)) + "个文件")
            [playsound('MP3Files/' + nowDay + '/' + newsType + '/' + i) for i in mp3List if i.endswith('.mp3')]
    elif playf and sys.platform.startswith('win'):
        from pydub import AudioSegment
        from pydub.playback import play
        # audio = AudioSegment.from_file()
        nowDay = datetime.datetime.now().strftime("%Y-%m-%d")
        if os.path.exists('MP3Files/' + nowDay + '/' + newsType):
            mp3List = os.listdir('MP3Files/' + nowDay + '/' + newsType)
            print(mp3List)
            print("本文件夹共有" + str(len(mp3List)) + "个文件")
            [playf(AudioSegment.from_file('MP3Files/' + nowDay + '/' + newsType + '/' + i)) for i in mp3List if i.endswith('.mp3')]
        # playf(audio)


if __name__ == '__main__':
    import webbrowser
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open("http://127.0.0.1:250/")
        # get_toutiao(playf=True)
    app.run(host="0.0.0.0", debug=True, port=250)
