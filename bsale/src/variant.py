#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import json
import urllib
import inspect

from constants import Environment

class Variant():

    @classmethod
    def Get(self,
            limit=25,
            offset=0,
            fields=None,
            expand=None,
            description=None,
            barcode=None,
            code=None,
            token=None,
            serialnumber=None,
            productid=None,
            state=1):
        # limit, limita la cantidad de items de una respuesta JSON, si no se envía el limit es 25.
        # offset, permite paginar los items de una respuesta JSON, si no se envía el offset es 0.
        # fields, solo devolver atributos específicos de un recurso
        # expand, permite expandir instancias y colecciones.
        # description, Permite filtrar por nombre de la variante.
        # barcode, filtra por código de barra de la variante.
        # code, filtra por código (SKU) de la variante.
        # serialnumber, filtra por numero de serie de la variante.
        # productid, filtra variantes por el id del producto.
        # state, boolean (0 o 1) indica si las variantes están activas(0) o inactivas (1).

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

        url = Environment.URL+'variants.json?'+params
        access_token=Environment.AccessToken

        headers= {'Content-type': 'application/json',
                  'Accept': 'application/json',
                  'access_token':access_token}

        r = requests.get(url, headers=headers)

        return r.json()

    @classmethod
    def Create(self, params):
        # Ejemplo de estructura JSON

        # {
        #   "productId": 595,
        #   "description": "Nintendo Wii U Pro Controller"
        # }

        # print "dataaaaa   -----  {}".format(params) 

        url = Environment.URL+'variants.json'
        access_token=Environment.AccessToken

        headers= {'Content-type': 'application/json',
                  'Accept': 'application/json',
                  'access_token':access_token}

        r = requests.post(url, data=json.dumps(params), headers=headers)

        return r.json()