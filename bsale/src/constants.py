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

    PRICE_LISTS = "price_lists.json"
    PRICE_LISTS_ID = "price_lists/{}.json"
    PRICE_LIST_ID_DETAILS = "price_lists/{}/details.json"
    PRICE_LIST_ID_DETAILS_ID = "price_lists/{}/details/{}.json"
    COUNT_PRICE_LIST = "price_lists/count.json"
