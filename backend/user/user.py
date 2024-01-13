from backend.exceptions import NotAuthorizedException
from backend.models import User
from backend.utils import decode_jwt_token
from db import get_session

def get_current_user(token):
    try:
        decoded = decode_jwt_token(token)
        id = decoded["sub"]
        with get_session() as session:
            user = session.get(User,id)
            return user
    except:
        raise NotAuthorizedException

