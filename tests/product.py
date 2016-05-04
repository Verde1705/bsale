#!/usr/bin/python
# -*- coding: UTF-8 -*-


import unittest

import bsale
# from bsale import *


class ProductTestCase(unittest.TestCase):

    def test_get_products(self):

        self.client = bsale.API()
        products = self.client.product.Get()

        self.assertIn("items", products)
