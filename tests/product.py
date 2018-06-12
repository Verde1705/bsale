#!/usr/bin/python
# -*- coding: UTF-8 -*-


import unittest

import bsale

from httmock import HTTMock
from tests.mock import mock_api_bsale


class ProductTestCase(unittest.TestCase):

    def test_get_products(self):
        with HTTMock(mock_api_bsale):
            products = bsale.Product.Get()

            assert "count" in products
            assert "items" in products
            assert "limit" in products
            assert "offset" in products

    def test_get_one_product(self):
        with HTTMock(mock_api_bsale):
            self.product = bsale.Product()
            id_product = 2334
            p = self.product.GetOneProduct(id_product)

    def test_update_product(self):

        with HTTMock(mock_api_bsale):
            self.product = bsale.Product()
            id_product = 2334
            name = "Calcetines de Mujer"

            self.product.Update(id_product, name)

    def test_remove_product(self):
        with HTTMock(mock_api_bsale):
            self.product = bsale.Product()
            id_product = 2334
            self.product.Remove(id_product)
    
    def test_count_products(self):
        with HTTMock(mock_api_bsale):
            self.product = bsale.Product()
            self.product.Count()

