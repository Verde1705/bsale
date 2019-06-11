#!/usr/bin/python
# -*- coding: UTF-8 -*-


import unittest

import bsale

from httmock import HTTMock
from bsale.mocks import mock_api_bsale

class OfficesTestCase(unittest.TestCase):

    def setUp(self):
        self.access_token = 'access_token'
        self.client = bsale.API(self.access_token)
        self.office_id = 1

    def test_getOne(self):
        with HTTMock(mock_api_bsale):
            result = self.client.Offices.getOne(self.office_id)

            self.assertEqual(
                "Fabrica Web",
                result["name"]
            )
            self.assertEqual(
                1,
                result["id"]
            )
