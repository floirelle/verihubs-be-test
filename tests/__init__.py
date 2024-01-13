import os
from sqlalchemy import URL
from sqlalchemy_utils.functions import drop_database

os.environ["DB_NAME"]="test"
url = URL.create(
    drivername="sqlite",
    database="test.db"
)

try:
    drop_database(url)
except Exception as e:
    pass