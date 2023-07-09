import json, os, sys, copy, datetime, csv, requests
import time
from flask import Flask, render_template, request, jsonify

# os.chdir(sys.path[0])  # 把现在的工作路径切换到当前文件夹
app = Flask(__name__, template_folder='./', static_folder='')


# 获取json里面数据
def get_json_data(jsonFileName=''):
    with open(jsonFileName, 'rb') as f:  # 使用只读模型，并定义名称为f
        params = json.load(f)  # 加载json文件
        # params["code"] = "404"  # code字段对应的值修改为404
        # print(params)  # 打印
    return params  # 返回修改后的内容


def write_json_data(params, jsonFileName=''):
    # 使用写模式，名称定义为r
    # 其中路径如果和读json方法中的名称不一致，会重新创建一个名称为该方法中写的文件名
    with open(jsonFileName, 'w') as f:
        # 将dict写入名称为r的文件中
        json.dump(params, f, ensure_ascii=False)


def get_csv():
    with open('try.csv',encoding='utf-8')as fp:
        reader = csv.reader(fp)
        # 获取标题
        header = next(reader)
        print(header)
        # 遍历数据
        for i in reader:
            print(i)


@app.route('/ai', methods=['GET'])
def ai():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(now)
    visitRawData = get_json_data('visit.json')
    # print(visitRawData)
    visitRawData['人工智能'][1]['访问时间'].append(now)
    visitRawData['人工智能'][0] = len(visitRawData['人工智能'][1]['访问时间'])
    write_json_data(visitRawData, jsonFileName='visit.json')
    # print(visitRawData)
	# 传递的是读取的文件的字符串
    return render_template('graduateAI.html')


@app.route('/math', methods=['GET'])
def math():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    visitRawData = get_json_data('visit.json')
    # print(visitRawData)
    visitRawData['数学'][1]['访问时间'].append(now)
    visitRawData['数学'][0] = len(visitRawData['数学'][1]['访问时间'])
    write_json_data(visitRawData, jsonFileName='visit.json')
    # print(visitRawData)
    return render_template('graduateMath.html')


@app.route('/poli', methods=['GET'])
def poli():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    visitRawData = get_json_data('visit.json')
    # print(visitRawData)
    visitRawData['政治'][1]['访问时间'].append(now)
    visitRawData['政治'][0] = len(visitRawData['政治'][1]['访问时间'])
    write_json_data(visitRawData, jsonFileName='visit.json')
    # print(visitRawData)
    return render_template('graduatePolitics.html')


@app.route('/eng', methods=['GET'])
def eng():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    visitRawData = get_json_data('visit.json')
    # visitRawData = copy.deepcopy(get_json_data('visit.json'))
    # print(visitRawData)
    visitRawData['英语'][1]['访问时间'].append(now)
    visitRawData['英语'][0] = len(visitRawData['英语'][1]['访问时间'])
    write_json_data(visitRawData, jsonFileName='visit.json')
    # print(visitRawData)
    return render_template('graduateEnglish.html')


# probRawData = copy.deepcopy(get_json_data())
# for i in range(len(probRawData)):
#     k = {'题目出现次数': 0}
#     probRawData[i].append(5)
# print(probRawData)
# write_json_data(probRawData)
# print(get_json_data())


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
    userRawData = get_json_data('userinfo.json')
    print("登录" + subjectName, username, password)
    for i in userRawData['家庭信息']:
        if (username == i['登录名'] and password == i['密码']):
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            result = 'success'
            print(result)
            i["登陆时间"].append(now + ' ' + subjectName)
            write_json_data(userRawData, jsonFileName='userinfo.json')
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
    userRawData = get_json_data('userinfo.json')
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
                    write_json_data(userRawData, jsonFileName='userinfo.json')
                    result = 'success'
    return result


@app.route('/checkResult', methods=['POST', 'GET'])
def check_result():
    username = request.form['username']
    password = request.form['password']
    userRawData = get_json_data('userinfo.json')
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
    chatRawData = get_json_data('chat.json')
    chatRawData['聊天内容'].append(inputContent)
    write_json_data(chatRawData, jsonFileName='chat.json')
    return inputContent


@app.route('/chatContent', methods=['POST', 'GET'])
def chatContent():
    return render_template('chat.html')


def write_file(content):
    with open('claudeAI.txt', 'a+') as f:
        f.write(content + '\n')
        

def claudeAI(text):
    slackToken = 'xoxp-415445285921-416003551682-5356031879952-e553f10d7af397d89db28fe1865ee985'
    def send_msg():
        sendURL = "https://slack.com/api/chat.postMessage"
        data = {
            "token": slackToken,
            "channel": "@Claude",
            "text": text
        }
        response = requests.post(sendURL, data=data)
        print(text)
        time.sleep(2)
        return response.text

    msgSent = json.loads(send_msg())

    def receive_msg():
        receiveURL = "https://slack.com/api/conversations.history"
        data = {
            "token": slackToken,
            "channel": "D052WQCP84D",
            "oldest": msgSent['ts']
        }
        response = requests.post(receiveURL, data=data)
        result = json.loads(response.text)
        try:
            if 'Typing' in result['messages'][1]['text']:
                time.sleep(2)
                return receive_msg()
            elif 'Typing' not in result['messages'][1]['text']:
                resultMessage = result['messages'][1]['text']
                return resultMessage
        except:
            if 'Typing' in result['messages'][0]['text']:
                time.sleep(2)
                return receive_msg()
            elif 'Typing' not in result['messages'][0]['text']:
                resultMessage = result['messages'][0]['text']
                return resultMessage
            
    return receive_msg()


