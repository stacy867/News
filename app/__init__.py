from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
# Initializing application
#app = Flask(__name__,instance_relative_config = True)
# Creating the app configurations
    app.config.from_object(config_options[config_name])

# Initializing Flask Extensions
    bootstrap.init_app(app)

# Registering a blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint) 

# Setting up configuration
    from .request import configure_request
    configure_request(app)

    return app

# from app import views