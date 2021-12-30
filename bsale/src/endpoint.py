#!/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    from urllib import urlencode
except:
    from urllib.parse import urlencode

import requests
import json

from retrying import retry

from .constants import Environment
from .itoken import iToken

stop_max_attempt_number = 3
wait_fixed = 2000


def retry_if_value_error(exception):
    """ captura Expecting value """
    return isinstance(exception, ValueError)


class Endpoint(object):
    """ base class for bsale enpoints, should be capable of
        performing get, post, put and delete
    """

    itoken = ""

    def __init__(self, itoken=iToken()):
        if not isinstance(itoken, iToken):
            raise Exception("itoken, must be an iTokenInstance")

        self.__class__.itoken = itoken

    @classmethod
    def instance(self):
        """ check if "self" is instance, otherwise create one """
        if isinstance(self, Endpoint):
            return self

        # create instance of the child class
        return self(self.itoken)

    def get_arguments(self, **args):
        """ return a dictionary with all arguments cleared """
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
    @retry(
        retry_on_exception=retry_if_value_error,
        stop_max_attempt_number=stop_max_attempt_number,
        wait_fixed=wait_fixed
    )
    def get(self, endpoint, **kargs):
        """ Perform a get to a given endpoint """

        instance = self.instance()
        arguments = instance.get_arguments(**kargs)
        # concatena dic en limit=10&offset=0 por ejemplo
        url = instance.generate_url(endpoint, arguments)
        headers = instance.generate_headers()

        # perform request
        r = requests.get(url, headers=headers)

        if r.status_code == 403:
            result = {"error": "Forbidden"}
        else:
            result = r.json()

        return result

    @classmethod
    @retry(
        retry_on_exception=retry_if_value_error,
        stop_max_attempt_number=stop_max_attempt_number,
        wait_fixed=wait_fixed
    )
    def post(self, endpoint, params):
        """ Perform a post to a given endpoint """
        instance = self.instance()

        url = instance.generate_url(endpoint)
        headers = instance.generate_headers()
        data = json.dumps(params)

        # perform request
        r = requests.post(url, headers=headers, data=data)

        if r.status_code == 403:
            result = {"error": "Forbidden"}
        else:
            result = r.json()

        return result

    @classmethod
    @retry(
        retry_on_exception=retry_if_value_error,
        stop_max_attempt_number=stop_max_attempt_number,
        wait_fixed=wait_fixed
    )
    def put(self, endpoint, params):
        """ Perform a post to a given endpoint """
        instance = self.instance()

        url = instance.generate_url(endpoint)
        headers = instance.generate_headers()
        data = json.dumps(params)

        # perform request
        r = requests.put(url, headers=headers, data=data)

        if r.status_code == 403:
            result = {"error": "Forbidden"}
        else:
            result = r.json()

        return result

    @classmethod
    @retry(
        retry_on_exception=retry_if_value_error,
        stop_max_attempt_number=stop_max_attempt_number,
        wait_fixed=wait_fixed
    )
    def delete(self, endpoint, **kargs):
        """ Perform a post to a given endpoint """
        instance = self.instance()
        arguments = instance.get_arguments(**kargs)
        # concatena dic en limit=10&offset=0 por ejemplo
        url = instance.generate_url(endpoint, arguments)
        headers = instance.generate_headers()

        # perform request
        return requests.delete(url, headers=headers)
