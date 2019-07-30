import unittest
import requests
import bsale

from unittest.mock import MagicMock
from .request_mock import MockResponse


class PaymentTestCase(unittest.TestCase):

    def setUp(self):
        self.access_token = 'access_token'
        self.client = bsale.API(self.access_token)
        self.payment_id = 1
        self.original_func_get = requests.get
        self.original_func_post = requests.post

    def test_Get(self):
        body = {
            "href": "https://api.bsale.cl/v1/payments.json",
            "count": 1,
            "limit": 1,
            "offset": 0,
            "items": [
                {
                    "href": "https://api.bsale.cl/v1/payments/79.json",
                    "id": 79,
                    "recordDate": 1548720000,
                    "amount": 6000,
                    "operationNumber": None,
                    "accountingDate": "",
                    "checkDate": None,
                    "checkNumber": None,
                    "checkAmount": None,
                    "checkTaken": 0,
                    "isCreditPayment": 0,
                    "createdAt": 1548768524,
                    "state": 0,
                    "payment_type": {
                        "href": "https://api.bsale.cl/v1/"
                        "payment_types/4.json",
                        "id": "4"
                    },
                    "document": {
                        "href": "https://api.bsale.cl/v1/documents/"
                        "195.json",
                        "id": "195"
                    },
                    "office": {
                        "href": "https://api.bsale.cl/v1/"
                        "offices/1.json",
                        "id": "1"
                    },
                    "user": {
                        "href": "https://api.bsale.cl/v1/"
                        "users/1.json",
                        "id": "1"
                    }
                }
            ],
            "next": "https://api.bsale.cl/v1/payments.json?limit=3"
            "\u0026offset=3"
        }
        requests.get = MagicMock(return_value=MockResponse(
            status_code=200,
            url='url',
            method='GET',
            body=body))

        result = self.client.Payment.Get()
        self.assertIn("href", result)
        self.assertIn("count", result)
        self.assertIn("limit", result)
        self.assertIn("offset", result)
        self.assertIn("items", result)
        self.assertIn("next", result)

    def test_GetOne(self):
        body = {
            "href": "https://api.bsale.cl/v1/payments/950.json",
            "id": 1,
            "recordDate": 1396494000,
            "amount": "68643.0",
            "checkDate": None,
            "checkNumber": None,
            "checkAmount": "0",
            "state": 0,
            "payment_type": {
                "href": "https://api.bsale.cl/v1/payment_types/1.json",
                "id": "1"
            },
            "document": {
                "href": "https://api.bsale.cl/v1/documents/3285.json",
                "id": "3285"
            },
            "office": {
                "href": "https://api.bsale.cl/v1/offices/2.json",
                "id": "2"
            },
            "user": {
                "href": "https://api.bsale.cl/v1/users/7.json",
                "id": "7"
            }
        }
        requests.get = MagicMock(return_value=MockResponse(
            status_code=200,
            url='url',
            method='GET',
            body=body))

        result = self.client.Payment.GetOne(payment_id=self.payment_id)
        self.assertIn("href", result)
        self.assertIn("id", result)
        self.assertIn("recordDate", result)
        self.assertIn("amount", result)
        self.assertIn("checkDate", result)
        self.assertIn("checkAmount", result)
        self.assertIn("payment_type", result)
        self.assertIn("document", result)
        self.assertIn("office", result)
        self.assertIn("user", result)

    def test_GetByPaymentType(self):
        body = [{
            "recordDate": 1396494000,
            "paymentTypeTotalAmount": 40906.0,
            "paymentTypeId": 1,
            "paymentTypeName": "Efectivo",
            "paymentLedgerAccount": None,
            "isCheck": 0,
            "isCreditNote": 0,
            "isClientCredit": 0,
            "isCash": 1,
            "isCreditMemo": 0,
            "codesii": "35",
            "officeId": 1,
            "officeName": "Puerto Varas",
            "officeCostCenter": "",
            "details": []
        }]

        requests.get = MagicMock(return_value=MockResponse(
            status_code=200,
            url='url',
            method='GET',
            body=body))

        result = self.client.Payment.GetOne(payment_id=self.payment_id)
        self.assertIn("recordDate", result[0])
        self.assertIn("paymentTypeTotalAmount", result[0])
        self.assertIn("paymentTypeId", result[0])
        self.assertIn("paymentTypeName", result[0])
        self.assertIn("paymentLedgerAccount", result[0])
        self.assertIn("isCheck", result[0])
        self.assertIn("isCreditNote", result[0])
        self.assertIn("isClientCredit", result[0])
        self.assertIn("codesii", result[0])
        self.assertIn("officeId", result[0])
        self.assertIn("officeName", result[0])
        self.assertIn("officeCostCenter", result[0])
        self.assertIn("details", result[0])

    def test_Count(self):
        body = {
            "count": 1926
        }

        result = self.client.Payment.Count()
        requests.get = MagicMock(return_value=MockResponse(
            status_code=200,
            url='url',
            method='GET',
            body=body))
        result = self.client.Payment.Count()
        self.assertIn("count", result)

    def test_Create(self):
        body = {
            "href": "https://api.bsale.cl/v1/payments/4873.json",
            "id": 4873,
            "recordDate": 1436214454,
            "amount": 3791,
            "checkDate": None,
            "checkNumber": None,
            "checkAmount": None,
            "checkTaken": 0,
            "state": 0,
            "payment_type": {
                "href": "https://api.bsale.cl/v1/payment_types/11.json",
                "id": "11"
            },
            "document": {
                "href": "https://api.bsale.cl/v1/documents/3004.json",
                "id": "3004"
            },
            "office": {
                "href": "https://api.bsale.cl/v1/offices/2.json",
                "id": "2"
            },
            "user": {
                "href": "https://api.bsale.cl/v1/users/2.json",
                "id": "2"
            }
        }

        requests.post = MagicMock(return_value=MockResponse(
            status_code=200,
            url='url',
            method='POST',
            body=body))

        result = self.client.Payment.Create(
            document_id=1,
            payment_type_id=1,
            record_date=None,
            amount=None
        )
        self.assertIn("href", result)
        self.assertIn("id", result)
        self.assertIn("recordDate", result)
        self.assertIn("amount", result)
        self.assertIn("checkDate", result)
        self.assertIn("checkNumber", result)
        self.assertIn("checkAmount", result)
        self.assertIn("checkTaken", result)
        self.assertIn("state", result)
        self.assertIn("payment_type", result)
        self.assertIn("document", result)
        self.assertIn("office", result)
        self.assertIn("user", result)

    def tearDown(self):
        requests.get = self.original_func_get
        requests.post = self.original_func_post
