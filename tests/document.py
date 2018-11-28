import unittest

import bsale

from bsale import *

from httmock import HTTMock
from tests.mock import mock_api_bsale


class DocumentTestCase(unittest.TestCase):

    def test_get_documents(self):
        with HTTMock(mock_api_bsale):
            self.document = bsale.Document()
            self.document.Get(limit=4, offset=0)

    def test_get_one_document(self):
        with HTTMock(mock_api_bsale):
            self.document = bsale.Document()

            id_document = 10829
            self.document.GetOneDocument(id_document)

    def test_get_document_sellers(self):
        with HTTMock(mock_api_bsale):
            self.document = bsale.Document()

            id_document = 10829
            seller = self.document.GetDocumentSeller(id_document)['items'][0]
            self.assertEquals(seller["id"], 2)

    def test_update_state_sii(self):
        with HTTMock(mock_api_bsale):
            self.document = bsale.Document()
            id_document = 10829
            state = 1
            document = self.document.UpdateStateSII(id_document, state)

    def test_add_nota_credito(self):
        """
        """
        with HTTMock(mock_api_bsale):
            self.document = bsale.Document()
            self.document.Create({
                "href": "https://api.bsale.cl/v1/documents/382.json",
                "id": 382,
                "emissionDate": 1463540400,
                "expirationDate": 1464663600,
                "generationDate": 1463593575,  
                "number": 1,
                "totalAmount": 14280.0,
                "netAmount": 12000.0,
                "taxAmount": 2280.0,
                "exemptAmount": 0,
                "exportTotalAmount": 0,
                "exportNetAmount": 0,
                "exportTaxAmount": 0,
                "exportExemptAmount": 0,
                "commissionRate": 0,
                "commissionNetAmount": 0,
                "commissionTaxAmount": 0,
                "commissionTotalAmount": 0,
                "percentageTaxWithheld": 0,
                "purchaseTaxAmount": 0,
                "purchaseTotalAmount": 0,
                "urlTimbre": None,
                "ted": None,
                "urlPublicView": "http://app2.bsale.cl/view/2/a2d9b4da5128?sfd=99",
                "urlPdf": "http://app2.bsale.cl/view/2/a2d9b4da5128.pdf?sfd=99",
                "urlPublicViewOriginal": "http://app2.bsale.cl/view/2/a2d9b4da5128",
                "urlPdfOriginal": "http://app2.bsale.cl/view/2/a2d9b4da5128.pdf",
                "token": "a2d9b4da5128",
                "state": 0,
                "userId": 2,
                "urlXml": None,
                "address": None,
                "municipality": None,
                "city": None,
                "informedSii": 1,
                "responseMsgSii": None,
                "document_type": {
                    "href": "https://api.bsale.cl/v1/document_types/1.json",
                    "id": "1"
                },
                "client": {
                    "href": "https://api.bsale.cl/v1/clients/7.json",
                    "id": "7"
                },
                "office": {
                    "href": "https://api.bsale.cl/v1/offices/2.json",
                    "id": "2"
                },
                "user": {
                    "href": "https://api.bsale.cl/v1/users/2.json",
                    "id": "2"
                },
                "references": {
                    "href": "https://api.bsale.cl/v1/documents/382/references.json"
                },
                "document_taxes": {
                    "href": "https://api.bsale.cl/v1/documents/382/document_taxes.json"
                },
                "details": {
                    "href": "https://api.bsale.cl/v1/documents/382/details.json"
                },
                "sellers": {
                    "href": "https://api.bsale.cl/v1/documents/382/sellers.json"
                }
            })

    def test_delete_document(self):
        with HTTMock(mock_api_bsale):
            self.document = bsale.Document()
            # print self.document.DeleteDocument(14387, 5)

    def test_credit_note(self):
        with HTTMock(mock_api_bsale):
            self.document = bsale.Document()

            detail = self.document.GetDetailDocument(14528)

            details = []
            for items in detail["items"]:
                det = {
                    "documentDetailId": items["id"],
                    "quantity": int(items["quantity"]),
                    "unitValue": (items['netAmount']/1.19)
                }
                details.append(det)

            client = {
                "code": 111111111,
                "city": "Santiago",
                "municipality": "Las Condes",
                "activity": "giro",
                "address": "Alonso de Cordova"
              }

            params = {
              "documentTypeId": 2,
              "officeId": 5,
              "referenceDocumentId": 14528,
              "expirationDate": 1474588800,
              "emissionDate": 1474588800,
              "motive": "prueba api",
              "declareSii": 1,
              "priceAdjustment": 0,
              "editTexts": 0,
              "type": 0,
              "details":details,
              "client":client
            }

            self.document.CreateCreditNote(params)