@app.route('/rewrite', methods=['POST', 'GET'])
def rewrite():
    rewriteContent = request.form['rewriteContent']
    content = claudeAI('用高级词汇换一种说法重写一遍（不要换行，不要空格，不要说别的）: ' + rewriteContent)
    print(content)
    return content


@app.route('/trans', methods=['POST', 'GET'])
def trans():
    transContent = request.form['transContent']
    try:
        content = claudeAI('直接把这个翻译成中文（不要换行，不要空格，不要说别的）: ' + transContent)
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


def trans_youdao(transContent):
    import requests
    data = {
        'doctype': 'json', 
        'type': 'auto',
        'i': transContent
    }
    r = requests.get("http://fanyi.youdao.com/translate",params=data)
    result = r.json()['translateResult'][0][0]['tgt']
    print(result)
    return result


def trans_micro(transContent):
    from translate import Translator
    # translator=Translator(from_lang="chinese",to_lang="english")
    # translation = translator.translate("你吃了吗？")
    # print(translation)
    translator2=Translator(from_lang="english",to_lang="chinese")
    translation = translator2.translate(transContent)
    print(translation)

    
def trans_google():
    from googletrans import Translator
    translator = Translator(service_urls=['translate.google.com'])
    title_alternative = translator.translate('你吃了吗？', dest='en').text
    print(title_alternative)
    

def text2speech(text, play, folderName):
    from playsound import playsound  
    r = requests.get(f"https://fanyi.sogou.com/reventondc/synthesis?text={text}&speed=1&lang=zh-CHS&from=translateweb&speaker=6")
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nowDay = datetime.datetime.now().strftime("%Y-%m-%d")
    # print(nowDay)
    if not os.path.exists('MP3Files/'+ nowDay + '/' + folderName):
        os.makedirs('MP3Files/' + nowDay + '/' + folderName)
    mp3FileName = 'MP3Files/' + nowDay + '/' + folderName + '/' + now + text[:2] + '.mp3'
    with open (mp3FileName, 'wb+') as f:
        f.write(r.content)
    if play:
        playsound(mp3FileName)
    
        
def get_toutiao(play=False):
    import requests, datetime, concurrent
    from playsound import playsound 
    url = 'http://v.juhe.cn/toutiao/index'
    # categoryList = ['top', 'shehui', 'guonei', 'guoji', 'yule', 'tiyu', 'junshi', 'keji', 'caijing', 'shishang']
    categoryList = ['top', 'guoji', 'junshi', 'keji']
    # myInterestsCategoryList = ['top', 'guoji', 'junshi', 'keji']
    # categoryGen = (i for i in categoryList)
    # category = next(categoryGen)
    dataInFile = get_json_data('news.json')
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
        # 报这个错的话：”TypeError: 'NoneType' object is not subscriptable“，应该是当天的额度用完了。
        print(i['title'])
        titleList.append(i['title'])
    if play:
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            # 将任务添加到线程池中
            for i in titleList:
                executor.submit(text2speech, i, play=False, folderName=newsType)
    dataInFile['result']['data'] += responseJson['result']['data']
    write_json_data(dataInFile, jsonFileName='news.json')
    if play:
        nowDay = datetime.datetime.now().strftime("%Y-%m-%d")
        if os.path.exists('MP3Files/' + nowDay + '/' + newsType):
            mp3List = os.listdir('MP3Files/' + nowDay + '/' + newsType)
            print(mp3List)
            print("本文件夹共有" + str(len(mp3List)) + "个文件")
            [playsound('MP3Files/' + nowDay + '/' + newsType + '/' + i) for i in mp3List if i.endswith('.mp3')]


def aiRobot(ask):
    url = 'https://api.dify.ai/v1/completion-messages'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer app-JPWdrBbT7GNtJM6VRc2wbNcZ',
    }
    payload = json.dumps({
        "inputs": {},
        "query": ask,
        "response_mode": "blocking",
        "user": "kkbb2"
    })
    response = requests.request("POST", url, headers=headers, data=payload)
    finalData = json.loads(response.text)
    print(finalData)

# aiRobot("把这个翻译成中文：University Students’ Different Online Shopping Interests")
# trans_youdao("As we can see in the chart, there are some differences between male and female university students in terms of online shopping, Compared with the male students’ almost even interest in clothing, books, electronic products and game currency, female students prefer clothing and books to e-products and computer games.")
# trans_micro("Such statistics can be naturally assciated with college students' varied lifestyle. First, youngsters nowadays are categorized by great academic pressures, which causes them to spend large proportion of time doing homeword. In addition, everyone, including college students, needs entertainment. Finally, doing part-time job, participating club activities and doing physical exercise can help students ease financial pressures, improve their social skills and maintain their physical health.")
# trans_google()    
    
if __name__ == '__main__':
    # get_toutiao(play=False)
    app.run(debug=True, port=5000)
