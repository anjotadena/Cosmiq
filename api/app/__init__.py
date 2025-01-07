from flask import Flask
from flask_smorest import Api, Blueprint
from marshmallow import Schema, fields
from .extensions import db


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")
    
    # Flask-Smorest Configurations
    app.config["API_TITLE"] = "Cosmiq API"
    app.config["API_VERSION"] = "1.0"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_REDOC_PATH"] = "/"
    app.config["OPENAPI_REDOC_URL"] = "https://cdn.jsdelivr.net/npm/redoc/bundles/redoc.standalone.js"

    api = Api(app)

    from app.auth.routes import auth_blp
    
    api.register_blueprint(auth_blp)

    db.init_app(app)

    return app
