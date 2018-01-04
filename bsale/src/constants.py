#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Environment(object):

    URL = "https://api.bsale.cl/v1/"
    AccessToken = ""


class Endpoints(object):
    """structure contianing all the existing endpoints"""

    DOCUMENTS = "documents.json"
    DOCUMENT_ID = "documents/{}.json"
    DOCUMENT_ID_DETAILS = "documents/{}/details.json"

    USERS = "users.json"
    USERS_SALES_SUMMARY = "users/sales_summary.json"

    VARIANTS = "variants.json"
    VARIANT_ID = "variants/{}.json"
