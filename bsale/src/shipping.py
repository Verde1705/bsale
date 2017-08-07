#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import json
import urllib
import inspect

from .itoken import iToken
from constants import Environment


class Shipping():

    itoken = ""

    def __init__(self, itoken):
        if not isinstance(itoken, iToken):
            raise Exception("itoken, must be an iTokenInstance")

        Shipping.itoken = itoken

    @classmethod
    def Get(self,
            limit=25,
            offset=0,
            fields=None,
            expand=None,
            shippingdate=None,
            officeid=None,
            shippingtypeid=None,
            informedsii=None,
            state=1):

        # GET /v1/shippings.json retornara todos los despachos.

        # Parametros

        # limit, limita la cantidad de items de una respuesta JSON, si no se envía el limit es 25.
        # offset, permite paginar los items de una respuesta JSON, si no se envía el offset es 0.
        # fields, solo devolver atributos específicos de un recurso
        # expand, permite expandir instancias y colecciones.
        # shippingdate, Permite filtrar por fecha de devolución.
        # officeid, Permite filtrar por sucursal.
        # shippingtypeid, filtra por documento de referencia.
        # state, boolean (0 o 1) indica si los documentos están activos(0) inactivos (1).
        
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

        url = Environment.URL+'shippings.json?'+params
        access_token=Environment.AccessToken

        headers= {'Content-type': 'application/json',
                  'Accept': 'application/json',
                  'access_token':access_token}

        r = requests.get(url, headers=headers)

        return r.json()

    @classmethod
    def GetOneShipping(self, idDocument):
        # GET /v1/documents/421.json retorna un documento específico.
        # Parametros

        # expand, permite expandir instancias y colecciones.
        # Ejemplos

        # GET /v1/documents/421.json?expand=[document_type,office]

        url = Environment.URL+'shippings/'+str(idDocument)+'.json'
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
        #   "documentTypeId": 10,
        #   "officeId": 1,
        #   "expirationDate": 1409149934,
        #   "emissionDate": 1409149934,
        #   "shippingTypeId": 6,
        #   "municipality": "Puerto Varas",
        #   "city": "Puerto Varas",
        #   "address": "la quebrada 1005",
        #   "declareSii": 1,
        #   "recipient": "Andres Gallardo",
        #   "details": [
        #     {
        #       "taxId": "[1]",
        #       "quantity": 1,
        #       "comment": "PASAJERO: JAIME GONZALEZ",
        #       "netUnitValue": 12000
        #     }
        #   ],
        #   "client": {
        #     "municipality": "PUERTO MONTT",
        #     "code": "13121776-5",
        #     "activity": "SERV. TELECOMUNICACIONES",
        #     "company": "JAIME ALTAMIRANO SOTO",
        #     "city": "PUERTO MONTT",
        #     "address": "EMILIO RECABARREN 231"
        #   }
        # }


        url = Environment.URL+'shippings.json'
        access_token=Environment.AccessToken

        headers= {'Content-type': 'application/json',
                  'Accept': 'application/json',
                  'access_token':access_token}

        r = requests.post(url, data=json.dumps(params), headers=headers)

        return r.json()

