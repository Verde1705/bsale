#!/usr/bin/python
# -*- coding: UTF-8 -*-


import unittest

import bsale

from httmock import HTTMock
from tests.mock import mock_api_bsale


class StockTestCase(unittest.TestCase):

    def setUp(self):
        self.bsale_client = bsale.API("")

    def test_get_stock(self):
        with HTTMock(mock_api_bsale):
            stock = self.bsale_client.Stock.Get(officeid=72, limit=1)

    def test_GetOneReception(self):
        with HTTMock(mock_api_bsale):
            stock = bsale.Stock.GetOneReception(id=1)
            self.assertIn("href", stock)
            self.assertIn("id", stock)
            self.assertIn("admissionDate", stock)
            self.assertIn("document", stock)
            self.assertIn("documentNumber", stock)
            self.assertIn("imagestionCctId", stock)
            self.assertIn("imagestionCcDescription", stock)
            self.assertIn("internalDispatchId", stock)
            self.assertIn("office", stock)
            self.assertIn("details", stock)

    def test_GetOneConsumption(self):
        with HTTMock(mock_api_bsale):
            stock = bsale.Stock.GetOneConsumption(id=1)
            self.assertIn("href", stock)
            self.assertIn("id", stock)
            self.assertIn("consumptionDate", stock)
            self.assertIn("note", stock)
            self.assertIn("imagestionCcdescription", stock)
            self.assertIn("imagestionCenterCostId", stock)
            self.assertIn("office", stock)
            self.assertIn("details", stock)
