#!/usr/bin/python
# -*- coding: UTF-8 -*-


import unittest


from product import ProductTestCase
from document import DocumentTestCase
from stock import StockTestCase
from api import APITestCase
from users import UsersTestCase
from variant import VariantTestCase


__all__ = [
    "ProductTestCase",
    "DocumentTestCase",
    "StockTestCase",
    "ClientTestCase",
    "UsersTestCase",
    "APITestCase",
    "VariantTestCase"
]


if __name__ == "__main__":
    unittest.main(verbosity=2)
