from flask import Flask
from distribution_app.config import config_dict
from distribution_app.utils.db import db
from flask_restful import Api
from distribution_app.rest.rest import ManufacturerList,DistributorList,OutletList,\
    ManufacturerSingle,DistributorSingle,OutletSingle
from flask_migrate import Migrate

def create_app(config=config_dict['dev']):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)

    api = Api(app)
    with app.app_context():
        db.init_app(app)
        db.create_all()
    migrate = Migrate(app, db)
    #migrate.init_app(app, db)

    from .models import model
    from .views import view
    app.register_blueprint(view.bp)


    api.add_resource(ManufacturerList, '/api/')
    api.add_resource(ManufacturerSingle, '/api/<int:id>')
    api.add_resource(DistributorList, '/api/distributors')
    api.add_resource(DistributorSingle, '/api/distributors/<int:id>')
    api.add_resource(OutletList, '/api/outlet')
    api.add_resource(OutletSingle, '/api/outlet/<int:id>')



    return app
