#!/usr/bin/python
# -*- coding: UTF-8 -*-
from .constants import Endpoints
from .endpoint import Endpoint


class Stock(Endpoint):

    @classmethod
    def Get(
        self,
        limit=None,
        offset=None,
        fields=None,
        expand=None,
        officeid=None,
        variantid=None,
        code=None,
        barcode=None
    ):
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
        return self.get(
            Endpoints.STOCKS,
            limit=limit,
            offset=offset,
            fields=fields,
            expand=expand,
            officeid=officeid,
            variantid=variantid,
            code=code,
            barcode=barcode
        )

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

        return self.post(Endpoints.STOCK_RECEPTIONS, params)

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

        return self.post(Endpoints.STOCK_CONSUMPTIONS, params)

    @classmethod
    def GetOneReception(
        self,
        id,
        expand=None

    ):
        """ Get one reception by id from bsale account

        Args:
            id          (int)  : identificador unico de la recepcion
            expand      (list) : permite expandir instancias y
                                 colecciones.

        Returns:
            (dict) Dictionary with the JSON representation of response
        """

        return self.get(
            Endpoints.STOCK_RECEPTIONS_ID.format(id),
            expand=expand,
        )

    @classmethod
    def GetOneConsumption(self, id, expand=None):
        """ Get one consumption by id from bsale account

        Args:
            id          (int)  : identificador unico de la recepcion
            expand      (list) : permite expandir instancias y
                                 colecciones.

        Returns:
            (dict) Dictionary with the JSON representation of response
        """

        return self.get(
            Endpoints.STOCK_CONSUMPTIONS_ID.format(id),
            expand=expand,
        )
