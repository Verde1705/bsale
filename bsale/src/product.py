#!/usr/bin/python
# -*- coding: UTF-8 -*-
from .constants import Endpoints
from .endpoint import Endpoint


class Product(Endpoint):

    @classmethod
    def Get(
        self,
        limit=None,
        offset=None,
        fields=None,
        expand=None,
        name=None,
        ledgeraccount=None,
        costcenter=None,
        producttypeid=None,
        state=None
    ):
        # lista de productos

        # Parametros

        # limit, limita la cantidad de items de una respuesta JSON,
        # si no se envía el limit es 25.
        # offset, permite paginar los items de una respuesta JSON,
        # si no se envía el offset es 0.
        # fields, solo devolver atributos específicos de un recurso
        # expand, permite expandir instancias y colecciones.
        # name, Permite filtrar por nombre del producto.
        # ledgeraccount, filtra por cuenta contable de los productos.
        # costcenter, filtra centro de costo de los productos.
        # producttypeid, filtra por tipo de producto.
        # state, boolean (0 o 1) indica si los productos
        # están activos(0) inactivos (1).

        # Ejemplos

        # GET /v1/products.json?limit=10&offset=0
        # GET /v1/products.json?fields=[name,ledgeraccount,description]
        # GET /v1/products.json?producttypeid=1
        # GET /v1/products.json?expand=[product_type]

        # get all parameters
        return self.get(
            Endpoints.PRODUCTS,
            limit=limit,
            offset=offset,
            fields=fields,
            expand=expand,
            name=name,
            ledgeraccount=ledgeraccount,
            costcenter=costcenter,
            producttypeid=producttypeid,
            state=state
        )

    @classmethod
    def GetOneProduct(self, idProduct):

        # Parametros

        # expand, permite expandir instancias y colecciones.

        # Ejemplos

        # GET /v1/products/150.json?expand=[product_type]

        return self.get(Endpoints.PRODUCT_ID.format(idProduct))

    @classmethod
    def Create(
        self,
        name="",
        description="",
        allowDecimal=0,
        ledgerAccount="",
        costCenter="",
        stockControl=1
    ):
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

        return self.post(Endpoints.PRODUCTS, data)

    @classmethod
    def Update(
        self,
        idProduct,
        name="",
        description="",
        allowDecimal=0,
        ledgerAccount="",
        costCenter="",
        stockControl=1
    ):
        # PUT /v1/products/67.json
        # Se debe enviar un Json con la siguiente esctructura.

        # {
        #   "id":"97",
        #   "name": "Calcetines de Mujer",
        # }

        data = {
            "id": idProduct,
            "name": name,
            "description": description,
            "allowDecimal": allowDecimal,
            "ledgerAccount": ledgerAccount,
            "costCenter": costCenter,
            "stockControl": stockControl
        }

        return self.put(Endpoints.PRODUCT_ID.format(idProduct), data)

    @classmethod
    def Remove(self, idProduct):
        # DELETE /v1/products/97.json cambia el estado del producto.

        data = {
            "id": idProduct,
            "state": 1
        }

        return self.put(Endpoints.PRODUCT_ID.format(idProduct), data)

    @classmethod
    def Count(self, state=0):
        # GET /v1/products/count.json
        # Parametros

        # state, permite filtrar por estado, activos (0) inactivos (1).
        # Respuesta

        # {
        # "count": 53
        # }

        return self.Get(
            Endpoints.COUNT_VARIANTS,
            state=state
        )
