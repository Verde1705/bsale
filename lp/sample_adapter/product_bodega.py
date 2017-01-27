#!/usr/bin/python
# -*- coding: UTF-8 -*-


from produc_adapter import ProductAdapter


class Product(object):
    """docstring for Product"""
    def __init__(self):
        super(Product, self).__init__()

    def save(self, id):
        f = open("product_bodegas", "a")
        f.write("\nproducto de bodegas : {}".format(id))
        f.close();

        produc_adapter = ProductAdapter()
        produc_adapter.onSaveProduct(1)


if __name__ == "__main__":
    produc = Product()
    produc.save(1)
