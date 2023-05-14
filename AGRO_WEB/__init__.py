from flask import Flask

def create_app():
    app = Flask(__name__,instance_relative_config=False)
    with app.app_context():
        from .home import home
        from .homeFarmer import homeFarmer
        from .homePlaze import homePlaze

        app.register_blueprint(home.home_bp)
        app.register_blueprint(homeFarmer.homeFarmer_bp)
        app.register_blueprint(homePlaze.homePlaze_bp)
        return app
