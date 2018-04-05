#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import urllib
import inspect
from constants import Environment
from .itoken import iToken
import logging


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
    def get(self, endpoint, **args):
        """ perform a get to a given endpoint
        """

        instance = self.instance()
        arguments = instance.get_arguments(**args)

        # concatena dic en limit=10&offset=0 por ejemplo
        url = instance.generate_url(endpoint, arguments)
        headers = instance.generate_headers()

        # perform request
        r = requests.get(url, headers=headers)
        return r.json()

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
        logging.error(args)
        arguments = dict()

        for key, value in args.items():
            if value is not None:
                arguments[key] = value
        logging.error(arguments)

        return arguments

    def generate_url(self, endpoint, arguments):
        """ generate url ready arguments
        """

        params = urllib.urlencode(sorted(arguments.items()))
        url = Environment.URL + endpoint + '?' + params
        return url

    def generate_headers(self):
        access_token = self.itoken.getToken()

        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            'access_token': access_token
        }

        return headers
