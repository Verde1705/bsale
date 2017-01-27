#!/usr/bin/python
# -*- coding: UTF-8 -*-


import urllib
import requests
from hashlib import sha256
from hmac import HMAC
from datetime import datetime
import uuid


def signed_request(url, method="get", params={}, app_secret=""):
    """
    perform a signed request for api to api login, using private-public key pair
    params should not come with keys signature and timestamp
    """

    # asure params is empty
    try:
        del params['signature']
        del params['timestamp']
    except:
        pass

    params['timestamp'] = str(uuid.uuid4())

    concatenated = urllib.urlencode(sorted(params.items()))
    params['signature'] = HMAC(app_secret, concatenated, sha256).hexdigest()

    if method.lower() == "get":
        response = requests.get(url, data=params)
    if method.lower() == "post":
        response = requests.post(url, data=params)
    if method.lower() == "put":
        response = requests.put(url, data=params)
    if method.lower() == "delete":
        response = requests.delete(url, data=params)

    return response
