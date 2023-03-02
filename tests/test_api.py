from flask import current_app
from distribution_app import create_app, config_dict, db
import unittest
from distribution_app.models.model import Manufacturer, Distributor, Outlet


class TestWebService(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config=config_dict['test'])
        self.appctx = self.app.app_context()
        self.appctx.push()
        self.client = self.app.test_client()
        db.create_all()
        self.populate_db()

    def tearDown(self):
        db.drop_all()
        self.appctx.pop()
        self.app = None
        self.appctx = None

    def populate_db(self):
        """add data for test database"""
        manufacturer_test=Manufacturer(name_manufacturer='Mfortest',code_manufacturer='123q', country='testcountry')
        distributor_test=Distributor(name_distributor='Dfortest',code_distributor='123w', adress='testadress')
        outlet_test=Outlet(name_outlet='Ofortest',code_outlet='123e',adress='testadress')
        db.session.add(manufacturer_test)
        db.session.add(distributor_test)
        db.session.add(outlet_test)
        db.session.commit()
    def test_app(self):
        assert self.app is not None
        assert current_app == self.app

    def test_api_manufacturers_list(self):
        """testing GET request for class ManufacturerList"""
        response = self.client.get('/api/')
        assert response.status_code == 200

    def test_api_add_manufacturer(self):
        """testing POST request for class ManufacturerList"""
        response=self.client.post('/api/',json=
        {'name_manufacturer':'testName','code_manufacturer':'testCode','country':'country'})
        assert response.status_code == 200
        #check the data in the database
        item = Manufacturer.query.filter_by(name_manufacturer='testName').first()
        assert item is not None
        assert item.code_manufacturer == 'testCode'

    def test_api_change_manufacturer(self):
        """testing PUT request for class ManufacturerSingle"""
        item=Manufacturer.query.filter_by(name_manufacturer='Mfortest').first()
        item.code_manufacturer='changeCode'
        response=self.client.put('/api/1',json={'name_manufacturer':item.name_manufacturer,
                                                'code_manufacturer':item.code_manufacturer,'country':item.country})
        assert response.status_code==200
        # check the data in the database
        elem=Manufacturer.query.filter_by(name_manufacturer='Mfortest').first()
        assert elem.code_manufacturer=='changeCode'

    def test_api_delete_manufacturer(self):
        """testing DELETE request for class ManufacturerSingle"""
        item = Manufacturer.query.filter_by(name_manufacturer='Mfortest').first()
        assert item is not None
        response=self.client.delete(f'/api/{item.id}')
        assert response.status_code == 200
    def test_api_distributors_list(self):
        """testing GET request for class DistributorList"""
        response = self.client.get('/api/distributors')
        assert response.status_code == 200

    def test_api_add_distributor(self):
        """testing POST request for class DistributorList"""
        response=self.client.post('/api/distributors',json=
        {'name_distributor':'testName','code_distributor':'testCode','adress':'adress'})
        assert response.status_code == 200
        #check the data in the database
        item = Distributor.query.filter_by(name_distributor='testName').first()
        assert item is not None
        assert item.code_distributor == 'testCode'

    def test_api_change_distributor(self):
        """testing PUT request for class DistributorSingle"""
        item=Distributor.query.filter_by(name_distributor='Dfortest').first()
        item.code_distributor='changeCode'
        response=self.client.put(f'/api/distributors/{item.id}',
                                 json={'name_distributor':item.name_distributor,
                                       'code_distributor':item.code_distributor,'adress':item.adress})
        assert response.status_code==200
        # check the data in the database
        elem=Distributor.query.filter_by(name_distributor='Dfortest').first()
        assert elem.code_distributor=='changeCode'
    def test_api_delete_distributor(self):
        """testing DELETE request for class DistributorSingle"""
        item = Distributor.query.filter_by(name_distributor='Dfortest').first()
        assert item is not None
        response=self.client.delete(f'/api/distributors/{item.id}')
        assert response.status_code == 200

    def test_api_outlets_list(self):
        """testing GET request for class OutletList"""
        response = self.client.get('/api/outlet')
        assert response.status_code == 200

    def test_api_add_outlet(self):
        """testing POST request for class OutletList"""
        response=self.client.post('/api/outlet',json=
        {'name_outlet':'testName','code_outlet':'testCode','adress':'adress'})
        assert response.status_code == 200
        #check the data in the database
        item = Outlet.query.filter_by(name_outlet='testName').first()
        assert item is not None
        assert item.code_outlet == 'testCode'

    def test_api_change_outlet(self):
        """testing PUT request for class OutletSingle"""
        item=Outlet.query.filter_by(name_outlet='Ofortest').first()
        item.code_outlet='changeCode'
        response=self.client.put(f'/api/outlet/{item.id}',
                                 json={'name_outlet':item.name_outlet,
                                       'code_outlet':item.code_outlet,'adress':item.adress})
        assert response.status_code==200
        # check the data in the database
        elem=Outlet.query.filter_by(name_outlet='Ofortest').first()
        assert elem.code_outlet=='changeCode'
    def test_api_delete_outlet(self):
        """testing DELETE request for class OutletSingle"""
        item = Outlet.query.filter_by(name_outlet='Ofortest').first()
        assert item is not None
        response=self.client.delete(f'/api/outlet/{item.id}')
        assert response.status_code == 200

if __name__ == '__main__':
    unittest.main()
