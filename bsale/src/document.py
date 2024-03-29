#!/usr/bin/python
# -*- coding: UTF-8 -*-

from .constants import Endpoints
from .endpoint import Endpoint


class Document(Endpoint):

    @classmethod
    def Get(
        self,
        limit=25,
        offset=0,
        fields=None,
        expand=None,
        emissiondate=None,
        expirationdate=None,
        emissiondaterange=None,
        number=None,
        token=None,
        documenttypeid=None,
        clientid=None,
        clientcode=None,
        officeid=None,
        saleconditionid=None,
        informedsii=None,
        referencenumber=None,
        state=0
    ):

        # GET /v1/documents.json retorna todos los documentos.

        # Parametros

        # limit, limita la cantidad de items de una respuesta JSON,
        # si no se envía el limit es 25.
        # offset, permite paginar los items de una respuesta JSON, si no se
        # envía el offset es 0.
        # fields, solo devolver atributos específicos de un recurso
        # expand, permite expandir instancias y colecciones para traer
        # relaciones en una sola petición.
        # emissiondate, filtra documentos por la fecha de emisión.
        # expirationdate, filtra documentos por la fecha de vencimiento.
        # emissiondaterange, filtra documentos por un rango de fecha.
        # number, filtra documentos por el folio.
        # token, filtra documentos por el token.
        # documenttypeid, filtra documentos por el tipo de documento.
        # clientid, filtra documentos por el cliente.
        # clientcode, filtra rut del cliente.
        # officeid, filtra documentos por la sucursal.
        # saleconditionid, filtra documentos por la condición de venta.
        # informedsii, filtra documentos si fue declarado en el SII, 0 es
        # correcto, 1 es enviado, 2 es rechazado (Integer).
        # state, boolean (0 o 1) indica si los documentos
        # están activos(0) inactivos (1).

        # get all parameters

        return self.get(
            Endpoints.DOCUMENTS,
            limit=limit,
            offset=offset,
            fields=fields,
            expand=expand,
            emissiondate=emissiondate,
            expirationdate=expirationdate,
            emissiondaterange=emissiondaterange,
            number=number,
            token=token,
            documenttypeid=documenttypeid,
            clientid=clientid,
            clientcode=clientcode,
            officeid=officeid,
            saleconditionid=saleconditionid,
            informedsii=informedsii,
            referencenumber=referencenumber,
            state=state
        )

    @classmethod
    def GetOneDocument(self, idDocument, expand=None):
        # GET /v1/documents/421.json retorna un documento específico.
        # Parametros

        # expand, permite expandir instancias y colecciones.
        # Ejemplos

        # GET /v1/documents/421.json?expand=[document_type,office]
        return self.get(
            Endpoints.DOCUMENT_ID.format(idDocument),
            expand=expand
        )

    @classmethod
    def GetDetailDocument(self, idDocument):
        # GET /v1/documents/12644/details.json
        return self.get(Endpoints.DOCUMENT_ID_DETAILS.format(idDocument))

    @classmethod
    def GetDocumentSeller(self, idDocument):
        # GET /v1/documents/12644/details.json
        return self.get(Endpoints.DOCUMENT_ID_SELLERS.format(idDocument))

    @classmethod
    def Create(self, params):
        # Ejemplo de estructura JSON

        # {
        #   "documentTypeId": 8,
        #   "officeId": 1,
        #   "emissionDate": 1407715200,
        #   "expirationDate": 1407715200,
        #   "declareSii": 1,
        #   "priceListId": 18,
        #   "client": {
        #     "code": "1-9",
        #     "city": "Puerto Varas",
        #     "company": "Imaginex",
        #     "municipality": "comuna",
        #     "activity": "giro",
        #     "address": "direccion"
        #   },
        #   "details": [
        #     {
        #       "variantId":1,
        #       "netUnitValue": 53975,
        #       "quantity": 1,
        #       "taxId": "[1,2]",
        #       "comment": "Producto 1",
        #       "discount": 0
        #     }
        #   ],
        #   "payments": [
        #     {
        #       "paymentTypeId": 1,
        #       "amount": 70000,
        #       "recordDate": 1407715200
        #     }
        #   ],
        #   "references": [
        #       {
        #         "number": 123,
        #         "referenceDate": 1407715200,
        #         "reason": "Orden de Compra 123",
        #         "codeSii": 801
        #       }
        #   ],
        #   "dynamicAttributes": [
        #     {
        #       "description": "098",
        #       "dynamicAttributeId": 17
        #     },
        #     {
        #       "description": "nombre",
        #       "dynamicAttributeId": 18
        #     }
        #   ]
        # }

        # data = {
        #   "name": name,
        #   "description": description,
        #   "allowDecimal": allowDecimal,
        #   "ledgerAccount": ledgerAccount,
        #   "costCenter": costCenter,
        #   "stockControl": costCenter
        # }

        return self.post(Endpoints.DOCUMENTS, params)

    @classmethod
    def UpdateStateSII(self, idDocument, state):
        # PUT /v1/documents/set_sii_state.json
        # En caso de necesitar el cambio de estado que indica si
        # el documento fue declarado en el SII, se debe enviar un
        # json con la siguiente estructura:
        # informedSii, indica si el documento fue informado al SII
        # 0 es correcto, 1 es enviado, 2 es rechazado (Integer).
        # {
        #    "id": 382,
        #    "informedSii": 1
        # }

        data = {
            "id": idDocument,
            "informedSii": state
        }

        return self.put(Endpoints.DOCUMENT_SET_SII_STATE, data)

    @classmethod
    def DeleteDocument(self, idDocument, officeid):
        # DELETE /v1/documents/[idDocument].json?officeid=[office_id]

        return self.delete(
            Endpoints.DOCUMENT_ID.format(idDocument),
            officeId=officeid
        )

    @classmethod
    def CreateCreditNote(self, params):
        # example json
        # {
        #   "documentTypeId": 9,
        #   "officeId": 1,
        #   "referenceDocumentId": 11528,
        #   "expirationDate": 1407384000,
        #   "emissionDate": 1407384000,
        #   "motive": "prueba api",
        #   "declareSii": 1,
        #   "priceAdjustment": 0,
        #   "editTexts": 0,
        #   "type": 1
        # }

        return self.post(Endpoints.RETURNS, params)
