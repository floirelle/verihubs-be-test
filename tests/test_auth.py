import unittest
from backend.auth import *
from backend.models import UserAuth
from backend.exceptions import BadRequestException,NotAuthorizedException

class TestAuth(unittest.TestCase):
    
    def test_signup(self):
        with self.assertRaises(BadRequestException) as expected:
            user = UserAuth(
                email = "test",
                password = "password",
                password_confirmation = "password"
            )
            
            signup(user)
        self.assertEqual(expected.exception.message,"Invalid email")

        with self.assertRaises(BadRequestException) as expected:
            user = UserAuth(
                email = "test@gmail.com",
                password = "password",
                password_confirmation = "not_same"
            )
            
            signup(user)
        self.assertEqual(expected.exception.message,"Password confirmation must be same with password")

        user = UserAuth(
            email = "test@gmail.com",
            password = "password",
            password_confirmation = "password"
        )
        registered = signup(user)
        self.assertEqual(user.email, registered["email"])

        with self.assertRaises(BadRequestException) as expected:
            user = UserAuth(
                email = "test@gmail.com",
                password = "password",
                password_confirmation = "password"
            )
            signup(user)
        self.assertEqual(expected.exception.message,"email already registered")

    def test_signin(self):
        user = UserAuth(
                email = "login@gmail.com",
                password = "password",
                password_confirmation = "password"
            )
            
        signup(user)
        
        with self.assertRaises(NotAuthorizedException) as expected:
            login = UserAuth(
                email = "login@gmail.com",
                password = "wrong_password"
            )
            signin(login)
        self.assertEqual(expected.exception.message,"Not authorized error")


