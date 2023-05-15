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

class Farmer(db.Model):
    __tablename__ = "farmer"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=False, nullable=False)
    lastname= db.Column(db.String(50), unique=False, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    date_of_birth = db.Column(db.DateTime, nullable=False)
    type_identification = db.Column(db.String(250), nullable=False)
    number_identification = db.Column(db.String(250), unique=True, nullable=False)
    genre =  db.Column(db.String(250), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(600), unique=False, nullable=False)
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
    
    @validates('genre')
    def validate_genre(self, key, value):
        allowed_values = ['M', 'F', 'I']
        if value not in allowed_values:
            raise ValueError(f"{value} is not a valid gender.")
        return value

    def __repr__(self):
        return '<Farmer {}>'.format(self.id)
