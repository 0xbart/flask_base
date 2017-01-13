from flask import Blueprint

documentation = Blueprint('documentation', __name__, url_prefix='/documentation', template_folder='templates')


@documentation.route('/index')
def index():
    return 'hello from index'
