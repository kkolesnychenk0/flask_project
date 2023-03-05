"""Module describing the models"""
from distribution_app.utils.db import db


class Manufacturer(db.Model):
    """Class describing model Manufacturer"""
    __tablename__='manufacturers'
    id = db.Column(db.Integer,primary_key=True)
    name_manufacturer=db.Column(db.String(80))
    code_manufacturer=db.Column(db.String(40), unique=True)
    country=db.Column(db.String(80))
    distr=db.relationship('Distributor',secondary='manufacturer_distributor',
                          backref='manufacturers',lazy=True)

    def __repr__(self):
        return f'Manufacturer:{self.id},{self.name_manufacturer},' \
               f'{self.code_manufacturer},{self.country}'

    def create(self):
        """creating new manufacturer"""
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """deleting manufacturer"""
        db.session.delete(self)
        db.session.commit()

class Distributor(db.Model):
    """Class describing model Distributor"""
    __tablename__ ='distributors'
    id=db.Column(db.Integer,primary_key=True)
    name_distributor=db.Column(db.String(80))
    code_distributor=db.Column(db.String(40), unique=True)
    adress=db.Column(db.String(80))
    outlets_contracts=db.relationship('Outlet',backref='distributors',lazy=True)

    def __repr__(self):
        return f'Distributor:{self.name_distributor}'

    def create(self):
        """creating new distributor"""
        db.session.add(self)
        db.session.commit()
    def delete(self):
        """deleting distributor"""
        db.session.delete(self)
        db.session.commit()

manufacturer_distributor=db.Table(
    'manufacturer_distributor',
    db.Column('manufacturer_id',db.Integer,db.ForeignKey('manufacturers.id')),
    db.Column('distributor_id',db.Integer,db.ForeignKey('distributors.id')))

class Outlet(db.Model):
    """Class describing model Outlet"""
    __tablename__='outlet'
    id=db.Column(db.Integer,primary_key=True)
    name_outlet=db.Column(db.String(80))
    code_outlet=db.Column(db.String(40), unique=True)
    adress=db.Column(db.String(80))
    distr=db.Column(db.Integer,db.ForeignKey('distributors.id'))

    def __repr__(self):
        return f'Outlet:{self.name_outlet}'
    def create(self):
        """creating outlet"""
        db.session.add(self)
        db.session.commit()
    def delete(self):
        """deleting outlet"""
        db.session.delete(self)
        db.session.commit()
