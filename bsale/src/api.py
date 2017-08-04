#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime
from .constants import Environment
from .clients import Clients
from .document import Document
from .product import Product
from .shipping import Shipping
from .stock import Stock
from .variant import Variant


class BsaleApiCLient(object):
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


def API(token, office_id, document_id, shipping_id):
    """
    inicializa el singleton BsaleApiCLient() 

    @param toke <str> indica el token entregado a la tienda
    @param office_id <str> indica el id de la sucursal a la cual se realizan los cambios 
    @param document_id <str> id del documento boleta 
    @param shipping_id <str> id del documento guia de despacho

    @return : nueva instancia de BsaleApiCLient
    """
    singleton = BsaleApiCLient()

    singleton._token = token
    singleton._office_id = office_id
    singleton._document_id = document_id
    singleton._shipping_id = shipping_id

    return singleton
