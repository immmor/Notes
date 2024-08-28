from tools import get_json_data, write_json_data
from flask import Blueprint, render_template, request

bp = Blueprint('try api', __name__)


# @bp.route('/chat', methods=['POST', 'GET'])
# def chat():
#     inputContent = request.form['inputContent']
#     chatRawData = get_json_data('Statics/Others/chat.json')
#     chatRawData['聊天内容'].append(inputContent)
#     write_json_data(chatRawData, jsonFileName='Statics/Others/chat.json')
#     return inputContent


# @bp.route('/chatContent', methods=['POST', 'GET'])
# def chatContent():
#     return render_template('chat.html')


@bp.route('/graph', methods=['POST', 'GET'])
def graph():
    import pandas as pd
    result = pd.read_csv('Statics/Others/bigData.csv')
    print(result, type(result))
    return render_template('Statics/Html/graph.html', result=result)
