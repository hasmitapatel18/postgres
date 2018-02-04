from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)
    from app import models

    from .querypg import querypg as querypg_blueprint
    app.register_blueprint(querypg_blueprint)

    from .searchingaa import searchingaa as searchingaa_blueprint
    app.register_blueprint(searchingaa_blueprint, url_prefix='/searchingaa')

    return app
