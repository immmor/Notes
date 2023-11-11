from flask import Blueprint, render_template
from flasgger import swag_from
from tools import claude_ai

bp = Blueprint('test', __name__)

@bp.route('/test', methods=['GET'])
@swag_from({
    'tags': ['Test Index Page'],
    'description': 'Returns details of a user', 
    'responses': {
        '200': {
            'description': 'Success' 
        }
    }
})
def test_interview():
    return render_template('Statics/Html/testInterview.html')


@bp.route('/test/generate', methods=['GET'])
@swag_from({
    'tags': ['generate_test_interview'],
    'description': 'Returns details of a user', 
    'responses': {
        '200': {
            'description': 'Success' 
        }
    }
})
def generate_test_interview():
    prompt = "给我1个Web UI自动化测试面试题并给出相应的答案(不要说别的，直接用markdown格式输出)。"
    result = claude_ai(prompt)
    print(result)
    return result

