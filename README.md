# Prerequisities
    3.10 <= Python < 3.12
# How to run
1. Install the required modules by running `pip install -r requirements.txt`
2. Run the backend server by running `uvicorn backend:app --reload`
3. To see the api list, go to <http:/127.0.0.1:8000/docs>

# How to run test
    pytest --cov=.

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