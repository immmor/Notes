import datetime
from tools import get_json_data, write_json_data
from flask import Blueprint, render_template
from flasgger import swag_from

bp = Blueprint('graduate poli', __name__)


@bp.route('/grad/poli', methods=['GET'])
@swag_from({
    'tags': ['Notes for Politics'],
    'description': 'Returns details of a user', 
    'responses': {
        '200': {
            'description': 'Success' 
        }
    }
})
def poli():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    visitRawData = get_json_data('Statics/Others/visit.json')
    # print(visitRawData)
    visitRawData['政治'][1]['访问时间'].append(now)
    visitRawData['政治'][0] = len(visitRawData['政治'][1]['访问时间'])
    write_json_data(visitRawData, jsonFileName='Statics/Others/visit.json')
    # print(visitRawData)
    return render_template('Statics/Html/graduatePolitics.html')