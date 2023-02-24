from distribution_app.utils.db import db


class Manufacturer(db.Model):
    __tablename__='manufacturers'
    id = db.Column(db.Integer,primary_key=True)
    name_manufacturer=db.Column(db.String(80))
    code_manufacturer=db.Column(db.String(80), unique=True)
    country=db.Column(db.String(80))
    distr=db.relationship('Distributor',secondary='manufacturer_distributor',backref='manufacturers',lazy=True)

    def __repr__(self):
        return f'Manufacturer:{self.id},{self.name_manufacturer},{self.code_manufacturer},{self.country}'

    def json(self):
        return {'name_manufacturer': self.name_manufacturer, 'code_manufacturer': self.code_manufacturer,
                'country': self.country}

class Distributor(db.Model):
    __tablename__ ='distributors'
    id=db.Column(db.Integer,primary_key=True)
    name_distributor=db.Column(db.String(80))
    code_distributor=db.Column(db.String(80), unique=True)
    adress=db.Column(db.String(80))
    outlets_contracts=db.relationship('Outlet',backref='distributors',lazy=True)

    def __repr__(self):
        return f'Distributor:{self.name_distributor}'

manufacturer_distributor=db.Table('manufacturer_distributor',
                                  db.Column('manufacturer_id',db.Integer,db.ForeignKey('manufacturers.id')),
                                  db.Column('distributor_id',db.Integer,db.ForeignKey('distributors.id')))

class Outlet(db.Model):
    __tablename__='outlet'
    id=db.Column(db.Integer,primary_key=True)
    name_outlet=db.Column(db.String(80))
    code_outlet=db.Column(db.String(80), unique=True)
    adress=db.Column(db.String(80))
    distr=db.Column(db.Integer,db.ForeignKey('distributors.id'))

    def __repr__(self):
        return f'Outlet:{self.name_outlet}'


