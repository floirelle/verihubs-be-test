from backend.models import UserAuth,User
from backend.exceptions import BadRequestException,NotAuthorizedException
from backend.utils import hash_password,is_password_valid,generate_jwt_token
from db import get_session
from sqlalchemy import select
from email_validator import validate_email

def get_user_statement(email: str):
    return select(User).filter_by(email=email)

def signup(user: UserAuth):
    try:
        validate_email(user.email)
    except:
        raise BadRequestException("Invalid email")
    if user.password != user.password_confirmation:
        raise BadRequestException("Password confirmation must be same with password")
    
    with get_session() as session:
        if session.scalars(get_user_statement(user.email)).one_or_none() != None:
            raise BadRequestException("email already registered")
        new_user = User(user.email,hash_password(user.password))
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return { "id": new_user.id, "email": new_user.email}

def signin(user: UserAuth):
    with get_session() as session:
        current_user = session.scalars(get_user_statement(user.email)).one_or_none()
        if current_user == None:
            raise NotAuthorizedException()
        if not is_password_valid(user.password,current_user.password_hash):
            raise NotAuthorizedException()

        return {
            "access_token":generate_jwt_token(current_user.id),
        }
