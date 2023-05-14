import os

class Config:
    # configuración de Flask
    SECRET_KEY = 'postgres'
    
    # configuración de la base de datos
    DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/agroweb'