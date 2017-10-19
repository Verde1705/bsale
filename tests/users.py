#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import bsale

from httmock import HTTMock
from tests.mock import mock_api_bsale


class UsersTestCase(unittest.TestCase):

    def test_get_users(self):
        with HTTMock(mock_api_bsale):
            b = bsale.API("ACCESS_TOKEN")
            users = b.Users.Get()

            # check if httmock is responding
            self.assertEqual(users["count"], 121)
            self.assertEqual(users["limit"], 2)

    def test_get_sales_summary(self):
        with HTTMock(mock_api_bsale):
            b = bsale.API("ACCESS_TOKEN")
            sales_summary = b.Users.GetSalesSummary(1)  # user id

            # check if httmock is responding
            self.assertEqual(sales_summary["startDate"], 1438560000)
            self.assertEqual(sales_summary["endDate"], 1438560000)
