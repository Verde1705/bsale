#!/usr/bin/python
# -*- coding: UTF-8 -*-


import unittest

import bsale

from httmock import HTTMock
from tests.mock import mock_api_bsale


class StockTestCase(unittest.TestCase):

    def test_get_stock(self):
        with HTTMock(mock_api_bsale):
            stock = bsale.Stock.Get(officeid=72, limit=1)
