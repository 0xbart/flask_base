from flask import Blueprint

base = Blueprint('base', __name__, template_folder='templates')


@base.route('/index')
def index():
    from management import create_app
    app = create_app()
    print(app.config['BOOTSTRAP_SERVE_LOCAL'])
    return 'hello from base index'