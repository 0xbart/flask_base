from flask import Flask
from flask_bootstrap import Bootstrap


def create_app():
    app = Flask(__name__)

    # Load flask config file (config/config.py, which using Yaml file)
    app.config.from_pyfile("config/config.py")

    # Time to load some nice modules
    bootstrap = Bootstrap(app)

    # Import Blueprints
    from management.modules.base.view import base
    from management.modules.documentation.view import documentation

    # Register Blueprints
    app.register_blueprint(base)
    app.register_blueprint(documentation)

    return app
