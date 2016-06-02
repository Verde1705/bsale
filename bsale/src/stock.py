#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import json
from constants import Environment

class Stock():

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
        #lista de stock

        # Parametros

        # limit, limita la cantidad de items de una respuesta JSON, si no se envía el limit es 25.
        # offset, permite paginar los items de una respuesta JSON, si no se envía el offset es 0.
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
                if values[x] != None:
                    arguments[x] = values[x]

        #concatena dic en limit=10&offset=0 por ejemplo
        params=urllib.urlencode(sorted(arguments.items()))

        url = Environment.URL+'stocks.json?'+params
        access_token=Environment.AccessToken

        headers= {'Content-type': 'application/json',
                  'Accept': 'application/json',
                  'access_token':access_token}

        r = requests.get(url, headers=headers)

        return r.json()