#!/usr/bin/python
# -*- coding: UTF-8 -*-


import unittest


from .product import ProductTestCase
from .document import DocumentTestCase
from .stock import StockTestCase
from .api import APITestCase
from .users import UsersTestCase
from .variant import VariantTestCase
from .price_list import PriceListTestCase
from .document_type import DocumentTypeTestCase


__all__ = [
    "ProductTestCase",
    "DocumentTestCase",
    "StockTestCase",
    "ClientTestCase",
    "UsersTestCase",
    "APITestCase",
    "VariantTestCase",
    "PriceListTestCase",
    "DocumentTypeTestCase"
]


if __name__ == "__main__":
    unittest.main(verbosity=2)
