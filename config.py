import os

class Config:
    # configuración de Flask
    SECRET_KEY = 'postgres'
    # configuración de la base de datos
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/agroweb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class GlobalSession:
    __instance = None

    def __init__(self):
        if GlobalSession.__instance is not None:
            raise Exception("Esta clase es un singleton. Use GlobalSession.getInstance() para obtener una instancia.")
        GlobalSession.__instance = self
        self.value = "Hola desde la variable global"

    @staticmethod
    def getInstance():
        if GlobalSession.__instance is None:
            GlobalSession()
        return GlobalSession.__instance
