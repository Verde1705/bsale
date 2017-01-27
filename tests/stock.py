#!/usr/bin/python
# -*- coding: UTF-8 -*-


import unittest

import bsale


class StockTestCase(unittest.TestCase):

    def test_get_stock(self):
        stock = bsale.Stock.Get(officeid=72, limit=1)
        print stock