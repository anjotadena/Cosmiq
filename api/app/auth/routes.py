from flask import request
from flask_smorest import Blueprint
from marshmallow import Schema, fields
from .service import AuthService

auth_blp = Blueprint("auth", "auth", url_prefix="/auth", description="Authentication APIs")

# @auth_blp.route("/register", methods=["POST"])
# def register():
#     data = request.get_json()
#     return AuthService.register_user(data)

class LoginSchema(Schema):
    email = fields.String(required=True, description="User email")
    password = fields.String(required=True, description="User password")

class LoginResponseSchema(Schema):
    message = fields.String()
@auth_blp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    return AuthService.login_user(data)


# @auth_blp.route("/forgot-password", methods=["POST"])
# def forgot_password():
#     data = request.get_json()
#     return AuthService.send_reset_email(data["email"])


# @auth_blp.route("/reset-password", methods=["POST"])
# def reset_password():
#     data = request.get_json()
#     return AuthService.reset_password(data["token"], data["new_password"])
