from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from flask_mail import Mail

db = SQLAlchemy()
redis_client = FlaskRedis()
mail = Mail()
