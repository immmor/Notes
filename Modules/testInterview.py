from flask import Blueprint, render_template

bp = Blueprint('test', __name__)

@bp.route('/test', methods=['GET'])
def test_interview():
    return render_template('Statics/Html/testInterview.html')