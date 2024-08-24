import datetime
from tools import get_json_data, write_json_data
from flask import Blueprint, render_template, request
from flasgger import swag_from

bp = Blueprint('graduate methods', __name__)


@bp.route('/changeFalseNumber', methods=['POST', 'GET'])
def false_number():
    probRawData = get_json_data('Statics/Others/gradProb.json')
    questionNumber = request.form['questionNumber']
    falseNumber = request.form['falseNumber']
    recentFalse = request.form['recentFalse']
    probRawData["考研题目"][int(questionNumber)]["错误次数"] = int(falseNumber)
    probRawData["考研题目"][int(questionNumber)]['最近错过'] = int(recentFalse)
    write_json_data(probRawData, jsonFileName='Statics/Others/gradProb.json')
    return questionNumber


@bp.route('/showTimes', methods=['POST', 'GET'])
def show_times():
    probRawData = get_json_data('Statics/Others/gradProb.json')
    questionNumber = request.form['questionNumber']
    probRawData["考研题目"][int(questionNumber)]['题目出现次数'] += 1
    write_json_data(probRawData, jsonFileName='Statics/Others/gradProb.json')
    return questionNumber


@bp.route('/checkResult', methods=['POST', 'GET'])
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
