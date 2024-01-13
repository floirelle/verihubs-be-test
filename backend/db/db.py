import os
from backend.db import Base
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy_utils.functions import create_database,database_exists
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import logging

logger = logging.getLogger()
load_dotenv()

url = None

def get_url(db_name=None):
    global url
    if url != None:
        return url
    
    if db_name != None:
        os.environ["DB_NAME"] = db_name
    
    url = URL.create(
        drivername="sqlite",
        database=os.getenv("DB_NAME","data")+".db"
    )

    return url

def init_db(url):
    create_database(url)
    engine = create_engine(url)
    Base.metadata.create_all(engine)

def init_database_if_not_exists(db_name=None):
    if(not database_exists(get_url(db_name))):
       init_db(url)

def get_session():
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    return Session()