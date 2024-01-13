import requests
from backend.db import get_session
from backend.models import Coin,AddCoinRequest
from backend.exceptions import NotFoundException,ForbiddenAccess,BadRequestException
from backend.utils import convert_usd_to_idr
from sqlalchemy import select

def get(url):
    base_url = "https://api.coincap.io/v2"
    return requests.get(base_url+url).json()

def add_coin(user_id,coin: AddCoinRequest):
    res = get(f"/assets/{coin.coin_id}")
    if "error" in res:
        raise BadRequestException(res["error"])
    
    exchange_rate = get("/rates/indonesian-rupiah")
    new_coin = Coin(coin.coin_id,user_id,res["data"]["name"],convert_usd_to_idr(float(res["data"]["priceUsd"]),float(exchange_rate["data"]["rateUsd"])))
    with get_session() as session:
        statement = select(Coin).filter_by(coin_id=coin.coin_id,user_id=user_id)
        res = session.scalars(statement).one_or_none()
        if res != None:
            raise BadRequestException("Coin already tracked")
        session.add(new_coin)
        session.commit()
        session.refresh(new_coin)
        return new_coin
    
def get_user_coins(user_id):
    exchange_rate = get("/rates/indonesian-rupiah")
    with get_session() as session:
        statement = select(Coin).filter_by(user_id=user_id)
        coins = session.scalars(statement).all()
        if len(coins) == 0:
            return "No coins tracked"
        res = get(f"/assets?ids={','.join(map(lambda x: str(x.coin_id),coins))}")
        for idx,c in enumerate(coins):
            c.name = res["data"][idx]["name"]
            c.price = convert_usd_to_idr(float(res["data"][idx]["priceUsd"]),float(exchange_rate["data"]["rateUsd"]))
        return coins

def remove_coin(coin_id,user_id):
    with get_session() as session:
        coin = session.get(Coin,coin_id)
        if coin == None:
            raise NotFoundException()
        if coin.user_id != user_id:
            raise ForbiddenAccess("Tracked coin is not yours")
        session.delete(coin)
        session.commit()
        return coin