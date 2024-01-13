from pydantic import BaseModel, EmailStr

class UserAuth(BaseModel):
    email: str
    password: str
    password_confirmation: str | None = None

class AddCoinRequest(BaseModel):
    coin_id: str