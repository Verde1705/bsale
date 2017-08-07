#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
from httmock import urlmatch
import logging

@urlmatch(netloc=r'(.*\.)?api.bsale.cl$')
def mock_api_bsale(url, request):
    """
    override all calls to accounts
    """

    logging.debug("url: {}".format(url.path))
    if url.path == '/v1/products.json':
        return {
            'status_code' : 200,
            'content' : {'count': 3123, 'items': [], 'limit': 0, 'offset': 0}
        }

    if url.path == '/v1/products/2334.json':
        return {
            'status_code': 200,
            'content': {'allowDecimal': 0, 'description': '', 'classification': 0, 'printDetailPack': 0, 'ledgerAccount': '', 'stockControl': 1, 'state': 1, 'href': 'https://api.bsale.cl/v1/products/2334.json', 'product_taxes': {'href': 'https://api.bsale.cl/v1/products/2334/product_taxes.json'}, 'costCenter': '', 'product_type': {'href': 'https://api.bsale.cl/v1/product_types/1.json', 'id': '1'}, 'presashopAttributeId': 0, 'prestashopProductId': 0, 'id': 2334, 'name': 'Calcetines de Mujer'}
        }

    if url.path == '/v1/stocks.json':
        return {
            'status_code': 200,
            'content': {'count': 9568, 'items': [{'office': {'href': 'https://api.bsale.cl/v1/offices/72.json', 'id': '72'}, 'variant': {'href': 'https://api.bsale.cl/v1/variants/5.json', 'id': '5'}, 'quantityReserved': 0.0, 'href': 'https://api.bsale.cl/v1/stocks/661079.json', 'quantityAvailable': 0.0, 'id': 661079, 'quantity': 0.0}], 'next': 'https://api.bsale.cl/v1/stocks.json?limit=1&offset=1', 'href': 'https://api.bsale.cl/v1/stocks.json', 'limit': 1, 'offset': 0}
        }

    if url.path == '/v1/documents/set_sii_state.json':
        return {
            'status_code': 200,
            'content': {'office': {'href': 'https://api.bsale.cl/v1/offices/31.json', 'id': '31'}, 'commissionTotalAmount': 0.0, 'municipality': 'comuna', 'number': 123124725, 'exportTaxAmount': 0.0, 'href': 'https://api.bsale.cl/v1/documents/10829.json', 'references': {'href': 'https://api.bsale.cl/v1/documents/10829/references.json'}, 'exportExemptAmount': 0.0, 'purchaseTotalAmount': 0.0, 'urlXml': None, 'netAmount': 53975.0, 'exportTotalAmount': 0.0, 'city': 'Puerto Varas', 'coin': {'href': 'https://api.bsale.cl/v1/coins/1.json', 'id': '1'}, 'urlPdf': 'http://app2.bsale.cl/view/2/512e36d08f44.pdf?sfd=99', 'urlPdfOriginal': 'http://app2.bsale.cl/view/2/512e36d08f44.pdf', 'id': 10829, 'state': 0, 'details': {'href': 'https://api.bsale.cl/v1/documents/10829/details.json'}, 'purchaseTaxAmount': 0.0, 'urlPublicView': 'http://app2.bsale.cl/view/2/512e36d08f44?sfd=99', 'percentageTaxWithheld': 0.0, 'totalAmount': 64230.0, 'exportNetAmount': 0.0, 'ted': None, 'sellers': {'href': 'https://api.bsale.cl/v1/documents/10829/sellers.json'}, 'document_taxes': {'href': 'https://api.bsale.cl/v1/documents/10829/document_taxes.json'}, 'urlTimbre': None, 'user': {'href': 'https://api.bsale.cl/v1/users/194.json', 'id': '194'}, 'address': 'direccion', 'document_type': {'href': 'https://api.bsale.cl/v1/document_types/1.json', 'id': '1'}, 'informedSii': 1, 'taxAmount': 10255.0, 'urlPublicViewOriginal': 'http://app2.bsale.cl/view/2/512e36d08f44', 'responseMsgSii': None, 'generationDate': 1462821448, 'commissionRate': 0.0, 'exemptAmount': 0.0, 'token': '512e36d08f44', 'client': {'href': 'https://api.bsale.cl/v1/clients/19.json', 'id': '19'}, 'emissionDate': 1407715200, 'commissionNetAmount': 0.0, 'commissionTaxAmount': 0.0, 'expirationDate': 1407715200}
        }

    if url.path == '/v1/documents/10829.json':
        return {
            'status_code': 200,
            'content': {'office': {'href': 'https://api.bsale.cl/v1/offices/31.json', 'id': '31'}, 'commissionTotalAmount': 0.0, 'municipality': 'comuna', 'number': 123124725, 'exportTaxAmount': 0.0, 'href': 'https://api.bsale.cl/v1/documents/10829.json', 'references': {'href': 'https://api.bsale.cl/v1/documents/10829/references.json'}, 'exportExemptAmount': 0.0, 'purchaseTotalAmount': 0.0, 'urlXml': None, 'netAmount': 53975.0, 'exportTotalAmount': 0.0, 'city': 'Puerto Varas', 'coin': {'href': 'https://api.bsale.cl/v1/coins/1.json', 'id': '1'}, 'urlPdf': 'http://app2.bsale.cl/view/2/512e36d08f44.pdf?sfd=99', 'urlPdfOriginal': 'http://app2.bsale.cl/view/2/512e36d08f44.pdf', 'id': 10829, 'state': 0, 'details': {'href': 'https://api.bsale.cl/v1/documents/10829/details.json'}, 'purchaseTaxAmount': 0.0, 'urlPublicView': 'http://app2.bsale.cl/view/2/512e36d08f44?sfd=99', 'percentageTaxWithheld': 0.0, 'totalAmount': 64230.0, 'exportNetAmount': 0.0, 'ted': None, 'sellers': {'href': 'https://api.bsale.cl/v1/documents/10829/sellers.json'}, 'document_taxes': {'href': 'https://api.bsale.cl/v1/documents/10829/document_taxes.json'}, 'urlTimbre': None, 'user': {'href': 'https://api.bsale.cl/v1/users/194.json', 'id': '194'}, 'address': 'direccion', 'document_type': {'href': 'https://api.bsale.cl/v1/document_types/1.json', 'id': '1'}, 'informedSii': 1, 'taxAmount': 10255.0, 'urlPublicViewOriginal': 'http://app2.bsale.cl/view/2/512e36d08f44', 'responseMsgSii': None, 'generationDate': 1462821448, 'commissionRate': 0.0, 'exemptAmount': 0.0, 'token': '512e36d08f44', 'client': {'href': 'https://api.bsale.cl/v1/clients/19.json', 'id': '19'}, 'emissionDate': 1407715200, 'commissionNetAmount': 0.0, 'commissionTaxAmount': 0.0, 'expirationDate': 1407715200}
        }

    if url.path == '/v1/documents.json':
        return {
            'status_code': 200,
            'content': {'count': 18385, 'items': [{'office': {'href': 'https://api.bsale.cl/v1/offices/2.json', 'id': '2'}, 'commissionTotalAmount': 0.0, 'municipality': None, 'number': 1, 'exportTaxAmount': 0.0, 'href': 'https://api.bsale.cl/v1/documents/382.json', 'references': {'href': 'https://api.bsale.cl/v1/documents/382/references.json'}, 'exportExemptAmount': 0.0, 'purchaseTotalAmount': 0.0, 'urlXml': None, 'netAmount': 12000.0, 'exportTotalAmount': 0.0, 'city': None, 'coin': {'href': 'https://api.bsale.cl/v1/coins/1.json', 'id': '1'}, 'urlPdf': 'http://app2.bsale.cl/view/2/439d299fb053.pdf?sfd=99', 'urlPdfOriginal': 'http://app2.bsale.cl/view/2/439d299fb053.pdf', 'id': 382, 'state': 0, 'details': {'href': 'https://api.bsale.cl/v1/documents/382/details.json'}, 'purchaseTaxAmount': 0.0, 'urlPublicView': 'http://app2.bsale.cl/view/2/439d299fb053?sfd=99', 'percentageTaxWithheld': 0.0, 'totalAmount': 14280.0, 'exportNetAmount': 0.0, 'ted': None, 'sellers': {'href': 'https://api.bsale.cl/v1/documents/382/sellers.json'}, 'document_taxes': {'href': 'https://api.bsale.cl/v1/documents/382/document_taxes.json'}, 'urlTimbre': '', 'user': {'href': 'https://api.bsale.cl/v1/users/2.json', 'id': '2'}, 'address': None, 'document_type': {'href': 'https://api.bsale.cl/v1/document_types/1.json', 'id': '1'}, 'informedSii': 1, 'taxAmount': 2280.0, 'urlPublicViewOriginal': 'http://app2.bsale.cl/view/2/439d299fb053', 'responseMsgSii': None, 'generationDate': '', 'commissionRate': 0.0, 'exemptAmount': 0.0, 'token': '439d299fb053', 'emissionDate': 1350604800, 'commissionNetAmount': 0.0, 'commissionTaxAmount': 0.0, 'expirationDate': 1350604800}, {'office': {'href': 'https://api.bsale.cl/v1/offices/2.json', 'id': '2'}, 'commissionTotalAmount': 0.0, 'municipality': None, 'number': 1, 'exportTaxAmount': 0.0, 'href': 'https://api.bsale.cl/v1/documents/404.json', 'references': {'href': 'https://api.bsale.cl/v1/documents/404/references.json'}, 'exportExemptAmount': 0.0, 'purchaseTotalAmount': 0.0, 'urlXml': None, 'netAmount': 0.0, 'exportTotalAmount': 0.0, 'city': None, 'coin': {'href': 'https://api.bsale.cl/v1/coins/1.json', 'id': '1'}, 'urlPdf': 'http://app2.bsale.cl/view/2/ad0496679450.pdf?sfd=99', 'urlPdfOriginal': 'http://app2.bsale.cl/view/2/ad0496679450.pdf', 'id': 404, 'state': 0, 'details': {'href': 'https://api.bsale.cl/v1/documents/404/details.json'}, 'purchaseTaxAmount': 0.0, 'urlPublicView': 'http://app2.bsale.cl/view/2/ad0496679450?sfd=99', 'percentageTaxWithheld': 0.0, 'totalAmount': 14280.0, 'exportNetAmount': 0.0, 'ted': None, 'sellers': {'href': 'https://api.bsale.cl/v1/documents/404/sellers.json'}, 'document_taxes': {'href': 'https://api.bsale.cl/v1/documents/404/document_taxes.json'}, 'urlTimbre': None, 'user': {'href': 'https://api.bsale.cl/v1/users/20.json', 'id': '20'}, 'address': None, 'document_type': {'href': 'https://api.bsale.cl/v1/document_types/3.json', 'id': '3'}, 'informedSii': 1, 'taxAmount': 0.0, 'urlPublicViewOriginal': 'http://app2.bsale.cl/view/2/ad0496679450', 'responseMsgSii': None, 'generationDate': '', 'commissionRate': 0.0, 'exemptAmount': 0.0, 'token': 'ad0496679450', 'emissionDate': 1351036800, 'commissionNetAmount': 0.0, 'commissionTaxAmount': 0.0, 'expirationDate': 1351036800}, {'office': {'href': 'https://api.bsale.cl/v1/offices/2.json', 'id': '2'}, 'commissionTotalAmount': 0.0, 'municipality': 'Santiago', 'number': 1, 'exportTaxAmount': 0.0, 'href': 'https://api.bsale.cl/v1/documents/421.json', 'references': {'href': 'https://api.bsale.cl/v1/documents/421/references.json'}, 'exportExemptAmount': 0.0, 'purchaseTotalAmount': 0.0, 'urlXml': None, 'netAmount': 4300000.0, 'exportTotalAmount': 0.0, 'city': 'Santiago', 'coin': {'href': 'https://api.bsale.cl/v1/coins/1.json', 'id': '1'}, 'urlPdf': 'http://app2.bsale.cl/view/2/f806d6a6ae73.pdf?sfd=99', 'urlPdfOriginal': 'http://app2.bsale.cl/view/2/f806d6a6ae73.pdf', 'id': 421, 'state': 0, 'details': {'href': 'https://api.bsale.cl/v1/documents/421/details.json'}, 'purchaseTaxAmount': 0.0, 'urlPublicView': 'http://app2.bsale.cl/view/2/f806d6a6ae73?sfd=99', 'percentageTaxWithheld': 0.0, 'totalAmount': 5117000.0, 'exportNetAmount': 0.0, 'ted': None, 'sellers': {'href': 'https://api.bsale.cl/v1/documents/421/sellers.json'}, 'document_taxes': {'href': 'https://api.bsale.cl/v1/documents/421/document_taxes.json'}, 'urlTimbre': None, 'user': {'href': 'https://api.bsale.cl/v1/users/2.json', 'id': '2'}, 'address': 'San Francisco 402, jj perez 7248', 'document_type': {'href': 'https://api.bsale.cl/v1/document_types/4.json', 'id': '4'}, 'informedSii': 2, 'taxAmount': 817000.0, 'urlPublicViewOriginal': 'http://app2.bsale.cl/view/2/f806d6a6ae73', 'responseMsgSii': None, 'generationDate': '', 'commissionRate': 0.0, 'exemptAmount': 0.0, 'token': 'f806d6a6ae73', 'client': {'href': 'https://api.bsale.cl/v1/clients/7.json', 'id': '7'}, 'emissionDate': 1351641600, 'commissionNetAmount': 0.0, 'commissionTaxAmount': 0.0, 'expirationDate': 1351641600}, {'office': {'href': 'https://api.bsale.cl/v1/offices/2.json', 'id': '2'}, 'commissionTotalAmount': 0.0, 'municipality': '', 'number': 1, 'exportTaxAmount': 0.0, 'href': 'https://api.bsale.cl/v1/documents/439.json', 'references': {'href': 'https://api.bsale.cl/v1/documents/439/references.json'}, 'exportExemptAmount': 0.0, 'purchaseTotalAmount': 0.0, 'urlXml': None, 'netAmount': 0.0, 'exportTotalAmount': 0.0, 'city': '', 'coin': {'href': 'https://api.bsale.cl/v1/coins/1.json', 'id': '1'}, 'urlPdf': 'http://app2.bsale.cl/view/2/814cd621b88b.pdf?sfd=99', 'urlPdfOriginal': 'http://app2.bsale.cl/view/2/814cd621b88b.pdf', 'id': 439, 'state': 0, 'details': {'href': 'https://api.bsale.cl/v1/documents/439/details.json'}, 'purchaseTaxAmount': 0.0, 'urlPublicView': 'http://app2.bsale.cl/view/2/814cd621b88b?sfd=99', 'percentageTaxWithheld': 0.0, 'totalAmount': 0.0, 'exportNetAmount': 0.0, 'ted': None, 'sellers': {'href': 'https://api.bsale.cl/v1/documents/439/sellers.json'}, 'document_taxes': {'href': 'https://api.bsale.cl/v1/documents/439/document_taxes.json'}, 'urlTimbre': None, 'user': {'href': 'https://api.bsale.cl/v1/users/2.json', 'id': '2'}, 'address': '', 'document_type': {'href': 'https://api.bsale.cl/v1/document_types/2.json', 'id': '2'}, 'informedSii': 1, 'taxAmount': 0.0, 'urlPublicViewOriginal': 'http://app2.bsale.cl/view/2/814cd621b88b', 'responseMsgSii': None, 'generationDate': '', 'commissionRate': 0.0, 'exemptAmount': 0.0, 'token': '814cd621b88b', 'client': {'href': 'https://api.bsale.cl/v1/clients/1.json', 'id': '1'}, 'emissionDate': 1351641600, 'commissionNetAmount': 0.0, 'commissionTaxAmount': 0.0, 'expirationDate': 1351641600}], 'next': 'https://api.bsale.cl/v1/documents.json?limit=4&offset=4', 'href': 'https://api.bsale.cl/v1/documents.json', 'limit': 4, 'offset': 0}
        }

    if url.path == '/v1/documents/14528/details.json':
        return {
            'status_code': 200,
            'content': {'count': 2, 'items': [{'taxAmount': 8148.0, 'totalAmount': 51030.0, 'variant': {'code': 'GDF-PV16-AZOR-C2-37', 'href': 'https://api.bsale.cl/v1/variants/17844.json', 'id': 17844, 'description': '-37'}, 'netDiscount': 0.0, 'totalDiscount': 0.0, 'href': 'https://api.bsale.cl/v1/documents/14528/details/24891.json', 'netUnitValue': 42882, 'lineNumber': 1, 'totalUnitValue': 51030, 'netAmount': 42882.0, 'id': 24891, 'quantity': 1.0}, {'taxAmount': 437.0, 'totalAmount': 2740.0, 'variant': {'code': '147466405630880', 'href': 'https://api.bsale.cl/v1/variants/26247.json', 'id': 26247, 'description': 'Despacho'}, 'netDiscount': 0.0, 'totalDiscount': 0.0, 'href': 'https://api.bsale.cl/v1/documents/14528/details/24892.json', 'netUnitValue': 2303, 'lineNumber': 2, 'totalUnitValue': 2740, 'netAmount': 2303.0, 'id': 24892, 'quantity': 1.0}], 'href': 'https://api.bsale.cl/v1/documents/14528/details.json', 'limit': 25, 'offset': 0}
        }

    if url.path == '/v1/returns.json':
        return {
            'status_code': 200,
            'content': {'error': 'The client has no name'}
        }

    logging.debug("no tiene")
    return {
        'status_code': 500,
        'content': {
            { 'message': 'mock not found' }
        }
    }
