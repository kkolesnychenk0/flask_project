from flask import Flask
from flask_migrate import Migrate
from distribution_app.config import config_dict
from distribution_app.utils.db import db
from flask_restful import Api
from distribution_app.rest.rest import ManufacturerList

def create_app(config=config_dict['dev']):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)
    migrate = Migrate()
    api = Api(app)
    with app.app_context():
        db.init_app(app)
        db.create_all()
    migrate.init_app(app, db)

    from .models import model
    from .views import view
    app.register_blueprint(view.bp)


    api.add_resource(ManufacturerList, '/')


    return app
