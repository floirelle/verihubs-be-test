from pydantic import BaseModel, EmailStr
from typing import Optional

class UserAuth(BaseModel):
    email: str
    password: str
    password_confirmation: Optional[str] = None

class AddCoinRequest(BaseModel):
    coin_id: str