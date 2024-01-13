import unittest
import sys, os
from sqlalchemy import URL
from sqlalchemy_utils.functions import drop_database,database_exists

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

if __name__ == "__main__":
    os.environ["DB_NAME"]="test"
    url = URL.create(
        drivername="sqlite",
        database="test.db"
    )

    try:
        drop_database(url)
    except Exception as e:
        pass

    loader = unittest.TestLoader()
    start_dir = 'tests'
    suite = loader.discover(start_dir)

    runner = unittest.TextTestRunner()
    runner.run(suite)