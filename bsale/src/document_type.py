#!/usr/bin/python
# -*- coding: UTF-8 -*-

from .constants import Endpoints
from .endpoint import Endpoint


class DocumentType(Endpoint):
    """
    Tipos de documento en Bsale

    Al realizar una petición HTTP, el servicio
    retornara un JSON con la siguiente estructura:
    {
        "href": "https://api.bsale.cl/v1/document_types/1.json",
        "id": 1,
        "name": "NOTA VENTA",
        "initialNumber": 1,
        "codeSii": "",
        "isElectronicDocument": 0,
        "breakdownTax": 1,
        "use": 0,
        "isSalesNote": 1,
        "isExempt": 0,
        "restrictsTax": 0,
        "useClient": 1,
        "messageBodyFormat": None,
        "thermalPrinter": 1,
        "state": 0,
        "copyNumber": 3,
        "isCreditNote": 0,
        "continuedHigh": 0,
        "ledgerAccount": None,
        "ipadPrint": 0,
        "ipadPrintHigh": "0"
    }

    """
    def getList(
        self,
        limit=25,
        offset=0,
        fields=None,
        expand=None,
        name=None,
        codesii=None,
        ledgeraccount=None,
        booktypeid=None,
        iselectronicdocument=None,
        issalesnote=None,
        state=0
    ):
        """ GET lista de tipos de documentos en bsale
            Args:
                limit                 (int)    : limita la cantidad de items
                                                 de una respuesta JSON, por
                                                 defecto el limit es 25,
                                                 el maximo permitido es 50.
                offset                (int)    : permite paginar los items de
                                                 una respuesta JSON, por
                                                 defecto el offset es 0.
                fields                (list)   : solicita lista atributos
                                                 de un recurso
                                                 Ex:
                                                 [codesii,ledgeraccount,state]
                expand                  (list) : permite expandir instancias
                                                 y colecciones.
                                                 Ex:
                                                 [book_type]
                name                    (str)  : Permite filtrar por nombre
                                                 del tipo de documento
                codesii                 (str)  : filtra por el codigo
                                                 tributario del tipo
                                                 de documento
                ledgeraccount           (str)  : filtra por la cuenta contable
                                                 del tipo de documento.
                booktypeid              (int)  : filtra por el tipo de libro
                                                 que pertenece
                iselectronicdocument    (int)  : permite filtrar si el tipo de
                                                 documento es electrónico
                                                 No(0) o Si(1)
                issalesnote             (str)  : permite filtrar si el tipo de
                                                 documento es una nota de
                                                 enta No(0) o Si(1)
                state                   (int)  : indica si los tipos de
                                                 documento están
                                                 activos(0) inactivos(1).
            Return:
                (dict) retorna diccionario con respuesta de la API

            Example:
            {
                "href": "https://api.bsale.cl/v1/document_types.json",
                "count": 3,
                "limit": 25,
                "offset": 0,
                "items": [
                    {
                        "href": "https://api.bsale.cl/v1/"
                                "document_types/2.json",
                        "id": 2,
                        "name": "FACTURA EXENTA O NO AFECTA ELECTRONICA",
                        "initialNumber": 1,
                        "codeSii": "34",
                        "isElectronicDocument": 1,
                        "breakdownTax": 1,
                        "use": 0,
                        "isSalesNote": 0,
                        "isExempt": 1,
                        "restrictsTax": 0,
                        "useClient": 1,
                        "messageBodyFormat": "",
                        "thermalPrinter": 1,
                        "state": 0,
                        "copyNumber": 2,
                        "isCreditNote": 0,
                        "continuedHigh": 0,
                        "ledgerAccount": None,
                        "ipadPrint": 0,
                        "ipadPrintHigh": "0",
                        "book_type": {
                            "href": "https://api.bsale.cl/v1/"
                                    "book_types/1.json",
                            "id": "1"
                    },
                    {
                        "href": "https://api.bsale.cl/v1/"
                                "document_types/3.json",
                        "id": 3,
                        "name": "NOTA CREDITO ELECTRONICA",
                        "initialNumber": 43,
                        "codeSii": "61",
                        "isElectronicDocument": 1,
                        "breakdownTax": 1,
                        "use": 1,
                        "isSalesNote": 0,
                        "isExempt": 0,
                        "restrictsTax": 0,
                        "useClient": 1,
                        "messageBodyFormat": "",
                        "thermalPrinter": 1,
                        "state": 0,
                        "copyNumber": 0,
                        "isCreditNote": 1,
                        "continuedHigh": 0,
                        "ledgerAccount": None,
                        "ipadPrint": 0,
                        "ipadPrintHigh": "0",
                        "book_type": {
                            "href": "https://api.bsale.cl/v1/"
                                    "book_types/1.json",
                            "id": "1"
                    },
                    {
                        "href": "https://api.bsale.cl/v1/"
                                "document_types/1.json",
                        "id": 1,
                        "name": "NOTA VENTA",
                        "initialNumber": 1,
                        "codeSii": "",
                        "isElectronicDocument": 0,
                        "breakdownTax": 1,
                        "use": 0,
                        "isSalesNote": 1,
                        "isExempt": 0,
                        "restrictsTax": 0,
                        "useClient": 1,
                        "messageBodyFormat": None,
                        "thermalPrinter": 1,
                        "state": 0,
                        "copyNumber": 3,
                        "isCreditNote": 0,
                        "continuedHigh": 0,
                        "ledgerAccount": None,
                        "ipadPrint": 0,
                        "ipadPrintHigh": "0"
                    }
                ]
            }

        """
        return self.get(
            Endpoints.DOCUMENT_TYPES,
            limit=limit,
            offset=offset,
            fields=fields,
            expand=expand,
            name=name,
            codesii=codesii,
            ledgeraccount=ledgeraccount,
            booktypeid=booktypeid,
            iselectronicdocument=iselectronicdocument,
            issalesnote=iselectronicdocument,
            state=state
        )

    def getOne(
        self,
        document_id,
        expand=None
    ):
        """ GET tipo de documento por id en bsale
            Args:
                document_id     (int)  : id del tipo de documento
                                         a recuperar
                expand          (list) : permite expandir instancias
                                         y colecciones.
                                         Ex:
                                         [book_type]
            Return:
                (dict) retorna diccionario con respuesta de la API
            Example:
                {
                    "href": "https://api.bsale.cl/v1/document_types/1.json",
                    "id": 1,
                    "name": "NOTA VENTA",
                    "initialNumber": 1,
                    "codeSii": "",
                    "isElectronicDocument": 0,
                    "breakdownTax": 1,
                    "use": 0,
                    "isSalesNote": 1,
                    "isExempt": 0,
                    "restrictsTax": 0,
                    "useClient": 1,
                    "messageBodyFormat": None,
                    "thermalPrinter": 1,
                    "state": 0,
                    "copyNumber": 3,
                    "isCreditNote": 0,
                    "continuedHigh": 0,
                    "ledgerAccount": None,
                    "ipadPrint": 0,
                    "ipadPrintHigh": "0"
                }
        """
        return self.get(
            Endpoints.DOCUMENT_TYPES_ID.format(document_id),
            expand=expand
        )

    def count(self, state=0):
        """
        GET cantidad de tipos de documento

        Args:
            state           (int)  : indica si los tipos de
                                     documento están
                                     activos(0) inactivos(1).
        Return:
            (dict) retorna diccionario con respuesta de la API
        Example:
            {
                "count": 3
            }
        """
        return self.get(
            Endpoints.COUNT_DOCUMENT_TYPES,
            state=state
        )

    def getCaf(self, codesii=None, documenttypeid=None):
        """
        GET caf actual de un tipo de documento

        Args:
            codesii           (str)  : filtra por el código tributario
                                       del tipo de documento.
            documenttypeid    (int)  : filtra por el identificador
                                       del tipo de documento
        Return:
            (dict) retorna diccionario con respuesta de la API
        Example:
            {
                "startDate": 1498694400,
                "expirationDate": 1546041600,
                "startNumber": 1,
                "lastNumber": 5000,
                "lastNumberUsed": 4409,
                "numbersAvailable": 591
            }
            Args:
                startDate           (int) : fecha en que inicia el caf
                expirationDate      (int) : fecha en que vence el caf
                startNumber         (int) : folio inicial del caf
                lastNumber          (int) : folio final del caf
                lastNumberUsed      (int) : ultimo folio utilizado
                                            para el tipo de documento
                numbersAvailable    (int) : folios disponibles para
                                            el tipo de documento.
        """
        return self.get(
            Endpoints.DOCUMENT_TYPES_CAF,
            codesii=codesii,
            documenttypeid=documenttypeid
        )

    def getFolios(self, codesii=None, documenttypeid=None):
        """
        Args:
            codesii           (str)  : filtra por el código tributario
                                    del tipo de documento.
            documenttypeid    (int)  : filtra por el identificador
                                    del tipo de documento
        Return:
            (dict) retorna diccionario con respuesta de la API
        Example:
            {
                "numbers_available": 2574,
                "last": 32119
            }
            Args:
            numbers_available  (int) : folios disponibles para
                                        el tipo de documento
            last               (int) : ultimo folio utilizado
                                        para el tipo de documento).
        """
        return self.get(
            Endpoints.DOCUMENT_TYPES_NUMBER_AVAILBLES,
            codesii=codesii,
            documenttypeid=documenttypeid
        )
