#!/usr/bin/python
# -*- coding: UTF-8 -*-


import unittest

import bsale

from bsale import *


class ProductTestCase(unittest.TestCase):

    def test_get_products(self):

        self.product = bsale.Product()
        products = self.product.Get()

        print products

        # self.assertIn("items", products)
