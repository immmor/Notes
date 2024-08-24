import os
import datetime
import webbrowser
from flask import Flask, render_template, request
from flasgger import Swagger, swag_from
from tools import get_json_data, write_json_data
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


if __name__ == '__main__':
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open("http://127.0.0.1:666/")
        # webbrowser.open("http://[::1]666/")
        # get_toutiao(playf=True)
    app.run(host="0.0.0.0", debug=True, port=666)
