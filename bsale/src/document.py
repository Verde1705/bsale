#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import json
import urllib
import inspect

from constants import Environment


class Document():

    @classmethod
    def Get(self,
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
            state=0):

        # GET /v1/documents.json retorna todos los documentos.

        # Parametros

        # limit, limita la cantidad de items de una respuesta JSON, si no se envía el limit es 25.
        # offset, permite paginar los items de una respuesta JSON, si no se envía el offset es 0.
        # fields, solo devolver atributos específicos de un recurso
        # expand, permite expandir instancias y colecciones para traer relaciones en una sola petición.
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
        # informedsii, filtra documentos si fue declarado en el SII, 0 es correcto, 1 es enviado, 2 es rechazado (Integer).
        # state, boolean (0 o 1) indica si los documentos están activos(0) inactivos (1).
        
        # get all parameters
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        arguments = dict()

        for x in args:
            if x != 'self':
                if values[x] != None:
                    arguments[x] = values[x]

        #concatena dic en limit=10&offset=0 por ejemplo
        params=urllib.urlencode(sorted(arguments.items()))

        url = Environment.URL+'documents.json?'+params
        access_token=Environment.AccessToken

        headers= {'Content-type': 'application/json',
                  'Accept': 'application/json',
                  'access_token':access_token}

        r = requests.get(url, headers=headers)

        return r.json()

    @classmethod
    def GetOneDocument(self, idDocument):
        # GET /v1/documents/421.json retorna un documento específico.
        # Parametros

        # expand, permite expandir instancias y colecciones.
        # Ejemplos

        # GET /v1/documents/421.json?expand=[document_type,office]

        url = Environment.URL+'documents/'+str(idDocument)+'.json'
        access_token=Environment.AccessToken

        headers= {'Content-type': 'application/json',
                  'Accept': 'application/json',
                  'access_token':access_token}

        r = requests.get(url, headers=headers)

        return r.json()

    @classmethod
    def GetDetailDocument(self, idDocument):
        # GET /v1/documents/12644/details.json

        url = Environment.URL+'documents/'+str(idDocument)+'/details.json'
        access_token=Environment.AccessToken

        headers= {'Content-type': 'application/json',
                  'Accept': 'application/json',
                  'access_token':access_token}

        r = requests.get(url, headers=headers)

        return r.json()

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

        # print "dataaaaa   -----  {}".format(params) 

        url = Environment.URL+'documents.json'
        access_token=Environment.AccessToken

        headers= {'Content-type': 'application/json',
                  'Accept': 'application/json',
                  'access_token':access_token}

        r = requests.post(url, data=json.dumps(params), headers=headers)

        return r.json()

    @classmethod
    def UpdateStateSII(self,idDocument, state):
        # PUT /v1/documents/set_sii_state.json
        # En caso de necesitar el cambio de estado que indica si el documento fue declarado en el SII, se debe enviar un json con la siguiente estructura:
        # informedSii, indica si el documento fue informado al SII, 0 es correcto, 1 es enviado, 2 es rechazado (Integer).
        # {
        #    "id": 382,
        #    "informedSii": 1
        # }

        data = {
          "id":idDocument, 
          "informedSii":state
        }

        url = Environment.URL+'documents/set_sii_state.json'
        access_token=Environment.AccessToken

        headers= {'Content-type': 'application/json',
                  'Accept': 'application/json',
                  'access_token':access_token}

        r = requests.put(url, data=json.dumps(data), headers=headers)

        return r.json()





