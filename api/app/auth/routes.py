from flask import Blueprint, request
from .service import AuthService

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    return AuthService.register_user(data)


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    return AuthService.login_user(data)


@auth_bp.route("/forgot-password", methods=["POST"])
def forgot_password():
    data = request.get_json()
    return AuthService.send_reset_email(data["email"])


@auth_bp.route("/reset-password", methods=["POST"])
def reset_password():
    data = request.get_json()
    return AuthService.reset_password(data["token"], data["new_password"])
