from flask import Flask
from AGRO_WEB import create_app

app = create_app()


if __name__ == '__main__':
    app.run(debug=True)