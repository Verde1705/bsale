import unittest
import requests
import bsale
from datetime import datetime

from unittest.mock import MagicMock
from .request_mock import MockResponse


class CoinTestCase(unittest.TestCase):

    def setUp(self):
        self.access_token = 'access_token'
        self.client = bsale.API(self.access_token)
        self.coin_id = 1
        self.original_func_get = requests.get
        self.original_func_post = requests.post

    def test_Get(self):
        body = {
            "href": "https://api.bsale.cl/v1/coins.json",
            "count": 1,
            "limit": 25,
            "offset": 0,
            "items": [
                {
                    "href": "https://api.bsale.cl/v1/coins/3.json",
                    "id": 1,
                    "name": "Peso Clileno",
                    "symbol": "CLP",
                    "decimals": 2,
                    "totalRound": 0
                }
            ]
        }

        requests.get = MagicMock(return_value=MockResponse(
            status_code=200,
            url='url',
            method='GET',
            body=body))

        result = self.client.Coin.Get()
        self.assertIn("href", result)
        self.assertIn("count", result)
        self.assertIn("limit", result)
        self.assertIn("offset", result)
        self.assertIn("items", result)

    def test_GetOne(self):
        body = {
            "href": "https://api.bsale.cl/v1/coins/1.json",
            "id": 1,
            "name": "Peso Chileno",
            "symbol": "$",
            "decimals": 0,
            "totalRound": 0
        }
        requests.get = MagicMock(return_value=MockResponse(
            status_code=200,
            url='url',
            method='GET',
            body=body))

        result = self.client.Payment.GetOne(payment_id=self.coin_id)
        self.assertIn("href", result)
        self.assertIn("id", result)
        self.assertIn("name", result)
        self.assertIn("symbol", result)
        self.assertIn("decimals", result)
        self.assertIn("totalRound", result)

    def test_GetByPaymentType(self):
        body = {
            "exchangeRate": 27204.23
        }

        requests.get = MagicMock(return_value=MockResponse(
            status_code=200,
            url='url',
            method='GET',
            body=body))

        result = self.client.Coin.GetExchangeRate(
            coin_id=self.coin_id, timestamp=datetime.timestamp(datetime.now()))
        self.assertIn("exchangeRate", result)

    def test_Count(self):
        body = {
            "count": 1926
        }

        requests.get = MagicMock(return_value=MockResponse(
            status_code=200,
            url='url',
            method='GET',
            body=body))
        result = self.client.Coin.Count()
        self.assertIn("count", result)

    def tearDown(self):
        requests.get = self.original_func_get
        requests.post = self.original_func_post
