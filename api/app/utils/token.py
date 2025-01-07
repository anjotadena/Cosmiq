import jwt
from datetime import datetime, timedelta
from config import Config


def generate_reset_token(user_id):
    payload = {
        "exp": datetime.utcnow() + timedelta(hours=1),
        "iat": datetime.utcnow(),
        "sub": user_id,
    }
    return jwt.encode(payload, Config.SECRET_KEY, algorithm="HS256")


def decode_reset_token(token):
    try:
        payload = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
