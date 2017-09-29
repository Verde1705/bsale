#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import json
import urllib
import inspect

from .itoken import iToken
from constants import Environment


class Clients():

    itoken = ""

    def __init__(self, itoken):
        if not isinstance(itoken, iToken):
            raise Exception("itoken, must be an iTokenInstance")

        Clients.itoken = itoken

    @classmethod
    def Get(self,
            limit=None,
            offset=None,
            fields=None,
            expand=None,
            code=None,
            firstname=None,
            lastname=None,
            paymenttypeid=None,
            salesconditionid=None,
            state=None):
        # Parametros

        # limit, limita la cantidad de items de una respuesta JSON, si no se envía el limit es 25.
        # offset, permite paginar los items de una respuesta JSON, si no se envía el offset es 0.
        # fields, solo devolver atributos específicos de un recurso
        # expand, permite expandir instancias y colecciones.
        # code, Permite filtrar por rut del cliente.
        # firstname, filtra los clientes por nombre.
        # lastname, filtra los clientes por apellido.
        # email, filtra los clientes por email.
        # paymenttypeid, recupera los clientes con forma de pago.
        # salesconditionid, recupera los clientes por la condición de venta.
        # state, boolean (0 o 1) indica si los clientes están activos(0) inactivos (1).

        # Ejemplos

        # GET /v1/clients.json?limit=10&offset=0
        # GET /v1/clients.json?fields=[firstname,lastname]
        # GET /v1/clients.json?code=1-9
        # GET /v1/clients.json?paymenttypeid=1
        # GET /v1/clients.json?expand=[contacts,attributes,payment_type]

        # get all parameters
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        arguments = dict()

        for x in args:
            if x != 'self':
                if values[x] is not None:
                    arguments[x] = values[x]

        # concatena dic en limit=10&offset=0 por ejemplo
        params = urllib.urlencode(sorted(arguments.items()))

        url = Environment.URL + 'clients.json?' + params
        access_token = self.itoken.getToken()

        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            'access_token': access_token
        }

        r = requests.get(url, headers=headers)

        return r.json()

    @classmethod
    def Create(self, params):
        # Ejemplo de estructura JSON

        # {
        #   "facebook": "",
        #   "municipality": "Las Condes",
        #   "phone": "66287196",
        #   "activity": "Venta de ropa",
        #   "city": "Santiago",
        #   "maxCredit": 100000,
        #   "hasCredit": 1,
        #   "lastName": "Muñoz",
        #   "note": "Cliente premiun",
        #   "firstName": "Marcela",
        #   "company": "Particular",
        #   "address": "Los trigales 372",
        #   "email": "mmunoz@.email.cl",
        #   "twitter": "",
        #   "code": "2-7"
        # }

        url = Environment.URL + 'clients.json'
        access_token = self.itoken.getToken()

        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            'access_token': access_token
        }

        r = requests.post(url, data=json.dumps(params), headers=headers)

        return r.json()

    def Update(seff, params, clientId):
        # Ejemplo de estructura JSON que recibe

        # {
        #   "id": 2110,
        #   "productId": 595,
        #   "description": "Nintendo Wii U Pro Controller",
        #   "code": "xxx-xxx-xxx",      //code es sku
        #   "attribute_values": [
        #    {
        #      "description": "Nintendo",
        #      "attributeId": 46
        #    },
        #    {
        #      "description": "Wii U",
        #      "attributeId": 47
        #    }
        #  ]
        # }

        # print "dataaaaa   -----  {}".format(params)

        url = Environment.URL + 'clients/' + clientId + '.json'
        access_token = self.itoken.getToken()

        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            'access_token': access_token
        }

        r = requests.post(url, data=json.dumps(params), headers=headers)

        return r.json()
