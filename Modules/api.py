import datetime
from tools import get_json_data, write_json_data
from flask import Blueprint, render_template, request
from flasgger import swag_from

bp = Blueprint('graduate api', __name__)


@bp.route('/listen', methods=['POST', 'GET'])
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


@bp.route('/pay', methods=['POST', 'GET'])
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
                    result = 'balance fail'
                else:
                    i['余额'] -= int(payPoints)
                    print(i['余额'])
                    write_json_data(userRawData, jsonFileName='Statics/Others/userinfo.json')
                    result = 'success'
            else:
                result = 'pass fail'
    return result