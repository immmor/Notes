import json, os, sys, copy, datetime, requests, webbrowser
from tools import claude_ai, get_json_data, write_json_data, trans_youdao, get_csv, chatanywhere_ai, word_count
from flask import Blueprint, render_template, request, jsonify
from flasgger import swag_from

bp = Blueprint('graduate math', __name__)


@bp.route('/grad/math', methods=['GET'])
@swag_from({
    'tags': ['Notes for MATH'],
    'description': 'Returns details of a user', 
    'responses': {
        '200': {
            'description': 'Success' 
        }
    }
})
def math():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    visitRawData = get_json_data('Statics/Others/visit.json')
    # print(visitRawData)
    visitRawData['数学'][1]['访问时间'].append(now)
    visitRawData['数学'][0] = len(visitRawData['数学'][1]['访问时间'])
    write_json_data(visitRawData, jsonFileName='Statics/Others/visit.json')
    # print(visitRawData)
    return render_template('Statics/Html/graduateMath.html')