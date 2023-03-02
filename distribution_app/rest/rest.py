from flask_restful import Resource, request
from .. import db
from ..models.model import Manufacturer, Distributor, Outlet


class ManufacturerList(Resource):
    def get(self):
        """shows the list of manufacturers"""
        manufacturer_list = Manufacturer.query.all()
        output = []
        for item in manufacturer_list:
            output_data = {'id': item.id, 'name_manufacturer': item.name_manufacturer,
                           'code_manufacturer': item.code_manufacturer, 'country': item.country}
            output.append(output_data)
        return {'list': output}

    def post(self):
        """creating manufacturer"""
        manufacturer = Manufacturer(name_manufacturer=request.get_json()['name_manufacturer'],
                                    code_manufacturer=request.get_json()['code_manufacturer'],
                                    country=request.get_json()['country'])
        manufacturer.create()
        #return {'id': manufacturer.id}


class ManufacturerSingle(Resource):
    def delete(self, id):
        """delete manufacturer"""
        manufacturer = Manufacturer.query.get(id)
        if manufacturer is None:
            return {'error': 'Not found'}
        manufacturer.delete()
        return {'message': 'Successful deletion'}

    def put(self, id):
        """changing the manufacturer's data"""
        manufacturer = Manufacturer.query.get(id)
        if manufacturer:
            name_manufacturer = request.get_json()['name_manufacturer']
            code_manufacturer = request.get_json()['code_manufacturer']
            country = request.get_json()['country']
            manufacturer.name_manufacturer = name_manufacturer
            manufacturer.code_manufacturer = code_manufacturer
            manufacturer.country = country
            db.session.commit()
            return {'message': 'Successfully edited'}
        else:
            return {'error': 'Not found'}


class DistributorList(Resource):
    def get(self):
        """shows the list of distributors"""
        distributor_list = Distributor.query.all()
        output = []
        for item in distributor_list:
            output_data = {'id': item.id, 'name_distributor': item.name_distributor,
                           'code_distributor': item.code_distributor, 'adress': item.adress}
            output.append(output_data)
        return {'list': output}

    def post(self):
        """creating distributor"""
        distributor = Distributor(name_distributor=request.get_json()['name_distributor'],
                                  code_distributor=request.get_json()['code_distributor'],
                                  adress=request.get_json()['adress'])
        distributor.create()
        return {'id': distributor.id}


class DistributorSingle(Resource):
    def delete(self, id):
        """delete distributor"""
        distributor = Distributor.query.get(id)
        if distributor is None:
            return {'error': 'Not found'}
        distributor.delete()
        return {'message': 'Successful deletion'}

    def put(self, id):
        """changing the distributor's data"""
        distributor = Distributor.query.get(id)
        if distributor:
            name_distributor = request.get_json()['name_distributor']
            code_distributor = request.get_json()['code_distributor']
            adress = request.get_json()['adress']
            distributor.name_distributor = name_distributor
            distributor.code_distributor = code_distributor
            distributor.adress = adress
            db.session.commit()
            return {'message': 'Successfully edited'}
        else:
            return {'error': 'Not found'}


class OutletList(Resource):
    def get(self):
        """shows the list of outlets"""
        outlet_list = Outlet.query.all()
        output = []
        for item in outlet_list:
            output_data = {'id': item.id, 'name_outlet': item.name_outlet,
                           'code_outlet': item.code_outlet, 'adress': item.adress}
            output.append(output_data)
        return {'list': output}

    def post(self):
        """creating outlet"""
        outlet = Outlet(name_outlet=request.get_json()['name_outlet'], code_outlet=request.get_json()['code_outlet'],
                        adress=request.get_json()['adress'])
        outlet.create()
        return {'id': outlet.id}


class OutletSingle(Resource):
    def delete(self, id):
        """delete outlet"""
        outlet = Outlet.query.get(id)
        if outlet is None:
            return {'error': 'Not found'}
        outlet.delete()
        return {'message': 'Successful deletion'}

    def put(self, id):
        """changing the outlet's data"""
        outlet = Outlet.query.get(id)
        if outlet:
            name_outlet = request.get_json()['name_outlet']
            code_outlet = request.get_json()['code_outlet']
            adress = request.get_json()['adress']
            outlet.name_outlet = name_outlet
            outlet.code_outlet = code_outlet
            outlet.adress = adress
            db.session.commit()
            return {'message': 'Successfully edited'}
        else:
            return {'error': 'Not found'}
