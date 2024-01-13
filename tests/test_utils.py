import unittest
from backend.utils import hash_password,is_password_valid,generate_jwt_token,decode_jwt_token,convert_usd_to_idr

class TestUtils(unittest.TestCase):
    def test_hash_password(self):
        password = "test"
        expected = "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"
        self.assertEqual(hash_password(password),expected)

    def test_is_password_valid(self):
        password = "test"
        hashed_password = "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"
        self.assertEqual(is_password_valid(password,hashed_password),True)
    
    def test_convert_usd_to_idr(self):
        price_in_usd = 1000
        convert_rate = 0.5
        self.assertEqual(convert_usd_to_idr(price_in_usd,convert_rate),2000)
