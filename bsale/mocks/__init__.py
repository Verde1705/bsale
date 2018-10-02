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
            'status_code': 200,
            'content': {
                'count': 3123,
                'items': [],
                'limit': 0,
                'offset': 0
            }
        }

    if url.path == '/v1/products/2334.json':
        return {
            'status_code': 200,
            'content': {
                'allowDecimal': 0,
                'description': '',
                'classification': 0,
                'printDetailPack': 0,
                'ledgerAccount': '',
                'stockControl': 1,
                'state': 1,
                'href': 'https://api.bsale.cl/v1/products/2334.json',
                'product_taxes': {
                    'href': "https://api.bsale.cl/v1/products"
                            "/2334/product_taxes.json"
                    },
                'costCenter': '',
                'product_type': {
                    'href': 'https://api.bsale.cl/v1/product_types/1.json',
                    'id': '1'
                    },
                'presashopAttributeId': 0,
                'prestashopProductId': 0,
                'id': 2334,
                'name':
                'Calcetines de Mujer'
            }
        }

    if url.path == '/v1/stocks.json':
        return {
            'status_code': 200,
            'content': {
                'count': 9568,
                'items': [{
                    'office': {
                        'href': 'https://api.bsale.cl/v1/offices/72.json',
                        'id': '72'
                    },
                    'variant': {
                        'href': 'https://api.bsale.cl/v1/variants/5.json',
                        'id': '5'
                    },
                    'quantityReserved': 0.0,
                    'href': 'https://api.bsale.cl/v1/stocks/661079.json',
                    'quantityAvailable': 0.0,
                    'id': 661079,
                    'quantity': 0.0
                }],
                'next': 'https://api.bsale.cl/v1/stocks.json?limit=1&offset=1',
                'href': 'https://api.bsale.cl/v1/stocks.json',
                'limit': 1,
                'offset': 0
            }
        }

    if url.path == '/v1/documents/set_sii_state.json':
        return {
            'status_code': 200,
            'content': {
                'office': {
                    'href': 'https://api.bsale.cl/v1/offices/31.json',
                    'id': '31'
                },
                'commissionTotalAmount': 0.0,
                'municipality': 'comuna',
                'number': 123124725,
                'exportTaxAmount': 0.0,
                'href': 'https://api.bsale.cl/v1/documents/10829.json',
                'references': {
                    'href': "https://api.bsale.cl/v1/"
                            "documents/10829/references.json"
                },
                'exportExemptAmount': 0.0,
                'purchaseTotalAmount': 0.0,
                'urlXml': None,
                'netAmount': 53975.0,
                'exportTotalAmount': 0.0,
                'city': 'Puerto Varas',
                'coin': {
                    'href': 'https://api.bsale.cl/v1/coins/1.json',
                    'id': '1'
                },
                'urlPdf': "http://app2.bsale.cl/view"
                          "/2/512e36d08f44.pdf?sfd=99",
                'urlPdfOriginal': "http://app2.bsale.cl/view/"
                                  "2/512e36d08f44.pdf",
                'id': 10829,
                'state': 0,
                'details': {
                    'href': "https://api.bsale.cl/v1/"
                            "documents/10829/details.json"
                },
                'purchaseTaxAmount': 0.0,
                'urlPublicView': "http://app2.bsale.cl/view/"
                                 "2/512e36d08f44?sfd=99",
                'percentageTaxWithheld': 0.0,
                'totalAmount': 64230.0,
                'exportNetAmount': 0.0,
                'ted': None,
                'sellers': {
                    'href': "https://api.bsale.cl/v1/documents/"
                            "10829/sellers.json"
                },
                'document_taxes': {
                    'href': "https://api.bsale.cl/v1/documents/"
                            "10829/document_taxes.json"
                },
                'urlTimbre': None,
                'user': {
                    'href': 'https://api.bsale.cl/v1/users/194.json',
                    'id': '194'
                },
                'address': 'direccion',
                'document_type': {
                    'href': 'https://api.bsale.cl/v1/document_types/1.json',
                    'id': '1'
                },
                'informedSii': 1,
                'taxAmount': 10255.0,
                'urlPublicViewOriginal': "http://app2.bsale.cl/view/"
                                         "2/512e36d08f44",
                'responseMsgSii': None,
                'generationDate': 1462821448,
                'commissionRate': 0.0,
                'exemptAmount': 0.0,
                'token': '512e36d08f44',
                'client': {
                    'href': 'https://api.bsale.cl/v1/clients/19.json',
                    'id': '19'
                },
                'emissionDate': 1407715200,
                'commissionNetAmount': 0.0,
                'commissionTaxAmount': 0.0,
                'expirationDate': 1407715200
            }
        }

    if url.path == '/v1/documents/10829.json':
        return {
            'status_code': 200,
            'content': {
                    'office': {
                        'href': 'https://api.bsale.cl/v1/offices/31.json',
                        'id': '31'
                    },
                    'commissionTotalAmount': 0.0,
                    'municipality': 'comuna',
                    'number': 123124725,
                    'exportTaxAmount': 0.0,
                    'href': 'https://api.bsale.cl/v1/documents/10829.json',
                    'references': {
                        'href': "https://api.bsale.cl/v1/documents/"
                                "10829/references.json"
                    },
                    'exportExemptAmount': 0.0,
                    'purchaseTotalAmount': 0.0,
                    'urlXml': None,
                    'netAmount': 53975.0,
                    'exportTotalAmount': 0.0,
                    'city': 'Puerto Varas',
                    'coin': {
                        'href': 'https://api.bsale.cl/v1/coins/1.json',
                        'id': '1'
                    },
                    'urlPdf': "http://app2.bsale.cl/view/"
                              "2/512e36d08f44.pdf?sfd=99",
                    'urlPdfOriginal': "http://app2.bsale.cl/view/"
                                      "2/512e36d08f44.pdf",
                    'id': 10829,
                    'state': 0,
                    'details': {
                        'href': "https://api.bsale.cl/v1/documents/"
                                "10829/details.json"
                    },
                    'purchaseTaxAmount': 0.0,
                    'urlPublicView': "http://app2.bsale.cl/view/"
                                     "2/512e36d08f44?sfd=99",
                    'percentageTaxWithheld': 0.0,
                    'totalAmount': 64230.0,
                    'exportNetAmount': 0.0,
                    'ted': None,
                    'sellers': {
                        'href': "https://api.bsale.cl/v1/documents/"
                                "10829/sellers.json"
                    },
                    'document_taxes': {
                        'href': "https://api.bsale.cl/v1/documents/"
                                "10829/document_taxes.json"
                    },
                    'urlTimbre': None,
                    'user': {
                        'href': "https://api.bsale.cl/v1/users/194.json",
                        'id': '194'
                    },
                    'address': 'direccion',
                    'document_type': {
                        'href': "https://api.bsale.cl/v1/"
                                "document_types/1.json",
                        'id': '1'
                    },
                    'informedSii': 1,
                    'taxAmount': 10255.0,
                    'urlPublicViewOriginal': "http://app2.bsale.cl/view/"
                                             "2/512e36d08f44",
                    'responseMsgSii': None,
                    'generationDate': 1462821448,
                    'commissionRate': 0.0,
                    'exemptAmount': 0.0,
                    'token': '512e36d08f44',
                    'client': {
                        'href': "https://api.bsale.cl/v1/clients/19.json",
                        'id': '19'
                    },
                    'emissionDate': 1407715200,
                    'commissionNetAmount': 0.0,
                    'commissionTaxAmount': 0.0,
                    'expirationDate': 1407715200
                }
        }

    if url.path == '/v1/documents.json':
        return {
            'status_code': 200,
            'content': {
                'count': 18385,
                'items': [{
                    'office': {
                        'href': 'https://api.bsale.cl/v1/offices/2.json',
                        'id': '2'
                    },
                    'commissionTotalAmount': 0.0,
                    'municipality': None,
                    'number': 1,
                    'exportTaxAmount': 0.0,
                    'href': 'https://api.bsale.cl/v1/documents/382.json',
                    'references': {
                        'href': "https://api.bsale.cl/v1/documents/"
                                "382/references.json"
                    },
                    'exportExemptAmount': 0.0,
                    'purchaseTotalAmount': 0.0,
                    'urlXml': None,
                    'netAmount': 12000.0,
                    'exportTotalAmount': 0.0,
                    'city': None,
                    'coin': {
                        'href': 'https://api.bsale.cl/v1/coins/1.json',
                        'id': '1'
                    },
                    'urlPdf': 'http://app2.bsale.cl/view/'
                              '2/439d299fb053.pdf?sfd=99',
                    'urlPdfOriginal': 'http://app2.bsale.cl/view/'
                                      '2/439d299fb053.pdf',
                    'id': 382,
                    'state': 0,
                    'details': {
                        'href': 'https://api.bsale.cl/v1/documents/'
                                '382/details.json'
                    },
                    'purchaseTaxAmount': 0.0,
                    'urlPublicView': 'http://app2.bsale.cl/view/'
                                     '2/439d299fb053?sfd=99',
                    'percentageTaxWithheld': 0.0,
                    'totalAmount': 14280.0,
                    'exportNetAmount': 0.0,
                    'ted': None,
                    'sellers': {
                        'href': 'https://api.bsale.cl/v1/documents/'
                                '382/sellers.json'
                    },
                    'document_taxes': {
                        'href': 'https://api.bsale.cl/v1/documents/'
                                '382/document_taxes.json'
                    },
                    'urlTimbre': '',
                    'user': {
                        'href': 'https://api.bsale.cl/v1/users/2.json',
                        'id': '2'
                    },
                    'address': None,
                    'document_type': {
                        'href': 'https://api.bsale.cl/v1/'
                                'document_types/1.json',
                        'id': '1'
                    },
                    'informedSii': 1,
                    'taxAmount': 2280.0,
                    'urlPublicViewOriginal': 'http://app2.bsale.cl/view/'
                                             '2/439d299fb053',
                    'responseMsgSii': None,
                    'generationDate': '',
                    'commissionRate': 0.0,
                    'exemptAmount': 0.0,
                    'token': '439d299fb053',
                    'emissionDate': 1350604800,
                    'commissionNetAmount': 0.0,
                    'commissionTaxAmount': 0.0,
                    'expirationDate': 1350604800
                }, {
                    'office': {
                        'href': 'https://api.bsale.cl/v1/offices/2.json',
                        'id': '2'
                    },
                    'commissionTotalAmount': 0.0,
                    'municipality': None,
                    'number': 1,
                    'exportTaxAmount': 0.0,
                    'href': 'https://api.bsale.cl/v1/documents/404.json',
                    'references': {
                        'href': 'https://api.bsale.cl/v1/documents/'
                                '404/references.json'
                    },
                    'exportExemptAmount': 0.0,
                    'purchaseTotalAmount': 0.0,
                    'urlXml': None,
                    'netAmount': 0.0,
                    'exportTotalAmount': 0.0,
                    'city': None,
                    'coin': {
                        'href': 'https://api.bsale.cl/v1/coins/1.json',
                        'id': '1'
                    },
                    'urlPdf': 'http://app2.bsale.cl/view/'
                              '2/ad0496679450.pdf?sfd=99',
                    'urlPdfOriginal': 'http://app2.bsale.cl/view/'
                                      '2/ad0496679450.pdf',
                    'id': 404,
                    'state': 0,
                    'details': {
                        'href': 'https://api.bsale.cl/v1/documents/'
                                '404/details.json'
                    },
                    'purchaseTaxAmount': 0.0,
                    'urlPublicView': 'http://app2.bsale.cl/view/'
                                     '2/ad0496679450?sfd=99',
                    'percentageTaxWithheld': 0.0,
                    'totalAmount': 14280.0,
                    'exportNetAmount': 0.0,
                    'ted': None,
                    'sellers': {
                        'href': 'https://api.bsale.cl/v1/documents/'
                                '404/sellers.json'
                    },
                    'document_taxes': {
                        'href': 'https://api.bsale.cl/v1/documents/'
                                '404/document_taxes.json'
                    },
                    'urlTimbre': None,
                    'user': {
                        'href': 'https://api.bsale.cl/v1/users/20.json',
                        'id': '20'
                    },
                    'address': None,
                    'document_type': {
                        'href': 'https://api.bsale.cl/v1/'
                                'document_types/3.json',
                        'id': '3'
                    },
                    'informedSii': 1,
                    'taxAmount': 0.0,
                    'urlPublicViewOriginal': 'http://app2.bsale.cl/view/'
                                             '2/ad0496679450',
                    'responseMsgSii': None,
                    'generationDate': '',
                    'commissionRate': 0.0,
                    'exemptAmount': 0.0,
                    'token': 'ad0496679450',
                    'emissionDate': 1351036800,
                    'commissionNetAmount': 0.0,
                    'commissionTaxAmount': 0.0,
                    'expirationDate': 1351036800
                }, {
                    'office': {
                        'href': 'https://api.bsale.cl/v1/offices/2.json',
                        'id': '2'
                    },
                    'commissionTotalAmount': 0.0,
                    'municipality': 'Santiago',
                    'number': 1,
                    'exportTaxAmount': 0.0,
                    'href': 'https://api.bsale.cl/v1/documents/421.json',
                    'references': {
                        'href': 'https://api.bsale.cl/v1/documents/'
                                '421/references.json'
                    },
                    'exportExemptAmount': 0.0,
                    'purchaseTotalAmount': 0.0,
                    'urlXml': None,
                    'netAmount': 4300000.0,
                    'exportTotalAmount': 0.0,
                    'city': 'Santiago',
                    'coin': {
                        'href': 'https://api.bsale.cl/v1/coins/1.json',
                        'id': '1'
                    },
                    'urlPdf': 'http://app2.bsale.cl/view/'
                              '2/f806d6a6ae73.pdf?sfd=99',
                    'urlPdfOriginal': 'http://app2.bsale.cl/view/'
                                      '2/f806d6a6ae73.pdf',
                    'id': 421,
                    'state': 0,
                    'details': {
                        'href': 'https://api.bsale.cl/v1/documents/'
                                '421/details.json'
                    },
                    'purchaseTaxAmount': 0.0,
                    'urlPublicView': 'http://app2.bsale.cl/view/'
                                     '2/f806d6a6ae73?sfd=99',
                    'percentageTaxWithheld': 0.0,
                    'totalAmount': 5117000.0,
                    'exportNetAmount': 0.0,
                    'ted': None,
                    'sellers': {
                        'href': 'https://api.bsale.cl/v1/documents/'
                                '421/sellers.json'
                    },
                    'document_taxes': {
                        'href': 'https://api.bsale.cl/v1/documents/'
                                '421/document_taxes.json'
                    },
                    'urlTimbre': None,
                    'user': {
                        'href': 'https://api.bsale.cl/v1/users/2.json',
                        'id': '2'
                    },
                    'address': 'San Francisco 402, jj perez 7248',
                    'document_type': {
                        'href': 'https://api.bsale.cl/v1/'
                                'document_types/4.json',
                        'id': '4'
                    },
                    'informedSii': 2,
                    'taxAmount': 817000.0,
                    'urlPublicViewOriginal': 'http://app2.bsale.cl/view/'
                                             '2/f806d6a6ae73',
                    'responseMsgSii': None,
                    'generationDate': '',
                    'commissionRate': 0.0,
                    'exemptAmount': 0.0,
                    'token': 'f806d6a6ae73',
                    'client': {
                        'href': 'https://api.bsale.cl/v1/clients/7.json',
                        'id': '7'
                    },
                    'emissionDate': 1351641600,
                    'commissionNetAmount': 0.0,
                    'commissionTaxAmount': 0.0,
                    'expirationDate': 1351641600
                }, {
                    'office': {
                        'href': 'https://api.bsale.cl/v1/offices/2.json',
                        'id': '2'
                    },
                    'commissionTotalAmount': 0.0,
                    'municipality': '',
                    'number': 1,
                    'exportTaxAmount': 0.0,
                    'href': 'https://api.bsale.cl/v1/documents/439.json',
                    'references': {
                        'href': 'https://api.bsale.cl/v1/documents/'
                                '439/references.json'
                    },
                    'exportExemptAmount': 0.0,
                    'purchaseTotalAmount': 0.0,
                    'urlXml': None,
                    'netAmount': 0.0,
                    'exportTotalAmount': 0.0,
                    'city': '',
                    'coin': {
                        'href': 'https://api.bsale.cl/v1/coins/1.json',
                        'id': '1'
                    },
                    'urlPdf': 'http://app2.bsale.cl/view/'
                              '2/814cd621b88b.pdf?sfd=99',
                    'urlPdfOriginal': 'http://app2.bsale.cl/view/'
                                      '2/814cd621b88b.pdf',
                    'id': 439,
                    'state': 0,
                    'details': {
                        'href': 'https://api.bsale.cl/v1/documents/'
                                '439/details.json'
                    },
                    'purchaseTaxAmount': 0.0,
                    'urlPublicView': 'http://app2.bsale.cl/view/'
                                     '2/814cd621b88b?sfd=99',
                    'percentageTaxWithheld': 0.0,
                    'totalAmount': 0.0,
                    'exportNetAmount': 0.0,
                    'ted': None,
                    'sellers': {
                        'href': 'https://api.bsale.cl/v1/documents/'
                                '439/sellers.json'
                    },
                    'document_taxes': {
                        'href': 'https://api.bsale.cl/v1/documents/'
                                '439/document_taxes.json'
                    },
                    'urlTimbre': None,
                    'user': {
                        'href': 'https://api.bsale.cl/v1/users/2.json',
                        'id': '2'
                    },
                    'address': '',
                    'document_type': {
                        'href': 'https://api.bsale.cl/v1/'
                                'document_types/2.json',
                        'id': '2'
                    },
                    'informedSii': 1,
                    'taxAmount': 0.0,
                    'urlPublicViewOriginal': 'http://app2.bsale.cl/view/'
                                             '2/814cd621b88b',
                    'responseMsgSii': None,
                    'generationDate': '',
                    'commissionRate': 0.0,
                    'exemptAmount': 0.0,
                    'token': '814cd621b88b',
                    'client': {
                        'href': 'https://api.bsale.cl/v1/clients/1.json',
                        'id': '1'
                    },
                    'emissionDate': 1351641600,
                    'commissionNetAmount': 0.0,
                    'commissionTaxAmount': 0.0,
                    'expirationDate': 1351641600
                }],
                'next': 'https://api.bsale.cl/v1/'
                        'documents.json?limit=4&offset=4',
                'href': 'https://api.bsale.cl/v1/documents.json',
                'limit': 4,
                'offset': 0
            }
        }

    if url.path == '/v1/documents/14528/details.json':
        return {
            'status_code': 200,
            'content': {
                'count': 2,
                'items': [{
                    'taxAmount': 8148.0,
                    'totalAmount': 51030.0,
                    'variant': {
                        'code': 'GDF-PV16-AZOR-C2-37',
                        'href': 'https://api.bsale.cl/v1/variants/17844.json',
                        'id': 17844,
                        'description': '-37'
                    },
                    'netDiscount': 0.0,
                    'totalDiscount': 0.0,
                    'href': 'https://api.bsale.cl/v1/documents/'
                            '14528/details/24891.json',
                    'netUnitValue': 42882,
                    'lineNumber': 1,
                    'totalUnitValue': 51030,
                    'netAmount': 42882.0,
                    'id': 24891,
                    'quantity': 1.0
                }, {
                    'taxAmount': 437.0,
                    'totalAmount': 2740.0,
                    'variant': {
                        'code': '147466405630880',
                        'href': 'https://api.bsale.cl/v1/variants/26247.json',
                        'id': 26247,
                        'description': 'Despacho'
                    },
                    'netDiscount': 0.0,
                    'totalDiscount': 0.0,
                    'href': 'https://api.bsale.cl/v1/documents/'
                            '14528/details/24892.json',
                    'netUnitValue': 2303,
                    'lineNumber': 2,
                    'totalUnitValue': 2740,
                    'netAmount': 2303.0,
                    'id': 24892,
                    'quantity': 1.0
                }],
                'href': 'https://api.bsale.cl/v1/documents/14528/details.json',
                'limit': 25,
                'offset': 0
            }
        }

    if url.path == '/v1/returns.json':
        return {
            'status_code': 200,
            'content': {'error': 'The client has no name'}
        }

    if "/v1/users.json" in url.path:
        return {
            'status_code': 200,
            'content':
            {
                "href": "http://localhost:9292/v1/users.json",
                "count": 121,
                "limit": 2,
                "offset": 0,
                "items": [{
                    "href": "http://localhost:9292/v1/users/32.json",
                    "id": 32,
                    "firstName": "Alejandro",
                    "lastName": "Herrera",
                    "email": "ah@gmail.com",
                    "state": 0,
                    "office": {
                        "href": "http://localhost:9292/v1/offices/2.json",
                        "id": "2"
                    }
                }, {
                    "href": "http://localhost:9292/v1/users/88.json",
                    "id": 88,
                    "firstName": "Andrés",
                    "lastName": "Oyarzo",
                    "email": "aoyarzo@gmail.com",
                    "state": 1,
                    "office": {
                        "href": "http://localhost:9292/v1/offices/2.json",
                        "id": "2"
                    }
                }
                ],
                "next": "http://localhost:9292/v1/users.json?limit=2&offset=2"
            }
        }

    if "/v1/users/sales_summary.json" in url.path:
        return {
            'status_code': 500,
            'content': {
                "startDate": 1438560000,
                "endDate": 1438560000,
                "total": 22882060,
                "sellers": [{
                    "href": "https://api.bsale.cl/v1/users/113.json",
                    "id": 113,
                    "fullName": "Daniela Valdes",
                    "subtotal": 255000,
                    "taxSubtotal": 40714,
                    "sales": {
                            "href": 'https://api.bsale.cl/v1/users/'
                                    '113/sales.json?'
                                    'startdate=1438560000&enddate=1438560000'
                    },
                    "returns": {
                        "href": "https://api.bsale.cl/v1/users/"
                                "113/returns.json?"
                                "startdate=1438560000&enddate=1438560000"
                    }
                },
                    {
                        "href": "https://api.bsale.cl/v1/users/114.json",
                        "id": 114,
                        "fullName": "Lara  Galan",
                        "subtotal": 255000,
                        "taxSubtotal": 40714,
                        "sales": {
                            "href": "https://api.bsale.cl/v1/users/"
                                    "114/sales.json?"
                                    "startdate=1438560000&enddate=1438560000"
                        },
                        "returns": {
                            "href": "https://api.bsale.cl/v1/users/"
                                    "114/returns.json?"
                                    "startdate=1438560000&enddate=1438560000"
                        }
                },
                    {
                        "href": "https://api.bsale.cl/v1/users/128.json",
                        "id": 128,
                        "fullName": "Luis Guzman",
                        "subtotal": 60,
                        "taxSubtotal": 9,
                        "sales": {
                            "href": "https://api.bsale.cl/v1/users/"
                                    "128/sales.json?"
                                    "startdate=1438560000&enddate=1438560000"
                        },
                        "returns": {
                            "href": "https://api.bsale.cl/v1/users/"
                                    "128/returns.json?"
                                    "startdate=1438560000&enddate=1438560000"
                        }
                },
                    {
                        "href": "https://api.bsale.cl/v1/users/105.json",
                        "id": 105,
                        "fullName": "Maximo Mancilla",
                        "subtotal": 22372000,
                        "taxSubtotal": 3572000,
                        "sales": {
                            "href": "https://api.bsale.cl/v1/users/"
                                    "105/sales.json"
                                    "?startdate=1438560000&enddate=1438560000"
                        },
                        "returns": {
                            "href": "https://api.bsale.cl/v1/users/"
                                    "105/returns.json?"
                                    "startdate=1438560000&enddate=1438560000"
                        }
                }
                ]
            }
        }

    if "/v1/variants.json" in url.path:
        return {
            "status_code": 200,
            "content": {
                "href": "https://api.bsale.cl/v1/variants.json",
                "count": 868,
                "limit": 3,
                "offset": 0,
                "items": [{
                        "href": "https://api.bsale.cl/v1/variants/1548.json",
                        "id": 1548,
                        "description": "120 ML",
                        "unlimitedStock": 0,
                        "allowNegativeStock": 0,
                        "state": 0,
                        "barCode": "1401291513",
                        "code": "1401291513",
                        "imagestionCenterCost": 0,
                        "imagestionAccount": 0,
                        "imagestionConceptCod": 0,
                        "imagestionProyectCod": 0,
                        "imagestionCategoryCod": 0,
                        "imagestionProductId": 0,
                        "serialNumber": 0,
                        "prestashopCombinationId": 0,
                        "prestashopValueId": 0,
                        "product": {
                            "href": "https://api.bsale.cl/v1/"
                                    "products/416.json",
                            "id": "416"
                        },
                        "attribute_values": {
                            "href": "https://api.bsale.cl/v1/variants/"
                                    "1548/attribute_values.json"
                        },
                        "costs": {
                                "href": "https://api.bsale.cl/v1/variants/"
                                        "1548/costs.json"
                        }
                    },
                    {
                        "href": "https://api.bsale.cl/v1/variants/1555.json",
                        "id": 1555,
                        "description": "150 ML",
                        "unlimitedStock": 0,
                        "allowNegativeStock": 0,
                        "state": 0,
                        "barCode": "1400786476",
                        "code": "1400786476",
                        "imagestionCenterCost": 0,
                        "imagestionAccount": 0,
                        "imagestionConceptCod": 0,
                        "imagestionProyectCod": 0,
                        "imagestionCategoryCod": 0,
                        "imagestionProductId": 0,
                        "serialNumber": 0,
                        "prestashopCombinationId": 0,
                        "prestashopValueId": 0,
                        "product": {
                            "href": "https://api.bsale.cl/v1/"
                                    "products/420.json",
                            "id": "420"
                        },
                        "attribute_values": {
                            "href": "https://api.bsale.cl/v1/variants/"
                                    "1555/attribute_values.json"
                        },
                        "costs": {
                            "href": "https://api.bsale.cl/v1/variants/"
                                    "1555/costs.json"
                        }
                    },
                    {
                        "href": "https://api.bsale.cl/v1/variants/2101.json",
                        "id": 2101,
                        "description": "300 ML",
                        "unlimitedStock": 0,
                        "allowNegativeStock": 0,
                        "state": 0,
                        "barCode": "1423687401",
                        "code": "1423687401",
                        "imagestionCenterCost": 0,
                        "imagestionAccount": 0,
                        "imagestionConceptCod": 0,
                        "imagestionProyectCod": 0,
                        "imagestionCategoryCod": 0,
                        "imagestionProductId": 0,
                        "serialNumber": 0,
                        "prestashopCombinationId": 0,
                        "prestashopValueId": 0,
                        "product": {
                            "href": "https://api.bsale.cl/v1/products/"
                                    "588.json",
                            "id": "588"
                        },
                        "attribute_values": {
                            "href": "https://api.bsale.cl/v1/variants/"
                                    "2101/attribute_values.json"
                        },
                        "costs": {
                            "href": "https://api.bsale.cl/v1/variants/"
                                    "2101/costs.json"
                        }
                }
                ],
                "next": "https://api.bsale.cl/v1/"
                        "variants.json?limit=3&offset=3"
            }
        }

    if "/v1/variants/1.json" in url.path:
        return {
            "status_code": 200,
            "content": {
                "href": "https://api.bsale.cl/v1/variants/2373.json",
                "id": 2373,
                "description": "240 ML",
                "unlimitedStock": 0,
                "allowNegativeStock": 0,
                "state": 0,
                "barCode": "1441310864",
                "code": "1441310864",
                "imagestionCenterCost": 0,
                "imagestionAccount": 0,
                "imagestionConceptCod": 0,
                "imagestionProyectCod": 0,
                "imagestionCategoryCod": 0,
                "imagestionProductId": 0,
                "serialNumber": 0,
                "prestashopCombinationId": 0,
                "prestashopValueId": 0,
                "product": {
                    "href": "https://api.bsale.cl/v1/products/656.json",
                    "id": "656"
                },
                "attribute_values": {
                    "href": "https://api.bsale.cl/v1/variants/"
                            "2373/attribute_values.json"
                },
                "costs": {
                    "href": "https://api.bsale.cl/v1/variants/2373/costs.json"
                }
            }
        }

    if url.path == '/v1/price_lists.json':
        return {
            'status_code': 200,
            'content': {
                "href": "https://api.bsale.cl/v1/price_lists.json",
                "count": 1,
                "limit": 25,
                "offset": 0,
                "items": [{
                    "href": "https://api.bsale.cl/v1/price_lists/1.json",
                    "id": "1",
                    "name": "Lista Base",
                    "description": "",
                    "state": 0,
                    "coin": {
                        "href": "https://api.bsale.cl/v1/coins/1.json",
                        "id": "1"
                    },
                    "details": {
                        "href": "https://api.bsale.cl/v1/"
                                "price_lists/1/details.json"
                    }
                }]
            }
        }

    if url.path == \
       '/v1/price_lists/{price_list_id}.json'.format(price_list_id=1):
        return {
            'status_code': 200,
            'content': {
                "href": "https://api.bsale.cl/v1/price_lists/1.json",
                "id": "1",
                "name": "Lista Base",
                "description": None,
                "state": 0,
                "coin": {
                    "href": "https://api.bsale.cl/v1/coins/3.json",
                    "id": "3"
                },
                "details": {
                    "href": "https://api.bsale.cl/v1/price_lists/"
                            "1/details.json"
                }
            }
        }

    if url.path == '/v1/price_lists/count.json':
        return {
            'status_code': 200,
            'content': {
                "count": 1
            }
        }

    if url.path ==\
       '/v1/price_lists/{price_lists_id}/details.json'.format(
           price_lists_id=1):
        return {
            'status_code': 200,
            'content': {
                "href": "https://api.bsale.cl/v1/price_lists/1/details.json",
                "count": 1,
                "limit": 4,
                "offset": 0,
                "items": [{
                    "href": "https://api.bsale.cl/v1/price_lists/"
                            "1/details/1.json",
                    "id": 1,
                    "variantValue": 4590,
                    "variantValueWithTaxes": 5462,
                    "variant": {
                        "href": "https://api.bsale.cl/v1/variant/1.json",
                        "id": "1"
                    }
                }],
                "next": "https://api.bsale.cl/v1/price_lists/"
                        "1/details.json?limit=4&offset=4"
            }
        }

    if url.path ==\
       '/v1/price_lists/{price_list_id}/details/{detail_id}.json'.format(
           price_list_id=1, detail_id=1) and request.method == 'GET':
        return {
            'status_code': 200,
            'content': {
                "href": "https://api.bsale.cl/v1/price_lists/1/details/1.json",
                "id": 1,
                "variantValue": 1000,
                "variantValueWithTaxes": 1190,
                "variant": {
                    "href": "https://api.bsale.cl/v1/variant/1.json",
                    "id": "1"
                }
            }
        }

    if url.path ==\
       '/v1/price_lists/{price_list_id}/details/{detail_id}.json'.format(
           price_list_id=1, detail_id=1) and request.method == 'PUT':
        return {
            'status_code': 200,
            'content': {
                "href": "https://api.bsale.cl/v1/price_lists/1/details/1.json",
                "variantValue": 100.0,
                "variantValueWithTaxes": 119.0,
                "variant": {
                    "href": "https://api.bsale.cl/v1/variant/1.json",
                    "id": "1"
                },
                "id": 1
            }
        }
    if url.path == "/v1/document_types.json":
        return {
            'status_code': 200,
            'content': {
                "href": "https://api.bsale.cl/v1/document_types.json",
                "count": 3,
                "limit": 25,
                "offset": 0,
                "items": [{
                        "href": "https://api.bsale.cl/v1/"
                                "document_types/2.json",
                        "id": 2,
                        "name": "FACTURA EXENTA O NO AFECTA ELECTRONICA",
                        "initialNumber": 1,
                        "codeSii": "34",
                        "isElectronicDocument": 1,
                        "breakdownTax": 1,
                        "use": 0,
                        "isSalesNote": 0,
                        "isExempt": 1,
                        "restrictsTax": 0,
                        "useClient": 1,
                        "messageBodyFormat": "",
                        "thermalPrinter": 1,
                        "state": 0,
                        "copyNumber": 2,
                        "isCreditNote": 0,
                        "continuedHigh": 0,
                        "ledgerAccount": None,
                        "ipadPrint": 0,
                        "ipadPrintHigh": "0",
                        "book_type": {
                            "href": "https://api.bsale.cl/v1/"
                                    "book_types/1.json",
                            "id": "1"
                        }
                    },
                    {
                        "href": "https://api.bsale.cl/v1/"
                                "document_types/3.json",
                        "id": 3,
                        "name": "NOTA CREDITO ELECTRONICA",
                        "initialNumber": 43,
                        "codeSii": "61",
                        "isElectronicDocument": 1,
                        "breakdownTax": 1,
                        "use": 1,
                        "isSalesNote": 0,
                        "isExempt": 0,
                        "restrictsTax": 0,
                        "useClient": 1,
                        "messageBodyFormat": "",
                        "thermalPrinter": 1,
                        "state": 0,
                        "copyNumber": 0,
                        "isCreditNote": 1,
                        "continuedHigh": 0,
                        "ledgerAccount": None,
                        "ipadPrint": 0,
                        "ipadPrintHigh": "0",
                        "book_type": {
                            "href": "https://api.bsale.cl/v1/"
                                    "book_types/1.json",
                            "id": "1"
                        }
                    },
                    {
                        "href": "https://api.bsale.cl/v1/"
                                "document_types/1.json",
                        "id": 1,
                        "name": "NOTA VENTA",
                        "initialNumber": 1,
                        "codeSii": "",
                        "isElectronicDocument": 0,
                        "breakdownTax": 1,
                        "use": 0,
                        "isSalesNote": 1,
                        "isExempt": 0,
                        "restrictsTax": 0,
                        "useClient": 1,
                        "messageBodyFormat": None,
                        "thermalPrinter": 1,
                        "state": 0,
                        "copyNumber": 3,
                        "isCreditNote": 0,
                        "continuedHigh": 0,
                        "ledgerAccount": None,
                        "ipadPrint": 0,
                        "ipadPrintHigh": "0"
                    }
                ]
            }
        }
    if url.path == "/v1/document_types/1.json":
        return {
            'status_code': 200,
            'content': {
                "href": "https://api.bsale.cl/v1/document_types/1.json",
                "id": 1,
                "name": "NOTA VENTA",
                "initialNumber": 1,
                "codeSii": "",
                "isElectronicDocument": 0,
                "breakdownTax": 1,
                "use": 0,
                "isSalesNote": 1,
                "isExempt": 0,
                "restrictsTax": 0,
                "useClient": 1,
                "messageBodyFormat": None,
                "thermalPrinter": 1,
                "state": 0,
                "copyNumber": 3,
                "isCreditNote": 0,
                "continuedHigh": 0,
                "ledgerAccount": None,
                "ipadPrint": 0,
                "ipadPrintHigh": "0"
            }
        }
    if url.path == "/v1/document_types/count.json":
        return {
            'status_code': 200,
            'content': {
                'count': 3
            }
        }

    if url.path == "/v1/document_types/caf.json":
        return {
            'status_code': 200,
            'content': {
                "startDate": 1498694400,
                "expirationDate": 1546041600,
                "startNumber": 1,
                "lastNumber": 5000,
                "lastNumberUsed": 4409,
                "numbersAvailable": 591
            }
        }

    if url.path == "/v1/document_types/number_availables.json":
        return {
            'status_code': 200,
            'content': {
                "numbers_available": 2574,
                "last": 32119
            }
        }
    if url.path == "/v1/offices.json":
        return {
            'status_code': 200,
            'content': {
                'count': 1,
                'items': [
                    {
                        'city': '',
                        'description': '',
                        'isVirtual': 0,
                        'country': '',
                        'municipality': '',
                        'zipCode': '',
                        'longitude': '',
                        'imagestionCellarId': 0,
                        'state': 0,
                        'href': 'https://api.bsale.cl/v1/offices/1.json',
                        'costCenter': None,
                        'address': '',
                        'latitude': '',
                        'id': 1,
                        'name': 'Casa Matriz'
                    }
                ],
                'href': 'https://api.bsale.cl/v1/offices.json',
                'limit': 25,
                'offset': 0}
        }

    logging.debug("no tiene")
    return {
        'status_code': 500,
        'content': {
            {'message': 'mock not found'}
        }
    }
