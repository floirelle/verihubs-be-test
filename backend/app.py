import sys,os
from fastapi import FastAPI,Request,Response
from fastapi.responses import JSONResponse
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from backend.models import UserAuth,AddCoinRequest
from backend.auth import auth
from backend.coin import coin
from backend.user import get_current_user
from backend.response import BaseResponse
from backend.exceptions import BaseException
from db import init_database_if_not_exists

init_database_if_not_exists()
app = FastAPI()

@app.exception_handler(BaseException)
async def handle_exception(request: Request, exc: BaseException):
    return JSONResponse(
        status_code=exc.status_code,
        content = vars(exc)
    )

@app.post("/users", status_code=201)
def create_user(user: UserAuth):
    return BaseResponse(201,"user created",auth.signup(user))

@app.post("/auth",status_code=200)
def signin(user: UserAuth, response: Response):
    res = auth.signin(user)
    response.set_cookie("token",res["access_token"])
    return BaseResponse(200,"user authenticated",res)

@app.post("/signout",status_code=200)
def signout(response: Response):
    response.set_cookie("token","")
    return BaseResponse(200,"ok")

auth_app = FastAPI()

@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    if not should_skip_auth(request.method, request.url.path):
        token = request.cookies.get("token")
        if token == "":
            return JSONResponse(vars(BaseResponse(401,"Not authorized")),401)
        user = get_current_user(token)    
        request.state.id = int(user.id)
    return await call_next(request)

@app.post("/coins",status_code=200)
def add_coin(body:AddCoinRequest, request:Request):
    return BaseResponse(200,"ok",coin.add_coin(request.state.id,body))

@app.get("/coins",status_code=200)
def add_coin(request:Request):
    return BaseResponse(200,"ok",coin.get_user_coins(request.state.id))

@app.delete("/coins/{coin_id}",status_code=200)
def remove_coin(coin_id,request:Request):
    return BaseResponse(200,"ok",coin.remove_coin(coin_id,request.state.id))

def should_skip_auth(method,path):
    excluded_paths=[
        {"method": "POST", "path": "/users"},
        {"method": "POST", "path": "/signout"},
        {"method": "POST", "path": "/auth"},
        {"method": "GET", "path": "/openapi.json"},
        {"method": "GET", "path": "/docs"},
    ]

    for req in excluded_paths:
        if method == req["method"] and path == req["path"]:
            return True
    return False