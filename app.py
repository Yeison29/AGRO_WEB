from flask import Flask
from AGRO_WEB import create_app
from config import Config
import psycopg2

app = create_app()
app.config.from_object(Config)

if __name__ == '__main__':
    app.run(debug=True)