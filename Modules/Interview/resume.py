from flask import Blueprint, render_template
from flasgger import swag_from

bp = Blueprint('resume', __name__)


@bp.route('/resume/cvc', methods=['GET'])
def resume_cvc():
    return render_template('Statics/Html/cvc.html')


@bp.route('/resume/cve', methods=['GET'])
def resume_cve():
    return render_template('Statics/Html/cve.html')