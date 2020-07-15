#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Environment(object):

    URL = "https://api.bsale.cl/v1/"
    AccessToken = ""


class Endpoints(object):
    """structure contianing all the existing endpoints"""
    COUNT_PRODUCTS = "products/count.json"

    CLIENTS = "clients.json"
    CLIENT_ID = "clients/{}.json"

    DOCUMENTS = "documents.json"
    DOCUMENT_ID = "documents/{}.json"
    DOCUMENT_ID_DETAILS = "documents/{}/details.json"
    DOCUMENT_ID_SELLERS = "documents/{}/sellers.json"

    DOCUMENT_TYPES = "document_types.json"
    DOCUMENT_TYPES_ID = "document_types/{}.json"
    COUNT_DOCUMENT_TYPES = "document_types/count.json"
    DOCUMENT_TYPES_CAF = "document_types/caf.json"
    DOCUMENT_TYPES_NUMBER_AVAILBLES = "document_types/number_availables.json"

    USERS = "users.json"
    USERS_SALES_SUMMARY = "users/sales_summary.json"

    VARIANTS = "variants.json"
    COUNT_VARIANTS = "variants/count.json"
    VARIANT_ID = "variants/{}.json"

    PRICE_LISTS = "price_lists.json"
    PRICE_LISTS_ID = "price_lists/{}.json"
    PRICE_LIST_ID_DETAILS = "price_lists/{}/details.json"
    PRICE_LIST_ID_DETAILS_ID = "price_lists/{}/details/{}.json"
    COUNT_PRICE_LIST = "price_lists/count.json"

    PAYMENT_TYPES = "payment_types.json"
    PAYMENT_TYPES_ID = "payment_types/{}.json"
    COUNT_PAYMENT_TYPES = "payment_types/count.json"
    PAYMENT_TYPES_DINAMIC_ATTR = "payment_types/{}/dynamic_attributes.json"

    PAYMENTS = "payments.json"
    PAYMENTS_ID = "payments/{}.json"
    PAYMENTS_BY_PAYMENT_TYPE = "payments/group_payment_types.json"
    COUNT_PAYMENTS = "payments/count.json"

    RETURNS = "returns.json"

    OFFICES_ID = "offices/{}.json"

    COINS = "coins.json"
    COIN_ID = "coins/{}.json"
    COIN_EXCANGE_RATE = "coins/{}/exchange_rate/{}.json"
    COUNT_COIN = "coins/count.json"

    STOCK_RECEPTIONS_ID = "stocks/receptions/{}.json"
    STOCK_CONSUMPTIONS_ID = "stocks/consumptions/{}.json"
