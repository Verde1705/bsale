import unittest

import bsale

from bsale import *

class DocumentTestCase(unittest.TestCase):

    def test_get_documents(self):
        self.document = bsale.Document()
        document = self.document.Get(limit=4, offset=0)

        # print document

    def test_get_one_document(self):
        self.document=bsale.Document()

        id_document=10829
        document=self.document.GetOneDocument(id_document)

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
        id_document=10829
        state=1
        document = self.document.UpdateStateSII(id_document, state)

        print document