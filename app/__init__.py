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

    from .homepage import homepage as homepage_blueprint
    app.register_blueprint(homepage_blueprint)

    from .querypg import querypg as querypg_blueprint
    app.register_blueprint(querypg_blueprint, url_prefix='/querypg')

    from .classespg import classespg as classespg_blueprint
    app.register_blueprint(classespg_blueprint, url_prefix='/classespg')

    from .familiespg import familiespg as familiespg_blueprint
    app.register_blueprint(familiespg_blueprint, url_prefix='/familiespg')

    from .namespg import namespg as namespg_blueprint
    app.register_blueprint(namespg_blueprint, url_prefix='/namespg')

    from .informationpg import informationpg as informationpg_blueprint
    app.register_blueprint(informationpg_blueprint, url_prefix='/informationpg')

    from .searchingaa import searchingaa as searchingaa_blueprint
    app.register_blueprint(searchingaa_blueprint, url_prefix='/searchingaa')

    return app
