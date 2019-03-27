from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import config

app = Flask(__name__)

db = SQLAlchemy()


def create_app(config_name):
    if config_name not in ['default', 'testing', 'production', 'development']:
        config_name = 'default'
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    from .windows import window as window_blueprint
    app.register_blueprint(window_blueprint)

    return app