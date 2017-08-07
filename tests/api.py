#!/usr/bin/python
# -*- coding: UTF-8 -*-


import bsale
import unittest
from httmock import urlmatch
from httmock import HTTMock


@urlmatch(netloc=r'(.*\.)?api.bsale.cl$')
def mock_url_document(url, request):

    assert request.method == 'POST'
    assert request.headers["access_token"] == 'foo'


class APITestCase(unittest.TestCase):

    def test_init_api(self):
        """ init API """

        with HTTMock(mock_url_document):
            client = bsale.API(token="foo")

            # https://github.com/gmontero/API-Bsale/wiki/Documentos#post-un-documento
            client.Document.Create({
                "documentTypeId": 8,
                "officeId": 1,
                "priceListId": 18,
                "emissionDate": 1407715200,
                "expirationDate": 1407715200,
                "declareSii": 1
            })
