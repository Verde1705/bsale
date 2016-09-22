import unittest

import bsale

from bsale import *


class DocumentTestCase(unittest.TestCase):

    def test_get_documents(self):
        self.document = bsale.Document()
        self.document.Get(limit=4, offset=0)
        # document = self.document.Get(emissiondaterange=[1474416000, 1474585200],  documenttypeid=1, officeid=1, limit=100000000, state=0 )
        # print document

    def test_get_one_document(self):
        self.document = bsale.Document()

        id_document = 10829
        self.document.GetOneDocument(id_document)

        # print document

    # def test_create_document(self):
    #     self.document=bsale.Document()
    #     data={
    #       "documentTypeId": 1,
    #       "officeId": 31,
    #       "emissionDate": 1407715200,
    #       "expirationDate": 1407715200,
    #       "declareSii": 1,
    #       "priceListId": 18,
    #       "client": {
    #         "code": "1-9",
    #         "city": "Puerto Varas",
    #         "company": "Imaginex",
    #         "municipality": "comuna",
    #         "activity": "giro",
    #         "address": "direccion"
    #       },
    #       "details": [
    #         {

    #           "netUnitValue": 53975,
    #           "quantity": 1,
    #           "taxId":  "[1]",
    #           "comment": "Producto 1",
    #           "discount": 0
    #         }
    #       ],
    #       "payments": [
    #         {
    #           "paymentTypeId": 1,
    #           "amount": 70000,
    #           "recordDate": 1407715200
    #         }
    #       ]
    #     }
    #     document= self.document.Create(data)

    #     print document

    def test_update_state_sii(self):
        self.document = bsale.Document()
        id_document = 10829
        state = 1
        document = self.document.UpdateStateSII(id_document, state)

        print document

    def test_add_nota_credito(self):
        """
        """
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
              "urlTimbre": null,
              "ted": null,
              "urlPublicView": "http://app2.bsale.cl/view/2/a2d9b4da5128?sfd=99",
              "urlPdf": "http://app2.bsale.cl/view/2/a2d9b4da5128.pdf?sfd=99",
              "urlPublicViewOriginal": "http://app2.bsale.cl/view/2/a2d9b4da5128",
              "urlPdfOriginal": "http://app2.bsale.cl/view/2/a2d9b4da5128.pdf",
              "token": "a2d9b4da5128",
              "state": 0,
              "userId": 2,
              "urlXml": null,
              "address": null,
              "municipality": null,
              "city": null,
              "informedSii": 1,
              "responseMsgSii": null,
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
        self.document = bsale.Document()
        # print self.document.DeleteDocument(14387, 5)

    def test_credit_note(self):
        self.document = bsale.Document()

        detail = self.document.GetDetailDocument(14387)
        details = []
        for items in detail["items"]:
            det = {
                "documentDetailId": items["id"],
                "quantity": int(items["quantity"]),
                "unitValue": (items['netAmount']/1.19)
            }
            details.append(det)

        client =  {
            "code": "1-9",
            "city": "Puerto Varas",
            "municipality": "comuna",
            "activity": "giro",
            "address": "direccion"
          }

        params =  {
          "documentTypeId": 2,
          "officeId": 5,
          "referenceDocumentId": 14387,
          "expirationDate": 1474502400,
          "emissionDate": 1474502400,
          "motive": "prueba api",
          "declareSii": 1,
          "priceAdjustment": 0,
          "editTexts": 0,
          "type": 0,
          "details":details,
          "client":client
        }

        # print details

        print self.document.CreateCreditNote(params)



