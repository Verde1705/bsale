#!/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    from urllib import urlencode
except:
    from urllib.parse import urlencode

import requests
import json

from .constants import Environment
from .itoken import iToken


class Endpoint(object):
    """base class for bsale enpoints, should be capable of
    performing get, post, put and delete
    """

    itoken = ""

    def __init__(self, itoken=iToken()):
        if not isinstance(itoken, iToken):
            raise Exception("itoken, must be an iTokenInstance")

        self.__class__.itoken = itoken

    @classmethod
    def instance(self):
        """ check if "self" is instance, otherwise create one
        """
        if isinstance(self, Endpoint):
            return self

        # create instance of the child class
        return self(self.itoken)

    def get_arguments(self, **args):
        """ return a dictionary with all arguments cleared
        """
        arguments = dict()

        for key, value in list(args.items()):
            if value is not None:
                arguments[key] = value

        return arguments

    def generate_url(self, endpoint, arguments=None):
        """ generate url ready arguments """

        url = Environment.URL + endpoint

        if arguments is None:
            return url

        params = urlencode(sorted(arguments.items()))
        url = url + '?' + params

        return url

    def generate_headers(self):
        access_token = self.itoken.getToken()

        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            'access_token': access_token
        }

        return headers

    @classmethod
    def get(self, endpoint, **args):
        """ Perform a get to a given endpoint """

        instance = self.instance()
        arguments = instance.get_arguments(**args)
        # concatena dic en limit=10&offset=0 por ejemplo
        url = instance.generate_url(endpoint, arguments)
        headers = instance.generate_headers()

        # perform request
        r = requests.get(url, headers=headers)
        return r.json()

    @classmethod
    def post(self, endpoint, params):
        """ Perform a post to a given endpoint """
        instance = self.instance()

        url = instance.generate_url(endpoint)
        headers = instance.generate_headers()
        data = json.dumps(params)

        # perform request
        r = requests.post(url, headers=headers, data=data)
        return r.json()
