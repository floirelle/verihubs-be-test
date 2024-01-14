# Prerequisities
   Python 3.9
# How to run
1. Install the required modules by running `pip install -r requirements.txt`
2. Run the backend server by running `uvicorn backend.app:app`
3. To see the api list, go to <http:/127.0.0.1:8000/docs>

# How to run test
    pytest --cov=.

# Live Service
Access the api here <https://verihubs-be.onrender.com/>

# Test Coverage
Name                                     Stmts   Miss  Cover
------------------------------------------------------------
backend\__init__.py                          0      0   100%
backend\app.py                              52     52     0%
backend\auth\__init__.py                     1      0   100%
backend\auth\auth.py                        31      2    94%
backend\coin\__init__.py                     1      0   100%
backend\coin\coin.py                        46      2    96%
backend\db\__init__.py                       3      0   100%
backend\db\db.py                            29      0   100%
backend\exceptions\__init__.py               6      0   100%
backend\exceptions\bad_request.py            4      0   100%
backend\exceptions\base.py                   5      0   100%
backend\exceptions\forbidden_access.py       4      0   100%
backend\exceptions\internal_server.py        4      1    75%
backend\exceptions\not_authorized.py         4      0   100%
backend\exceptions\not_found.py              4      0   100%
backend\models\__init__.py                   3      0   100%
backend\models\coin.py                      14      1    93%
backend\models\request.py                    8      0   100%
backend\models\user.py                      10      0   100%
backend\response\__init__.py                 1      1     0%
backend\response\base.py                     5      5     0%
backend\user\__init__.py                     1      1     0%
backend\user\user.py                        13     13     0%
backend\utils\__init__.py                   23      4    83%
tests\__init__.py                            9      2    78%
tests\test_auth.py                          31      0   100%
tests\test_coin.py                          61      0   100%
tests\test_utils.py                         15      0   100%
------------------------------------------------------------
TOTAL                                      388     84    78%

# TASK
Coding Test Backend

Duration: 3 Days

1. Build a JSON REST API service using Python FASTAPI as a backend of a cryptocurrencies price tracker web app.
2. Use <https://docs.coincap.io> as a source of the price.
3. Use SQLite as database.
4. You must implement REST API endpoints to do:
    a. Signup (email, password, password confirmation)
    b. Signin (email and password). API user will get a JWT Token to identify user.
    c. Authenticated user can signout.
    d. Authenticated user can show user list of tracked coins (name of coin and price in rupiah)
    e. Authenticated user can add coin to tracker.
    f. Authenticated user can remove coin from tracker.
5. Bonus point if you can add tests.
6. Bonus point if you can deploy the service online.
7. Please share your public git repository to us with clear README to run your service.

---