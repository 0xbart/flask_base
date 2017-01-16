from flask import render_template, Blueprint

base = Blueprint('base', __name__, template_folder='templates')


@base.route('/index')
def index():
    return 'hello from base index'


@base.route('/')
def test():
    return render_template("base/index.html")
