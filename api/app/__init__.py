from flask import Flask


def create_app(config_name="config.Config"):
    app = Flask(__name__)
    app.config.from_object(config_name)

    db.init_app(app)

    # Redis
