from app.auth.models import User
from app.extensions import db
from app.utils.token import generate_reset_token, decode_reset_token
from app.utils.email import send_email


class AuthService:
    @staticmethod
    def register_user(data):
        if User.query.filter_by(email=data["email"]).first():
            return {"message": "Email already exists"}, 400
        user = User(username=data["username"], email=data["email"])
        user.set_password(data["password"])
        db.session.add(user)
        db.session.commit()

        return {"message": "User registered successfully"}, 201

    @staticmethod
    def login_user(data):
        user = User.query.filter_by(email=data["email"]).first()
        if not user or not user.check_password(data["password"]):
            return {"message": "Invalid credentials"}, 401

        from flask_jwt_extended import create_access_token

        token = create_access_token(identity=user.id)
        return {"access_token": token}, 200

    @staticmethod
    def send_reset_email(email):
        user = User.query.filter_by(email=email).first()
        if not user:
            return {"message": "Invalid email address"}, 404
        token = generate_reset_token(user.id)
        send_email(email, "Reset Your Password", f"Your reset token: {token}")
        return {"message": "Reset email sent"}, 200

    @staticmethod
    def reset_password(token, new_password):
        user_id = decode_reset_token(token)

        if not user_id:
            return {"message": "Invalid or expired token"}, 400

        user = User.query.get(user_id)

        if not user:
            return {"message": "User not found"}, 404

        user.set_password(new_password)
        db.session.commit()

        return {"message": "Password reset successfully"}, 200
