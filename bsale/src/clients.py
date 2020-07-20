#!/usr/bin/python
# -*- coding: UTF-8 -*-

from .constants import Endpoints
from .endpoint import Endpoint


class Clients(Endpoint):

    @classmethod
    def Get(
        self,
        limit=None,
        offset=None,
        fields=None,
        expand=None,
        code=None,
        firstname=None,
        lastname=None,
        paymenttypeid=None,
        salesconditionid=None,
        state=None
    ):
        """
        # Parametros

        # limit, limita la cantidad de items de una respuesta JSON,
          si no se envía el limit es 25.
        # offset, permite paginar los items de una respuesta JSON,
          si no se envía el offset es 0.
        # fields, solo devolver atributos específicos de un recurso
        # expand, permite expandir instancias y colecciones.
        # code, Permite filtrar por rut del cliente.
        # firstname, filtra los clientes por nombre.
        # lastname, filtra los clientes por apellido.
        # email, filtra los clientes por email.
        # paymenttypeid, recupera los clientes con forma de pago.
        # salesconditionid, recupera los clientes por la condición de venta.
        # state, boolean (0 o 1) indica si los clientes están
          activos(0) inactivos (1).

        # Ejemplos

        # GET /v1/clients.json?limit=10&offset=0
        # GET /v1/clients.json?fields=[firstname,lastname]
        # GET /v1/clients.json?code=1-9
        # GET /v1/clients.json?paymenttypeid=1
        # GET /v1/clients.json?expand=[contacts,attributes,payment_type]
        """

        return self.get(
            Endpoints.CLIENTS,
            limit=limit,
            offset=offset,
            fields=fields,
            expand=expand,
            code=code,
            firstname=firstname,
            lastname=lastname,
            paymenttypeid=paymenttypeid,
            salesconditionid=salesconditionid,
            state=state
        )

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

        return self.post(Endpoints.CLIENTS, params)

    def Update(self, params, clientId):
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

        return self.post(Endpoints.CLIENT_ID.format(clientId), params)
