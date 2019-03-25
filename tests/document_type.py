import unittest

import bsale

from bsale import *

from httmock import HTTMock
from tests.mock import mock_api_bsale


class DocumentTypeTestCase(unittest.TestCase):

    def test_getList(self):
        with HTTMock(mock_api_bsale):
            self.document_type = bsale.DocumentType()
            request = self.document_type.getList(limit=4, offset=0)
        self.assertTrue('count' in request)
        self.assertTrue('limit' in request)
        self.assertTrue('items' in request)

    def test_getOne(self):
        self.document_id = 1
        with HTTMock(mock_api_bsale):
            self.document_type = bsale.DocumentType()
            request = self.document_type.getOne(self.document_id)

        self.assertEqual(request["id"], self.document_id)
        self.assertTrue(request["name"], "NOTA VENTA")

    def test_count(self):
        with HTTMock(mock_api_bsale):
            self.document_type = bsale.DocumentType()
            request = self.document_type.count()
        self.assertTrue('count' in request)
        self.assertEqual(request["count"], 3)

    def test_getCaf(self):
        with HTTMock(mock_api_bsale):
            self.document_type = bsale.DocumentType()
            request = self.document_type.getCaf()
        self.assertTrue('startDate' in request)
        self.assertTrue('expirationDate' in request)
        self.assertTrue('startNumber' in request)
        self.assertTrue('lastNumber' in request)
        self.assertTrue('lastNumberUsed' in request)
        self.assertTrue('numbersAvailable' in request)

    def test_getFolios(self):
        with HTTMock(mock_api_bsale):
            self.document_type = bsale.DocumentType()
            request = self.document_type.getFolios()
        self.assertTrue('numbers_available' in request)
        self.assertTrue('last' in request)
