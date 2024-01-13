from sqlalchemy import Column,Integer,String,ForeignKey
from db import Base

class Coin(Base):
    __tablename__ = "coin"

    def __init__(self, coin_id, user_id, name, price):
        self.coin_id = coin_id
        self.user_id = user_id
        self.name = name
        self.price = price

    def __str__(self):
        return "A"

    id = Column(Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey("user.id"))
    coin_id = Column(String)
    