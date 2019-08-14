import unittest

import bsale

from bsale import *

from httmock import HTTMock
from tests.mock import mock_api_bsale
from .request_mock import MockResponse


class ReturnsTestCase(unittest.TestCase):
    def setUp(self):
        self.access_token = 'access_token'
        self.client = bsale.API(self.access_token)
        self.original_func_get = requests.get
        self.original_func_post = requests.post

    def test_Get(self):
        body = {
            "href": "https://api.bsale.cl/v1/returns.json",
            "count": 1,
            "limit": 1,
            "offset": 0,
            "items": [
                {
                    "href": "url",
                    "id": 1,
                    "code": "137615600351",
                    "returnDate": 1376107200,
                    "motive": "Cambio a Factura",
                    "type": 1,
                    "priceAdjustment": 0,
                    "editTexts": 0,
                    "amount": 27541.0,
                    "office": {
                        "href": "url",
                        "id": "1"
                    },
                    "reference_document": {
                        "href": "url",
                        "id": "472"
                    },
                    "credit_note": {
                        "href": "url",
                        "id": "477"
                    },
                    "details": {
                        "href": "url"
                    }
                }
            ]
        }

        requests.get = MagicMock(return_value=MockResponse(
            status_code=200,
            url='url',
            method='GET',
            body=body))

        result = self.client.Returns.get()
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
