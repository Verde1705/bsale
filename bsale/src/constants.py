#!/usr/bin/python
# -*- coding: UTF-8 -*-

from lp.globals import Enviroment, enviroment

# token usuario estefany.campos87@gmail.com
TOKEN = "8ef0ee4a6d26e2bdda847e8d57ea3a6b8e2d6de3"

if enviroment == Enviroment.PRODUCTION:
    # TOKEN = "277e8fdc9c588be8e0a52308a4949b4e7ce676f6"
    # token usuario web all@loadingplay.com
    TOKEN = "1a670eef334d56e6ecf6a3354462fc570ce19e45"


class Environment(object):

    URL = "https://api.bsale.cl/v1/"
    AccessToken = TOKEN
