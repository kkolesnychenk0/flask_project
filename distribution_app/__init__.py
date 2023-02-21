from flask import Flask
from flask_migrate import Migrate
from sqlalchemy import create_engine

from config import config_dict
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate=Migrate()

def create_app(config=config_dict['dev']):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)
    from .models import model
    with app.app_context():
        db.init_app(app)
        db.create_all()
    migrate.init_app(app, db)

    from .views import view
    app.register_blueprint(view.bp)
    return app
