from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

# initialize bootstrap
bootstrap = Bootstrap()

def create_app(config_name):
    """
    Function that will initialize the Flask instance (app)
    """
    #create the app instance
    app = Flask(__name__)

    #set app configurations
    app.config.from_object(config_options[config_name])

    #initialize bootstrap
    bootstrap.init_app(app)

    #register blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #init requests configurations
    from .request import configure_request
    configure_request(app)

    return app