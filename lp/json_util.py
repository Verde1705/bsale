#!/usr/bin/python
# -*- coding: UTF-8 -*-

from json import JSONEncoder, loads as old_loads, dumps as old_dumps
from datetime import date

"""
loadingplay's json module, allow you to parse json even with dates
@sample:

from lp import json_util

json_util.loads('{}')
json_util.dumps({})
"""


class MyJSONEncoder(JSONEncoder):

    def default(self, obj):
        if isinstance(obj, date):
            return obj.isoformat()

        return JSONEncoder.default(self, obj)


def loads(json_string):
    """
    very simple implmentation of json.loads with a new enconder to catch dates
    """
    return old_loads(json_string)


def dumps(json_data):
    """
    very simple implmentation of json.loads with a new enconder to catch dates
    """
    return old_dumps(json_data, cls=MyJSONEncoder)
