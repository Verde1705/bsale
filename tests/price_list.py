#!/usr/bin/python
# -*- coding: UTF-8 -*-


import unittest

import bsale

from httmock import HTTMock
from tests.mock import mock_api_bsale


class PriceListTestCase(unittest.TestCase):

    def setUp(self):
        self.access_token = 'access_token'
        self.client = bsale.API(self.access_token)
        self.price_list_id = 1
        self.detail_id = 1
        self.price = 100

    def test_Get(self):
        with HTTMock(mock_api_bsale):
            price_list = self.client.PriceList.Get()

        self.assertEquals(price_list['count'], 1)
        self.assertEqual(price_list['items'][0]['state'], 0)
        self.assertEqual(price_list['items'][0]['name'], 'Lista Base')

    def test_GetOne(self):
        with HTTMock(mock_api_bsale):
            price_list = self.client.PriceList.GetOne(self.price_list_id)

        self.assertEqual(price_list['state'], 0)
        self.assertEqual(price_list['name'], 'Lista Base')

    def test_Count(self):
        with HTTMock(mock_api_bsale):
            price_list = self.client.PriceList.Count()
            self.assertEqual(price_list['count'], 1)

    def test_GetDetail(self):
        with HTTMock(mock_api_bsale):
            price_list = self.client.PriceList.GetDetail(
                self.price_list_id, self.detail_id)

        self.assertEquals(price_list['count'], 1)
        self.assertEqual(price_list['items'][0]['variant']['id'], '1')

    def test_GetOneDetail(self):
        with HTTMock(mock_api_bsale):
            price_list = self.client.PriceList.GetOneDetail(
                self.price_list_id, self.detail_id)

        self.assertEquals(price_list['id'], 1)
        self.assertEqual(price_list['variantValue'], 1000)

    def test_UpdateDetail(self):
        with HTTMock(mock_api_bsale):
            price_list = self.client.PriceList.UpdateDetail(
                self.price_list_id, self.detail_id, self.price)

        self.assertEquals(price_list['id'], self.detail_id)
        self.assertEquals(price_list['variantValue'], self.price)
