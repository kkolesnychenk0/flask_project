import unittest
from distribution_app import create_app, config_dict, db

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config=config_dict['test'])
        self.appctx = self.app.app_context()
        self.appctx.push()
        self.client = self.app.test_client()

        db.create_all()
    def tearDown(self):
        db.drop_all()

        self.appctx.pop()
        self.app = None
        self.client = None
    def test_manufacturers_list(self):
        response = self.client.get('/api/')
        assert response.status_code==200

    def test_manufacturer_add(self):
        data={
            'name_manufacturer':'test',
            'code_manufacturer':'code-test',
            'country':'country-test'
        }
        response=self.client.post('/api/',json=data)
        assert response.status_code==201


if __name__=='__main__':
    unittest.main()