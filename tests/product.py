#!/usr/bin/python
# -*- coding: UTF-8 -*-


import unittest

import bsale

from bsale import *


class ProductTestCase(unittest.TestCase):

    def test_get_products(self):

        self.product = bsale.Product()
        products = self.product.Get()

        # print products

        # self.assertIn("items", products)

    def test_get_one_product(self):
        self.product = bsale.Product()
        id_product=2334
        product = self.product.GetOneProduct(id_product)

        # print product

    # def test_create_product(self):
    #     self.product = bsale.Product()
    #     name="Calcetines"
    #     description="Multiples colores de calcetines"
    #     allowDecimal=0
    #     ledgerAccount="Calcetas"
    #     costCenter="23"
    #     stockControl=1  
    #     product = self.product.Create(name, description, allowDecimal, ledgerAccount, costCenter, stockControl)

    #     print product

    def test_update_product(self):
        self.product = bsale.Product()
        id_product=2334
        name="Calcetines de Mujer"
        # description="Multiples colores de calcetines"
        # allowDecimal=0
        # ledgerAccount="Calcetas"
        # costCenter="23"
        # stockControl=1  
        product = self.product.Update(id_product, name)

        # print product

    def test_remove_product(self):
        self.product = bsale.Product()
        id_product=2334
        product = self.product.Remove(id_product)

        print product
