#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import json

from constants import Endpoints, Environment
from endpoint import Endpoint


class Variant(Endpoint):

    @classmethod
    def Get(
        self,
        limit=None,
        offset=None,
        fields=None,
        expand=None,
        description=None,
        barcode=None,
        code=None,
        token=None,
        serialnumber=None,
        productid=None,
        state=None
    ):
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

        # GET /v1/variants.json?limit=10&offset=0
        # GET /v1/variants.json?fields=[description,barCode,code]
        # GET /v1/variants.json?state=0
        # GET /v1/variants.json?productid=26
        # GET /v1/variants.json?expand=[product]

        return self.get(
            Endpoints.VARIANTS,
            limit=limit,
            offset=offset,
            fields=fields,
            expand=expand,
            description=description,
            barcode=barcode,
            code=code,
            token=token,
            serialnumber=serialnumber,
            productid=productid,
            state=state
        )

    @classmethod
    def GetOne(self, variant_id, expand=None):
        # Parametros

        # expand, permite expandir instancias y colecciones.
        # Ejemplos

        # GET /v1/variants/5730.json?expand=[product]
        return self.get(
            Endpoints.VARIANT_ID.format(variant_id),
            expand=expand
        )

    @classmethod
    def Create(self, params):
        # Ejemplo de estructura JSON

        # {
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

        url = Environment.URL + 'variants.json'
        access_token = self.itoken.getToken()

        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            'access_token': access_token
        }

        r = requests.post(url, data=json.dumps(params), headers=headers)

        return r.json()

    def Update(self, params, variantId):
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

        url = Environment.URL + 'variants/' + str(variantId) + '.json'
        access_token = self.itoken.getToken()

        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            'access_token': access_token
        }

        r = requests.put(url, data=json.dumps(params), headers=headers)

        return r.json()

    @classmethod
    def Remove(self, variantId):

        url = Environment.URL + 'variants/' + str(variantId) + '.json'
        access_token = self.itoken.getToken()

        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            'access_token': access_token
        }

        r = requests.delete(url, headers=headers)

        return r.json()

    @classmethod
    def Count(self, state=0):
        # Parametros

        # state, permite filtrar por estado, activos (0) inactivos (1).
        # Respuesta

        # {
        #   "count": 165
        # }
        return self.get(
            Endpoints.COUNT_VARIANTS,
            state=state
        )
