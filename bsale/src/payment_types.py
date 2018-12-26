#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import json

from constants import Endpoints, Environment
from endpoint import Endpoint


class PaymentTypes(Endpoint):

    @classmethod
    def Get(
        self,
        limit=None,
        offset=None,
        fields=None,
        expand=None,
        name=None,
        ledgeraccount=None,
        state=None
    ):
        """ Get all the payment types from bsale account

        Args:
            limit         (int)  : limita la cantidad de items de una
                                    respuesta JSON, por defecto el limit
                                    es 25, el máximo permitido es 50.
            offset        (int)  : permite paginar los items de una
                                    respuesta JSON, por defecto el
                                    offset es 0.
            fields        (list) : solo devolver atributos específicos de
                                    un recurso.
            expand        (list) : permite expandir instancias y
                                    colecciones.
            name          (str)  : Permite filtrar por nombre de la forma
                                    de pago.
            ledgeraccount (str)  : cuenta contable de la forma de pago
            state         (int)  : boolean (0 o 1) indica si las formas de
                                    pago están activas(0) inactivas(1).
        Returns:
            (dict) Dictionary with the JSON representation of response
        """

        return self.get(
            Endpoints.PAYMENT_TYPES,
            limit=limit,
            offset=offset,
            fields=fields,
            expand=expand,
            name=name,
            ledgeraccount=ledgeraccount,
            state=state
        )

    @classmethod
    def GetOne(self, payment_type_id):
        """ Get One of the payment types from bsale account

        Args:
            payment_type_id (int) : payment type identificator

        Returns:
            (dict) Dictionary with the JSON representation of response
        """

        return self.get(
            Endpoints.PAYMENT_TYPES_ID.format(payment_type_id)
        )

    @classmethod
    def Count(self):
        """ Count all the payment types on a bsale account

        Returns:
            (dict) Dictionary with the JSON representation of response
        """
        return self.get(
            Endpoints.COUNT_PAYMENT_TYPES,
        )

    @classmethod
    def GetDynamicAttributes(
        self,
        payment_type_id
    ):
        """ Get all dynamic atrributes on a payment type

        Returns:
            (dict) Dictionary with the JSON representation of response
        """

        return self.get(
            Endpoints.PAYMENT_TYPES_DINAMIC_ATTR.format(payment_type_id)
        )

    @classmethod
    def Create(
        self,
        name,
        isCash=None,
        isCheck=None,
        maxCheck=None,
        isCreditMemo=None,
        ledgerAccount=None,
        ledgerCode=None
    ):
        """ POST a new payment type on a bsale account

        Args:
            name          (str): nombre de la forma de pago
            isCash        (int): indica si la forma de pago es efectivo,
                                 No(0) o Si (1)
            isCheck       (int): indica si la forma de pago es cheque,
                                 No(0) o Si (1)
            maxCheck      (int): indica el máximo de cheques permitidos
            isCreditMemo  (int): indica si la forma de pago es un abono,
                                 No(0) o Si (1)
            ledgerAccount (str): indica la cuenta contable de la forma de pago
            ledgerCode    (str): indica el código contable de la forma de pago

        Returns:
            (dict) Dictionary with the JSON representation of response
        """

        url = Environment.URL + Endpoints.PAYMENT_TYPES
        access_token = self.itoken.getToken()

        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            'access_token': access_token
        }
        params = {
            "name": name,
            "isCash": isCash,
            "isCheck": isCheck,
            "maxCheck": maxCheck,
            "isCreditMemo": isCreditMemo,
            "ledgerAccount": ledgerAccount,
            "ledgerCode": ledgerCode

        }

        r = requests.post(url, data=json.dumps(params), headers=headers)

        return r.json()
