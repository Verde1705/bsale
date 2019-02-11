import unittest

import bsale

from httmock import HTTMock
from tests.mock import mock_api_bsale


class VariantTestCase(unittest.TestCase):

    def test_get_variants(self):
        with HTTMock(mock_api_bsale):
            self.variant = bsale.Variant()
            self.variant.Get(limit=4, offset=0)

    def test_get_one_variant(self):

        with HTTMock(mock_api_bsale):
            self.variant = bsale.Variant()
            variant = self.variant.GetOne("1")

            # check if fields exists
            self.assertIn("id", variant)
            self.assertIn("description", variant)
            self.assertIn("unlimitedStock", variant)
            self.assertIn("allowNegativeStock", variant)
            self.assertIn("state", variant)
            self.assertIn("barCode", variant)
            self.assertIn("code", variant)
            self.assertIn("imagestionCenterCost", variant)
            self.assertIn("imagestionAccount", variant)
            self.assertIn("imagestionConceptCod", variant)
            self.assertIn("imagestionProyectCod", variant)
            self.assertIn("imagestionCategoryCod", variant)
            self.assertIn("imagestionProductId", variant)
            self.assertIn("serialNumber", variant)
            self.assertIn("prestashopCombinationId", variant)
            self.assertIn("prestashopValueId", variant)
            self.assertIn("product", variant)

    def test_remove(self):

        with HTTMock(mock_api_bsale):
            self.variant = bsale.Variant()
            variant = self.variant.Remove("1")

            # check if fields exists
            self.assertIn("id", variant)
            self.assertIn("description", variant)
            self.assertIn("unlimitedStock", variant)
            self.assertIn("allowNegativeStock", variant)
            self.assertIn("state", variant)
            self.assertIn("barCode", variant)
            self.assertIn("code", variant)
            self.assertIn("imagestionCenterCost", variant)
            self.assertIn("imagestionAccount", variant)
            self.assertIn("imagestionConceptCod", variant)
            self.assertIn("imagestionProyectCod", variant)
            self.assertIn("imagestionCategoryCod", variant)
            self.assertIn("imagestionProductId", variant)
            self.assertIn("serialNumber", variant)
            self.assertIn("prestashopCombinationId", variant)
            self.assertIn("prestashopValueId", variant)
            self.assertIn("product", variant)

    def test_GetSerialStock(self):
        self.variant = bsale.Variant()

        def mock_get_serial_stock(self, variant_id, office_id):
            return {
                "id": str(variant_id),
                "count": 1,
                "items": [
                    {
                        "stockAvailable": 20,
                        "serialNumber": "serial number"
                    }
                ]
            }
        self.variant.GetSerialStock = mock_get_serial_stock

        result = self.variant.GetSerialStock(variant_id=-1, office_id=-1)
        print result
