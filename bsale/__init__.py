#!/usr/bin/python
# -*- coding: UTF-8 -*-


from .src.product import Product
from .src.api import API
from .src.document import Document
from .src.stock import Stock
from .src.variant import Variant
from .src.shipping import Shipping
from .src.clients import Clients


__all__ = [
    "API",
    "Product", 
    "Document",
    "Stock",
    "Variant",
    "Shipping",
    "Clients"
]
