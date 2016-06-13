#!/usr/bin/python
# -*- coding: UTF-8 -*-

from lp.globals import Enviroment, enviroment

TOKEN = "8ef0ee4a6d26e2bdda847e8d57ea3a6b8e2d6de3"
if enviroment == Enviroment.PRODUCTION:
    TOKEN = "277e8fdc9c588be8e0a52308a4949b4e7ce676f6"


class Environment(object):

    URL = "https://api.bsale.cl/v1/"
    AccessToken = TOKEN
