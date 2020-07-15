#!/usr/bin/python
# -*- coding: UTF-8 -*-
from .constants import Endpoints
from .endpoint import Endpoint


class Payment(Endpoint):

    @classmethod
    def Get(
        self,
        limit=None,
        offset=None,
        fields=None,
        expand=None,
        recorddate=None,
        documentid=None,
        number=None,
        codesii=None,
        state=None
    ):
        """ Get all the payments types from bsale account

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
            recorddate    (list) : Permite filtrar por fecha del pago

            documentid    (list) : Permite filtrar por el id del documento.

            number        (str)  :  filtra documentos por el folio.

            codesii       (int)  : filtra documentos por el código tributario.

            state         (int)  : boolean (0 o 1) indica si las formas de
                                    pago están activas(0) inactivas(1).
        Returns:
            (dict) Dictionary with the JSON representation of response
        """

        return self.get(
            Endpoints.PAYMENTS,
            limit=limit,
            offset=offset,
            fields=fields,
            expand=expand,
            recorddate=recorddate,
            documentid=documentid,
            number=number,
            codesii=codesii,
            state=state
        )

    @classmethod
    def GetOne(self, payment_id):
        """ Get One of the payment  from bsale account

        Args:
            payment_id (int) : payment  identificator

        Returns:
            (dict) Dictionary with the JSON representation of response
        """

        return self.get(
            Endpoints.PAYMENT_TYPES_ID.format(payment_id)
        )

    @classmethod
    def GetByPaymentType(
        self,
        limit=None,
        offset=None,
        fields=None,
        expand=None,
        recorddate=None,
        documentid=None,
        number=None,
        codesii=None,
        state=None
    ):
        """ Get all the payments by types from bsale account

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
            recorddate    (list) : Permite filtrar por fecha del pago

            documentid    (list) : Permite filtrar por el id del documento.

            number        (str)  :  filtra documentos por el folio.

            codesii       (int)  : filtra documentos por el código tributario.

            state         (int)  : boolean (0 o 1) indica si las formas de
                                    pago están activas(0) inactivas(1).
        Returns:
            (dict) Dictionary with the JSON representation of response
        """

        return self.get(
            Endpoints.PAYMENTS_BY_PAYMENT_TYPE,
            limit=limit,
            offset=offset,
            fields=fields,
            expand=expand,
            recorddate=recorddate,
            documentid=documentid,
            number=number,
            codesii=codesii,
            state=state
        )

    @classmethod
    def Count(self):
        """ Count all the payment on a bsale account

        Returns:
            (dict) Dictionary with the JSON representation of response
        """
        return self.get(
            Endpoints.COUNT_PAYMENTS,
        )

    @classmethod
    def Create(
        self,
        document_id,
        payment_type_id,
        record_date=None,
        amount=None
    ):
        """ POST a new payment type on a bsale account

        Args:
            document_id     (int): identificador del documento asociado al pago
            payment_type_id (int): identificador del tipo de pago
            record_date     (int): fecha en la que se registra el pago
                                   (formato:UNIX timestamp)
            amount          (int): monto del pago

        Returns:
            (dict) Dictionary with the JSON representation of response
        """

        params = {
            "recordDate": record_date,
            "amount": amount,
            "documentId": document_id,
            "paymentTypeId": payment_type_id
        }

        return self.post(Endpoints.PAYMENTS, params)
