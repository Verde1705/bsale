#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json

from .constants import Environment, Endpoints
from .endpoint import Endpoint


class Returns(Endpoint):
    """
    Devoluciones

    Al realizar una petición HTTP, el servicio
    retornara un JSON con la siguiente estructura:
    {
        "href": "https://api.bsale.cl/v1/returns/1.json",
        "id": 1,
        "code": "137615600351",
        "returnDate": 1376107200,
        "motive": "Cambio a Factura",
        "type": 1,
        "priceAdjustment": 0,
        "editTexts": 0,
        "amount": 27541.0,
        "office": {
            "href": "https://api.bsale.cl/v1/offices/1.json",
            "id": "1"
        },
        "reference_document": {
            "href": "https://api.bsale.cl/v1/documents/472.json",
            "id": "472"
        },
        "credit_note": {
            "href": "https://api.bsale.cl/v1/documents/477.json",
            "id": "477"
        },
        "details": {
            "href": "https://api.bsale.cl/v1/returns/1/details.json"
        }
    }

    """

    def Get(
        self,
        limit=None,
        offset=None,
        fields=None,
        expand=None,
        returndate=None,
        code=None,
        type=None,
        officeid=None,
        referencedocumentid=None,
        creditnoteid=None
    ):
        """
        GET lista de devoluciones en bsale
            Args:
                limit                (int)   : limita la cantidad de items
                                            de una respuesta JSON, por
                                            defecto el limit es 25,
                                            el maximo permitido es 50.
                offset               (int)   : permite paginar los items de
                                            una respuesta JSON, por
                                            defecto el offset es 0.
                fields               (list) : solicita lista atributos
                                            de un recurso]
                expand               (list) : permite expandir instancias
                                            y colecciones.
                returndate           (str)  :Permite filtrar por 
                                            fecha de devolución.
                code                 (str)  : filtra por código de la
                                            devolución.

                type                 (str)  : filtra por tipo de
                                            devolución.
                officeid             (int)  : Permite filtrar por sucursal.
                referencedocumentid  (int)  : filtra por documento de
                                            referencia.
                creditnoteid         (str)  : filtra por el id de
                                            la nota de crédito

        """
        return self.get(
            Endpoints.RETURNS,
            limit=limit,
            offset=offset,
            fields=fields,
            expand=expand,
            returndate=returndate,
            code=code,
            type=type,
            officeid=officeid,
            referencedocumentid=referencedocumentid,
            creditnoteid=creditnoteid
        )