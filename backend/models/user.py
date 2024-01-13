from sqlalchemy import Column,Integer,String
from db import Base

class User(Base):
    __tablename__ = "user"

    def __init__(self, email, password_hash):
        self.email = email
        self.password_hash = password_hash

    id = Column(Integer,primary_key=True)
    email = Column(String)
    password_hash = Column(String)
