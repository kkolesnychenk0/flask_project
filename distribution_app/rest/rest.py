from flask_restful import Resource
from ..models.model import Manufacturer

class ManufacturerList(Resource):
    def get(self):
        return {'items':[item.json() for item in Manufacturer.query.all()]}

