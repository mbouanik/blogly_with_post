from flask import Flask
from models import db


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///blogly"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

    from routes import app_routes

    app.register_blueprint(app_routes)

    return app


app = create_app()
db.init_app(app)
