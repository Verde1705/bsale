#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import json
from constants import Environment

class Product():
    """docstring for Product"""

    def test(self):
        print "llega"

    @classmethod
    def Get(cls):
        #lista de productos

        # Parametros

        # limit, limita la cantidad de items de una respuesta JSON, si no se envía el limit es 25.
        # offset, permite paginar los items de una respuesta JSON, si no se envía el offset es 0.
        # fields, solo devolver atributos específicos de un recurso
        # expand, permite expandir instancias y colecciones.
        # name, Permite filtrar por nombre del producto.
        # ledgeraccount, filtra por cuenta contable de los productos.
        # costcenter, filtra centro de costo de los productos.
        # producttypeid, filtra por tipo de producto.
        # state, boolean (0 o 1) indica si los productos están activos(0) inactivos (1).

        # Ejemplos

        # GET /v1/products.json?limit=10&offset=0
        # GET /v1/products.json?fields=[name,ledgeraccount,description]
        # GET /v1/products.json?producttypeid=1
        # GET /v1/products.json?expand=[product_type]

        url = Environment.URL+'products.json'
        access_token=Environment.AccessToken

        headers= {'Content-type': 'application/json',
                  'Accept': 'application/json',
                  'access_token':access_token}

        r = requests.get(url, headers=headers)

        return r.json()

    def GetOneProduct(self, idProduct):

        # Parametros

        # expand, permite expandir instancias y colecciones.

        # Ejemplos

        # GET /v1/products/150.json?expand=[product_type]

        url = Environment.URL+'products/'+str(idProduct)+'.json'
        access_token=Environment.AccessToken

        headers= {'Content-type': 'application/json',
                  'Accept': 'application/json',
                  'access_token':access_token}

        r = requests.get(url, headers=headers)

        return r.json()

    def Create(self,
                   name="",
                   description="",
                   allowDecimal=0,
                   ledgerAccount="",
                   costCenter="",
                   stockControl=1):
        # POST /v1/products.json
        # Se debe enviar un Json con la siguiente estructura.

        # {
        #   "name": "Calcetines",
        #   "description": "Multiples colores de calcetines",
        #   "allowDecimal": 0,
        #   "ledgerAccount": "Calcetas",
        #   "costCenter": "23",
        #   "stockControl": 1  
        # }

        data = {
          "name": name,
          "description": description,
          "allowDecimal": allowDecimal,
          "ledgerAccount": ledgerAccount,
          "costCenter": costCenter,
          "stockControl": costCenter  
        }

        url = Environment.URL+'products.json'
        access_token=Environment.AccessToken

        headers= {'Content-type': 'application/json',
                  'Accept': 'application/json',
                  'access_token':access_token}

        r = requests.post(url, data=json.dumps(data), headers=headers)

        return r.json()

    def Update(self,
            idProduct,
            name="",
            description="",
            allowDecimal=0,
            ledgerAccount="",
            costCenter="",
            stockControl=1):
        # PUT /v1/products/67.json
        # Se debe enviar un Json con la siguiente esctructura.

        # {
        #   "id":"97",
        #   "name": "Calcetines de Mujer", 
        # }

        data = {
          "id":idProduct, 
          "name": name,
          "description": description,
          "allowDecimal": allowDecimal,
          "ledgerAccount": ledgerAccount,
          "costCenter": costCenter,
          "stockControl": costCenter  
        }

        url = Environment.URL+'products/'+str(idProduct)+'.json'
        access_token=Environment.AccessToken

        headers= {'Content-type': 'application/json',
                  'Accept': 'application/json',
                  'access_token':access_token}

        r = requests.put(url, data=json.dumps(data), headers=headers)

        return r.json()

    def Remove(self,idProduct):
        # DELETE /v1/products/97.json cambia el estado del producto.

        data = {
          "id":idProduct, 
          "state":1
        }

        url = Environment.URL+'products/'+str(idProduct)+'.json'
        access_token=Environment.AccessToken

        headers= {'Content-type': 'application/json',
                  'Accept': 'application/json',
                  'access_token':access_token}

        r = requests.put(url, data=json.dumps(data), headers=headers)

        return r.json()