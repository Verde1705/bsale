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

    def Create(self, params):
        """
        {
            "documentTypeId": 9,
            "officeId": 1,
            "referenceDocumentId": 11528,
            "expirationDate": 1407384000,
            "emissionDate": 1407384000,
            "motive": "prueba api",
            "declareSii": 1,
            "priceAdjustment": 0,
            "editTexts": 0,
            "type": 1,
            "client": {
                "code": "1-9",
                "city": "Puerto Varas",
                "municipality": "comuna",
                "activity": "giro",
                "address": "direccion"
            },
            "details": [
                {
                    "documentDetailId": 21493,
                    "quantity": 1,
                    "unitValue": 0
                }
            ]
        }
        """

        url = Environment.URL + Endpoints.RETURNS
        access_token = self.itoken.getToken()

        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            'access_token': access_token
        }

        r = requests.post(url, data=json.dumps(params), headers=headers)

        return r.json()
