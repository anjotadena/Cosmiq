from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from email.message import EmailMessage

db = SQLAlchemy()
jwt = JWTManager()
mail = EmailMessage()
