from flask import Blueprint, render_template
from flasgger import swag_from

bp = Blueprint('language', __name__)


@bp.route('/lang', methods=['GET'])
def language_learn():
    return render_template('Statics/Html/language.html')