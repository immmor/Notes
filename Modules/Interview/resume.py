from flask import Blueprint, render_template
from flasgger import swag_from

bp = Blueprint('resume', __name__)


@bp.route('/resume/testercvc', methods=['GET'])
def resume_tester_cvc():
    return render_template('Statics/Html/testercvc.html')


@bp.route('/resume/testercve', methods=['GET'])
def resume_tester_cve():
    return render_template('Statics/Html/testercve.html')


@bp.route('/resume/pythoncvc', methods=['GET'])
def resume_python_cvc():
    return render_template('Statics/Html/pythoncvc.html')


@bp.route('/resume/pythoncve', methods=['GET'])
def resume_python_cve():
    return render_template('Statics/Html/pythoncve.html')