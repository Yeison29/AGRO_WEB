from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Country(db.Model):
    __tablename__ = "country"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    zip_code = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Country {}>'.format(self.id)
    
class Department(db.Model):
    __tablename__ = "department"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    zip_code = db.Column(db.String(50), unique=True, nullable=False)
    fk_country = db.Column(db.Integer, ForeignKey('country.id'), unique=False, nullable=False)
    country = relationship(Country)

    def __repr__(self):
        return '<Department {}>'.format(self.id)
    
class City(db.Model):
    __tablename__ = "city"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=False, nullable=False)
    zip_code = db.Column(db.String(50), unique=False, nullable=False)
    fk_department = db.Column(db.Integer, ForeignKey('department.id'), unique=False, nullable=False)
    department = relationship(Department)
    def __repr__(self):
        return '<City {}>'.format(self.id)

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=False, nullable=False)
    lastname= db.Column(db.String(50), unique=False, nullable=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    date_of_birth = db.Column(db.DateTime, nullable=False)
    type_identification = db.Column(db.String(250), nullable=True)
    number_identification = db.Column(db.String(250), unique=True, nullable=False)
    gender =  db.Column(db.String(250), nullable=True)
    phone = db.Column(db.String(10), unique=False, nullable=False)
    address = db.Column(db.String(600), unique=False, nullable=False)
    type_user = db.Column(db.String(1), unique=False, nullable=False)
    fk_country = db.Column(db.Integer, ForeignKey('country.id'), unique=False, nullable=False)
    country = relationship(Country)
    fk_department = db.Column(db.Integer, ForeignKey('department.id'), unique=False, nullable=False)
    department = relationship(Department)
    fk_city = db.Column(db.Integer, ForeignKey('city.id'), unique=False, nullable=False)
    city = relationship(City)
 
    @validates('type_identification')
    def validate_type_identification(self, key, value):
        allowed_values = ['T.I', 'C.C', 'C.E', 'R.C', 'P.E.P', 'N.U.I.P']
        if value not in allowed_values:
            raise ValueError(f"{value} is not a valid type of identification.")
        return value
    
    @validates('gender')
    def validate_gender(self, key, value):
        allowed_values = ['M', 'F', 'I']
        if value not in allowed_values:
            raise ValueError(f"{value} is not a valid gender.")
        return value
    
    @validates('type_user')
    def validate_type_identification(self, key, value):
        allowed_values = ['T', 'A', 'P', 'S']
        if value not in allowed_values:
            raise ValueError(f"{value} is not a valid type of identification.")
        return value

    def __repr__(self):
        return '<User {}>'.format(self.id)
    
class ProductPlaze(db.Model):
    __tablename__ = "productPlaze"
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(50), unique=True, nullable=False)
    name_product = db.Column(db.String(250), unique=False, nullable=False)
    unit_kg = db.Column(db.String(50), unique=False, nullable=False)
    fk_user = db.Column(db.Integer, ForeignKey('user.id'), unique=False, nullable=False)
    user = relationship(User)


    def __repr__(self):
        return '<ProductPlaze {}>'.format(self.id)

class PricePlaze(db.Model):
    __tablename__ = "pricesPlaze"
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, unique=False, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    fk_product_plaze = db.Column(db.Integer, ForeignKey('productPlaze.id'), unique=False, nullable=False)
    product_plaze = relationship(ProductPlaze)


    def __repr__(self):
        return '<PricePlaze {}>'.format(self.id)
    
# class PriceSupplieAgricultural(db.Model):
#     __tablename__ = "priceSupplieAgricultural"
#     id = db.Column(db.Integer, primary_key=True)
#     code = db.Column(db.String(50), unique=True, nullable=False)
#     name = db.Column(db.String(250), unique=False, nullable=False)
#     price = db.Column(db.d, unique=False, nullable=False)
#     fk_user = db.Column(db.Integer, ForeignKey('user.id'), unique=False, nullable=False)
#     user = relationship(User)


#     def __repr__(self):
#         return '<PriceSupplieAgricultural {}>'.format(self.id)


class RequestProductPlaze(db.Model):
    __tablename__ = "requestProductPlaze"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    price_max = db.Column(db.Float, unique=False, nullable=False)
    price_min = db.Column(db.Float, unique=False, nullable=False)
    quantity = db.Column(db.Float, unique=False, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    fk_product_plaze = db.Column(db.Integer, ForeignKey('productPlaze.id'), unique=False, nullable=False)
    product_plaze = relationship(ProductPlaze)


    def __repr__(self):
        return '< RequestProductPlaze {}>'.format(self.id)

class Harvest(db.Model):
    __tablename__ = "harvest"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_harvest = db.Column(db.String(250), unique=False, nullable=False)
    def __repr__(self):
        return '< Harvest {}>'.format(self.id)
    
class ControlHarvest(db.Model):
    __tablename__ = "control_harvest"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hectares=db.Column(db.Float, unique=False, nullable=False)
    date_init = db.Column(db.DateTime, nullable=False)
    date_fin = db.Column(db.DateTime, nullable=False)
    time_production = db.Column(db.Integer, nullable=False)
    fk_user = db.Column(db.Integer, ForeignKey('user.id'), unique=False, nullable=False)
    user = relationship(User)
    fk_harvest= db.Column(db.Integer, ForeignKey('harvest.id'), unique=False, nullable=False)
    harvest=relationship(Harvest)
