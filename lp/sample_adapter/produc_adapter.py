#!/usr/bin/python
# -*- coding: UTF-8 -*-

from product_sites import Product as ProductSites
from product_bodega import Product as ProductBodegas


class ProductAdapter(object):
    def __init__(self):
        super(ProductAdapter, self).__init__()

    def onSaveProduct(self, id):
        pass

    def onProductSale(self, id):
        product = ProductBodegas()
        product.sale()
