#!/usr/bin/python
# -*- coding: UTF-8 -*-


import unittest

import bsale

from httmock import HTTMock
from bsale.mocks import mock_api_bsale


class PaymentTypesTestCase(unittest.TestCase):

    def setUp(self):
        self.access_token = 'access_token'
        self.client = bsale.API(self.access_token)
        self.payment_type_id = 1

    def test_Get(self):
        with HTTMock(mock_api_bsale):
            result = self.client.PaymentTypes.Get()

            self.assertIn("count", result)
            self.assertIn("limit", result)
            self.assertIn("href", result)
            self.assertIn("offset", result)
            self.assertIn("items", result)

    def test_Create(self):
        with HTTMock(mock_api_bsale):
            result = self.client.PaymentTypes.Create("new payment type")

            self.assertIn("href", result)
            self.assertIn("id", result)
            self.assertIn("name", result)
            self.assertIn("isVirtual", result)
            self.assertIn("isCheck", result)
            self.assertIn("maxCheck", result)
            self.assertIn("isCreditNote", result)
            self.assertIn("isClientCredit", result)
            self.assertIn("isCash", result)
            self.assertIn("isCreditMemo", result)
            self.assertIn("state", result)
            self.assertIn("maxClientCuota", result)
            self.assertIn("ledgerAccount", result)
            self.assertIn("ledgerCode", result)
            self.assertIn("isAgreementBank", result)
            self.assertIn("agreementCode", result)

            self.assertEqual(result["name"], "new payment type")

    def test_GetOne(self):
        with HTTMock(mock_api_bsale):
            result = self.client.PaymentTypes.GetOne(self.payment_type_id)

            self.assertIn("href", result)
            self.assertIn("id", result)
            self.assertIn("name", result)
            self.assertIn("isVirtual", result)
            self.assertIn("isCheck", result)
            self.assertIn("maxCheck", result)
            self.assertIn("isCreditNote", result)
            self.assertIn("isClientCredit", result)
            self.assertIn("isCash", result)
            self.assertIn("isCreditMemo", result)
            self.assertIn("state", result)
            self.assertIn("maxClientCuota", result)
            self.assertIn("ledgerAccount", result)
            self.assertIn("ledgerCode", result)
            self.assertIn("isAgreementBank", result)
            self.assertIn("agreementCode", result)

    def test_Count(self):
        with HTTMock(mock_api_bsale):
            result = self.client.PaymentTypes.Count()

            self.assertIn("count", result)

    def test_GetDynamicAttributes(self):
        with HTTMock(mock_api_bsale):
            result = self.client.PaymentTypes.GetDynamicAttributes(
                self.payment_type_id)

            self.assertIn("count", result)
            self.assertIn("limit", result)
            self.assertIn("href", result)
            self.assertIn("offset", result)
            self.assertIn("items", result)
