from flask import Blueprint, render_template
from flasgger import swag_from
from tools import chatanywhere_ai
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

bp = Blueprint('interview', __name__)

@bp.route('/interview', methods=['GET'])
@swag_from({
    'tags': ['Test Index Page'],
    'description': 'Returns details of a user', 
    'responses': {
        '200': {
            'description': 'Success' 
        }
    }
})
def interview_testing():
    return render_template('Statics/Html/interviewTesting.html')


@bp.route('/interview/generate', methods=['GET'])
@swag_from({
    'tags': ['generate_test_interview'],
    'description': 'Returns details of a user', 
    'responses': {
        '200': {
            'description': 'Success' 
        }
    }
})
def generate_interview_testing():
    prompt = "给每个类型的测试[测试基础, WEB功能测试, MySQL数据库, Python编程, 接口测试, WebUI自动化, 安卓自动化, Jmeter, 性能测试, 车载测试]一个面试题并给出相应的答案(每个类型之间用---分隔开。不要说别的，直接用markdown格式输出)。"
    print(prompt)
    result = chatanywhere_ai(prompt)
    print(result)
    return result

