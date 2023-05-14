import os

class Config:
    # configuración de Flask
    SECRET_KEY = 'postgres'
    # configuración de la base de datos
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/agroweb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False