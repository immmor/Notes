import json, os, sys, copy, datetime, requests, webbrowser
from flask import Flask, render_template, request, jsonify
from flasgger import Swagger, swag_from
from tools import claude_ai, get_json_data, write_json_data, trans_youdao, get_csv, chatanywhere_ai
from Modules.wrapBlueprints import blueList

# os.chdir(sys.path[0])  # 把现在的工作路径切换到当前文件夹
app = Flask(__name__, template_folder='./', static_folder='Statics')
for i in blueList:
    app.register_blueprint(i)
Swagger(app)


@app.route('/', methods=['GET'])
@swag_from({
    'tags': ['index'],
    'description': 'Returns details of a user', 
    'responses': {
        '200': {
            'description': 'Success' 
        }
    }
})
def hello():
    return render_template('Statics/Html/hello.html')


@app.route('/ai', methods=['GET'])
@swag_from({
    'tags': ['Notes for AI'],
    'description': 'Returns details of a user', 
    'responses': {
        '200': {
            'description': 'Success' 
        }
    }
})
def ai():
    # redirect
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


@app.route('/派森', methods=['GET'])
def python_full_stack():
    return render_template('Statics/Html/pythonFullStack.html')


@app.route('/problems', methods=['POST', 'GET'])  #TODO
def problems():
    return render_template('Statics/Html/problems.html')


@app.route('/addProblem', methods=['POST', 'GET'])  #TODO
def add_problem():
    return None


@app.route('/changeFalseNumber', methods=['POST', 'GET'])
def false_number():
    probRawData = get_json_data('Statics/Others/gradProb.json')
    questionNumber = request.form['questionNumber']
    falseNumber = request.form['falseNumber']
    recentFalse = request.form['recentFalse']
    probRawData["考研题目"][int(questionNumber)]["错误次数"] = int(falseNumber)
    probRawData["考研题目"][int(questionNumber)]['最近错过'] = int(recentFalse)
    write_json_data(probRawData, jsonFileName='Statics/Others/gradProb.json')
    # print(f'这道题答错{falseNumber}次了')
    return questionNumber


@app.route('/showTimes', methods=['POST', 'GET'])
def show_times():
    probRawData = get_json_data('Statics/Others/gradProb.json')
    questionNumber = request.form['questionNumber']
    probRawData["考研题目"][int(questionNumber)]['题目出现次数'] += 1
    write_json_data(probRawData, jsonFileName='Statics/Others/gradProb.json')
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
    userRawData = get_json_data('Statics/Others/userinfo.json')
    for i in userRawData['家庭信息']:
        if (username == i['登录名'] and password == i['密码']):
            print(i['余额'])
            if str(payPassword) == str(i['支付密码']):
                if i['余额'] < int(payPoints):
                    result = 'pass fail'
                else:
                    i['余额'] -= int(payPoints)
                    print(i['余额'])
                    write_json_data(userRawData, jsonFileName='Statics/Others/userinfo.json')
                    result = 'success'
            else:
                result = 'balance fail'
    return result


@app.route('/listen', methods=['POST', 'GET'])
def listen():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    clickedElement = request.form['clickedElement']
    title = request.form['title']
    currentUrl = request.form['currentUrl']
    data = now + ' ' + title + ' ' + currentUrl + ' ' + clickedElement
    print(data)
    ok = True
    if ok:
        import pandas as pd
        df = pd.DataFrame([data])
        df.to_csv('Statics/Others/bigData.csv', mode='a', header=False, index=False)
    return clickedElement


@app.route('/graph', methods=['POST', 'GET'])
def graph():
    import pandas as pd
    result = pd.read_csv('Statics/Others/bigData.csv')
    # result = get_csv('Statics/Others/bigData.csv')
    print(result, type(result))
    # result = '112'
    return render_template('Statics/Html/graph.html', result=result)


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


if __name__ == '__main__':
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open("http://127.0.0.1:666/")
        # get_toutiao(playf=True)
    app.run(host="0.0.0.0", debug=True, port=666)
