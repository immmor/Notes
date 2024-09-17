import datetime
from tools import claude_ai, get_json_data, write_json_data
from flask import Blueprint, render_template, request, jsonify, current_app
from flasgger import swag_from
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
# from notes import limiter

bp = Blueprint('graduate ai', __name__)
# 当前文件的flask_limiter没有起作用
limiter = Limiter(
    key_func=get_remote_address,
    # app=bp,
    app=current_app,
    # default_limits=["200 per day", "50 per hour"]
)
# with current_app.app_context():
#     limiter = current_app.extensions.get('flask_limiter')
# limiter = current_app.extensions.get['limiter']


@bp.route('/grad/ai', methods=['GET'])
@limiter.limit("1/minute")   # TODO
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