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

        id_document=716
        document=self.document.GetOneDocument(id_document)

        # print document