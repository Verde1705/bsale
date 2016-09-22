import unittest

import bsale

from bsale import *


class VariantTestCase(unittest.TestCase):

    def test_get_variants(self):
        self.variant = bsale.Variant()
        self.variant.Get(limit=4, offset=0)
