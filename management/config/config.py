from config import DEFAULT_CONFIG

# Enable or disable debugging
DEBUG = False

# Secret key code
SECRET_KEY = DEFAULT_CONFIG.get('SECRET_KEY', None)

# Bootstrap
# Enable or disable local serving required bootstrap files
BOOTSTRAP_SERVE_LOCAL = DEFAULT_CONFIG.get('BOOTSTRAP_SERVE_LOCAL', False)
