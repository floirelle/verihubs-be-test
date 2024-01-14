import unittest
import backend.coin as coin
from unittest.mock import MagicMock
from backend.coin import *
from backend.auth import signup
from backend.models import UserAuth,AddCoinRequest
from backend.exceptions import BadRequestException,ForbiddenAccess,NotFoundException
from backend.db import init_database_if_not_exists

class TestCoin(unittest.TestCase):

    def setUp(cls):
        init_database_if_not_exists("test")

    def get_side_effect(self,value):
        if value == "/assets/5":
            return {"error":"Coin not listed"}
        if value == "/assets/6":
            return {"data":{"name":"name","priceUsd":10}}
        if value == "/assets?ids=6":
            return {"data":[{"name":"name","priceUsd":10}]}
        if value == "/rates/indonesian-rupiah":
            return {"data":{"rateUsd":1}}

    def test_add_coin(self):
        user = UserAuth(
            email = "testuser@gmail.com",
            password = "password",
            password_confirmation = "password"
        )
        test_user = signup(user)
        coin.get = MagicMock(side_effect=self.get_side_effect)
        with self.assertRaises(BadRequestException) as expected:
            coin_request = AddCoinRequest(
                coin_id = "5"
            )
            add_coin(test_user["id"],coin_request)
        self.assertEqual(expected.exception.message,"Coin not listed")

        coin_request = AddCoinRequest(
            coin_id = "6"
        )
        new_coin = add_coin(test_user["id"],coin_request)

        self.assertEqual(new_coin.name,"name")
        self.assertEqual(new_coin.user_id,test_user["id"])
        self.assertEqual(new_coin.price,10)

        with self.assertRaises(BadRequestException) as expected:
            add_coin(test_user["id"],coin_request)
        self.assertEqual(expected.exception.message,"Coin already tracked")

    def test_get_user_coins(self):
        user = UserAuth(
            email = "testuser2@gmail.com",
            password = "password",
            password_confirmation = "password"
        )
        test_user = signup(user)

        self.assertEqual(get_user_coins(test_user["id"]),"No coins tracked")

        coin_request = AddCoinRequest(
            coin_id = "6"
        )
        add_coin(test_user["id"],coin_request)

        self.assertEqual(len(get_user_coins(test_user["id"])),1)

    def test_remove_coins(self):
        user = UserAuth(
            email = "user@gmail.com",
            password = "password",
            password_confirmation = "password"
        )
        test_user = signup(user)
        with self.assertRaises(NotFoundException) as expected:
            remove_coin(9999,test_user["id"])
        self.assertEqual(expected.exception.message,"Resource not found")

        user.email = "user2@gmail.com"
        test_user_2 = signup(user)

        coin_request = AddCoinRequest(
            coin_id = "6"
        )
        other_coin = add_coin(test_user_2["id"],coin_request)

        with self.assertRaises(ForbiddenAccess) as expected:
            remove_coin(other_coin.id,test_user["id"])
        self.assertEqual(expected.exception.message,"Tracked coin is not yours")

        coin_request = AddCoinRequest(
            coin_id = "6"
        )
        test_coin = add_coin(test_user["id"],coin_request)
        deleted_coin = remove_coin(test_coin.id,test_user["id"])
        
        self.assertEqual(deleted_coin.coin_id,"6")
        self.assertEqual(deleted_coin.user_id,test_user["id"])