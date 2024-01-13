import os
from datetime import datetime,timedelta
from hashlib import sha256
from dotenv import load_dotenv
from jose import jwt

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ACCESS_TOKEN_EXPIRY_TIME_MINUTES = 30
ALGORITHM = "HS256"

def hash_password(password:str):
    hash = sha256()
    hash.update(password.encode("utf-8"))
    return hash.hexdigest()

def is_password_valid(password:str, hashed_password:str):
    return hash_password(password) == hashed_password

def generate_jwt_token(id:int):
    access_token = {
        "sub":str(id),
        "exp": datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRY_TIME_MINUTES)
    }

    return jwt.encode(access_token,SECRET_KEY,algorithm=ALGORITHM)

def decode_jwt_token(token: str):
    decoded = jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
    return decoded

def convert_usd_to_idr(price_in_usd,convert_rate):
    return price_in_usd/convert_rate