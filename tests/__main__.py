#!/usr/bin/python
# -*- coding: UTF-8 -*-


import unittest


from product import ProductTestCase
from document import DocumentTestCase
from stock import StockTestCase

__all__ = [
    "ProductTestCase",
    "DocumentTestCase",
    "StockTestCase"
]


if __name__ == "__main__":
    unittest.main()
