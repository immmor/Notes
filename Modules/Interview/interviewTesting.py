from flask import Blueprint, render_template
from flasgger import swag_from
import json
from tools import chatanywhere_ai, get_json_data, write_json_data
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
    interviewTestRawData = get_json_data('Statics/Others/interviewTest.json')
    
    # write_json_data(visitRawData, jsonFileName='Statics/Others/visit.json')
    return render_template('Statics/Html/interviewTesting.html', interviewTestData=interviewTestRawData['测试面试题'])


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
    # prompt = """
    # [
    #     {
    #         "模块": "Python编程",
    #         "问题": "什么是Python中的列表推导式？",
    #         "答案": "列表推导式是一种简洁的方式来创建列表，它允许用户通过一个表达式来创建一个列表，即通过一个已有的列表快速生成另一个列表。"
    #     }
    # ]
    # 按照这个json格式给这些模块[测试基础, WEB功能测试, MySQL数据库, Python编程, 接口测试, WebUI自动化, 安卓自动化, Jmeter, 性能测试, 车载测试]各输出一个面试题并给出相应的答案(把他们都放到一个列表里，保留"模块"这个键。不要生成同样的内容，不要说别的，直接用json格式输出)。"
    # """
    prompt = """
    [
        {
            "模块": "Python编程",
            "问题": "什么是Python中的列表推导式？",
            "答案": "列表推导式是一种简洁的方式来创建列表，它允许用户通过一个表达式来创建一个列表，即通过一个已有的列表快速生成另一个列表。"
        }
    ]
    按照这个json格式给[安卓自动化]模块输出十个面试题并给出相应的答案(把他们都放到一个列表里，保留"模块"这个键。不要生成同样的内容，不要说别的，直接用json格式输出)。"
    """
    print(prompt)
    result = chatanywhere_ai(prompt)
    print(result)
    jsonResult = json.loads(result)
    print(jsonResult)
    interviewTestRawData = get_json_data('Statics/Others/interviewTest.json')
    interviewTestRawDataList = interviewTestRawData["测试面试题"]
    print(interviewTestRawDataList)
    interviewTestRawData["测试面试题"] = interviewTestRawDataList + jsonResult
    print(interviewTestRawData["测试面试题"])
    write_json_data(interviewTestRawData, 'Statics/Others/interviewTest.json')
    return interviewTestRawData


if '__name__' == '__main__':
    d1 = {'a': [{'k': 'd'}]}
    print(d1)


    interviewTestRawData11 = get_json_data('Statics/Others/interviewTest.json')
    print(interviewTestRawData11)

    interviewTestRawData11.update('d1')
    print(interviewTestRawData11)
    my_dict = {'key1': 'value1', 'key2': 'value2'}

    print(my_dict)

