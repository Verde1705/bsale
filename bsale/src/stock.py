#!/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    from urllib import urlencode
except:
    from urllib.parse import urlencode

import requests
import json
import inspect

from .itoken import iToken
from .constants import Environment


class Stock():

    itoken = ""

    def __init__(self, itoken):
        if not isinstance(itoken, iToken):
            raise Exception("itoken, must be an iTokenInstance")

        Stock.itoken = itoken

    @classmethod
    def Get(self,
            limit=None,
            offset=None,
            fields=None,
            expand=None,
            officeid=None,
            variantid=None,
            code=None,
            barcode=None):
        # lista de stock

        # Parametros

        # limit, limita la cantidad de items de una respuesta JSON,
        # si no se envía el limit es 25.
        # offset, permite paginar los items de una respuesta JSON,
        # si no se envía el offset es 0.
        # fields, solo devolver atributos específicos de un recurso
        # expand, permite expandir instancias y colecciones.
        # officeid, Permite filtrar por sucursal.
        # variantid, filtra por el identificador de la variante (Integer)
        # code, filtra por el SKU de la variante (String).
        # barcode, filtra por el codigo de barras de la variante (String).

        # Ejemplos

        # GET /v1/stocks.json?limit=10&offset=0
        # GET /v1/stocks.json?fields=[quantity]
        # GET /v1/stocks.json?expand=[office,variant]

        # get all parameters
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        arguments = dict()

        for x in args:
            if x != 'self':
                if values[x] is not None:
                    arguments[x] = values[x]

        # concatena dic en limit=10&offset=0 por ejemplo
        params = urlencode(sorted(arguments.items()))

        url = Environment.URL + 'stocks.json?' + params
        access_token = self.itoken.getToken()

        headers = {'Content-type': 'application/json',
                   'Accept': 'application/json',
                   'access_token': access_token}

        r = requests.get(url, headers=headers)

        return r.json()

    @classmethod
    def AddStock(self, params):
        # POST /v1/stocks/receptions.json
        # Se debe enviar un Json con la siguiente estructura.

        # {
        #   "document": "Guía",
        #   "officeId": 1,
        #   "documentNumber": "123",
        #   "note": "prueba api",
        #   "details": [
        #     {
        #       "quantity": 32.22,
        #       "variantId": 629,
        #       "cost": 3200
        #     }
        #   ],
        # }
        url = Environment.URL + 'stocks/receptions.json'
        access_token = self.itoken.getToken()

        headers = {'Content-type': 'application/json',
                   'Accept': 'application/json',
                   'access_token': access_token}

        r = requests.post(url, data=json.dumps(params), headers=headers)

        return r.json()

    @classmethod
    def RemoveStock(self, params):
        # POST /v1/stocks/consumptions.json
        # Se debe enviar un Json con la siguiente estructura.
        # officeId es el id de la "sucursal" en bsale

        # {
        #   "note": "prueba api",
        #   "officeId": 1,
        #   "details": [
        #     {
        #       "quantity": 13,
        #       "variantId": 629
        #     }
        #   ]
        # }

        url = Environment.URL + 'stocks/consumptions.json'
        access_token = self.itoken.getToken()

        headers = {'Content-type': 'application/json',
                   'Accept': 'application/json',
                   'access_token': access_token}

        r = requests.post(url, data=json.dumps(params), headers=headers)

        return r.json()
