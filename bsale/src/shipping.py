#!/usr/bin/python
# -*- coding: UTF-8 -*-

from .constants import Endpoints
from .endpoint import Endpoint


class Shipping(Endpoint):

    @classmethod
    def Get(
        self,
        limit=25,
        offset=0,
        fields=None,
        expand=None,
        shippingdate=None,
        officeid=None,
        shippingtypeid=None,
        informedsii=None,
        state=1
    ):
        """
        # GET /v1/shippings.json retornara todos los despachos.

        # Parametros

        # limit, limita la cantidad de items de una respuesta JSON,
          si no se envía el limit es 25.
        # offset, permite paginar los items de una respuesta JSON,
          si no se envía el offset es 0.
        # fields, solo devolver atributos específicos de un recurso
        # expand, permite expandir instancias y colecciones.
        # shippingdate, Permite filtrar por fecha de devolución.
        # officeid, Permite filtrar por sucursal.
        # shippingtypeid, filtra por documento de referencia.
        # state, boolean (0 o 1) indica si los documentos están
          activos(0) inactivos (1).
        """

        # get all parameters

        return self.get(
            Endpoints.SHIPPINGS,
            limit=limit,
            offset=offset,
            fields=fields,
            expand=expand,
            shippingdate=shippingdate,
            officeid=officeid,
            shippingtypeid=shippingtypeid,
            informedsii=informedsii,
            state=state
        )

    @classmethod
    def GetOneShipping(self, idDocument):
        # GET /v1/documents/421.json retorna un documento específico.
        # Parametros

        # expand, permite expandir instancias y colecciones.
        # Ejemplos

        # GET /v1/documents/421.json?expand=[document_type,office]

        return self.get(Endpoints.SHIPPING_ID.format(idDocument))

    @classmethod
    def GetOneShippingDetails(self, idDocument):
        # GET /v1/shippings/421/details.json retorna los detalles de un documento.

        return self.get(Endpoints.SHIPPING_ID_DETAILS.format(idDocument))

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

        return self.post(Endpoints.SHIPPINGS, params)
