import os
import datetime
import webbrowser
from flask import render_template, request
from flasgger import swag_from
from initiation import app, limiter, socketio
from flask_socketio import emit
from tools import get_json_data, write_json_data
from Modules.wrapBlueprints import blueList

for i in blueList:
    app.register_blueprint(i)


@app.route('/', methods=['GET'])
@limiter.limit("20/minute;100/day")
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


@app.route('/chat')
def chat():
    return render_template('Statics/Html/chat.html')


@socketio.on('message')
def handle_message(message):
    emit('message', message, broadcast=True, include_self=False)


@app.route('/login', methods=['POST', 'GET'])
# @limiter.limit("2/minute;5/hour;10/day")
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
    socketio.run(app, debug=True, host="0.0.0.0", port=666, allow_unsafe_werkzeug=True)
