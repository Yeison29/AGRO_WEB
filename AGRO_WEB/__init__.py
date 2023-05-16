from flask import Flask
from config import Config
from AGRO_WEB.models.models import db
from config import GlobalSession

def create_app():
    app = Flask(__name__,instance_relative_config=False)
    app.config['GLOBAL_SESSION'] = GlobalSession.getInstance()
    app.config.from_object(Config)
    db.init_app(app)
    with app.app_context():
        from .home import home
        from .homeFarmer import homeFarmer
        from .homePlaze import homePlaze
        import AGRO_WEB.session.session as session

        app.config['GLOBAL_SESSION'].value = session.getSessionUser()

        app.register_blueprint(home.home_bp)
        app.register_blueprint(homeFarmer.homeFarmer_bp)
        app.register_blueprint(homePlaze.homePlaze_bp)

        db.create_all()
        return app
