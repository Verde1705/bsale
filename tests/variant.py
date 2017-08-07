import unittest

import bsale

from bsale import *

from httmock import HTTMock
from tests.mock import mock_api_bsale


class VariantTestCase(unittest.TestCase):

    def test_get_variants(self):
        with HTTMock(mock_api_bsale):
            self.variant = bsale.Variant()
            self.variant.Get(limit=4, offset=0)
