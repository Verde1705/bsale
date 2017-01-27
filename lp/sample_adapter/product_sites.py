#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Product(object):
    """docstring for Product"""
    def __init__(self):
        super(Product, self).__init__()

    def save(self, id):
        f = open("product_sites", "a")
        f.write("\nproducto de sites : {}".format(id))
        f.close()


if __name__ == "__main__":
    produc = Product()
    produc.save(1)
