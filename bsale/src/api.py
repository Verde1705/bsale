#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime
from .clients import Clients
from .document import Document
from .product import Product
from .shipping import Shipping
from .stock import Stock
from .variant import Variant
from .users import Users
from .itoken import iToken
from .price_list import PriceList
from .document_type import DocumentType
from .payment_types import PaymentTypes


class BsaleApiCLient(iToken):
    # return "hola"
    @property
    def token(self):
        return self._token

    @property
    def office_id(self):
        return self.office_id

    @property
    def document_id(self):
        return self._document_id

    @property
    def shipping_id(self):
        return self._shipping_id

    def __init__(self):
        self._token = ''
        self._office_id = ''
        self._document_id = ''
        self._shipping_id = ''

        self.Document = Document(self)
        self.Clients = Clients(self)
        self.Product = Product(self)
        self.Shipping = Shipping(self)
        self.Stock = Stock(self)
        self.Variant = Variant(self)
        self.Users = Users(self)
        self.PriceList = PriceList(self)
        self.DocumentType = DocumentType(self)
        self.PaymentTypes = PaymentTypes(self)

    # itoken implementation
    def getToken(self):
        return self.token


def API(token):
    """
    inicializa el singleton BsaleApiCLient()

    @param token <str> indica el token entregado a la tienda

    @return : nueva instancia de BsaleApiCLient
    """
    singleton = BsaleApiCLient()
    singleton._token = token

    return singleton
