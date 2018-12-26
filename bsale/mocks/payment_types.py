#!/usr/bin/python
# -*- coding: UTF-8 -*-

from bsale.src.constants import Endpoints


def payment_type_mock(url_api, request):
    method = request.method
    endpoint = url_api.path

    if endpoint == '/v1/' + Endpoints.PAYMENT_TYPES:
        if method == "GET":

            return {
                "status_code": 200,
                "content": {
                    "href": "https://api.bsale.cl/v1/payment_types.json",
                    "count": 5,
                    "limit": 25,
                    "offset": 0,
                    "items": [
                        {
                            "href": "https://api.bsale.cl/v1/"
                                    "payment_types/7.json",
                            "id": 7,
                            "name": "ABONO DE CLIENTE",
                            "isVirtual": 0,
                            "isCheck": 0,
                            "maxCheck": None,
                            "isCreditNote": 0,
                            "isClientCredit": 0,
                            "isCash": 0,
                            "isCreditMemo": 1,
                            "state": 0,
                            "maxClientCuota": 0,
                            "ledgerAccount": "",
                            "ledgerCode": None,
                            "isAgreementBank": 0,
                            "agreementCode": None
                        },
                        {
                            "href": "https://api.bsale.cl/v1/"
                                    "payment_types/5.json",
                            "id": 5,
                            "name": "CHEQUE",
                            "isVirtual": 0,
                            "isCheck": 1,
                            "maxCheck": 3,
                            "isCreditNote": 0,
                            "isClientCredit": 0,
                            "isCash": 0,
                            "isCreditMemo": 0,
                            "state": 0,
                            "maxClientCuota": 0,
                            "ledgerAccount": "1110201",
                            "ledgerCode": None,
                            "isAgreementBank": 0,
                            "agreementCode": None,
                            "dynamic_attributes": {
                                "href": "https://api.bsale.cl/v1/"
                                        "payment_types/5/"
                                        "dynamic_attributes.json"
                            }
                        },
                        {
                            "href": "https://api.bsale.cl/v1/"
                                    "payment_types/4.json",
                            "id": 4,
                            "name": "CREDITO",
                            "isVirtual": 0,
                            "isCheck": 0,
                            "maxCheck": None,
                            "isCreditNote": 0,
                            "isClientCredit": 1,
                            "isCash": 0,
                            "isCreditMemo": 0,
                            "state": 0,
                            "maxClientCuota": 0,
                            "ledgerAccount": "",
                            "ledgerCode": None,
                            "isAgreementBank": 0,
                            "agreementCode": None
                        },
                        {
                            "href": "https://api.bsale.cl/v1/"
                                    "payment_types/1.json",
                            "id": 1,
                            "name": "EFECTIVO",
                            "isVirtual": 0,
                            "isCheck": 0,
                            "maxCheck": None,
                            "isCreditNote": 0,
                            "isClientCredit": 0,
                            "isCash": 1,
                            "isCreditMemo": 0,
                            "state": 0,
                            "maxClientCuota": 0,
                            "ledgerAccount": "1112401",
                            "ledgerCode": None,
                            "isAgreementBank": 0,
                            "agreementCode": None
                        },
                        {
                            "href": "https://api.bsale.cl/v1/"
                                    "payment_types/3.json",
                            "id": 3,
                            "name": "NOTA CREDITO DEVOLUCION",
                            "isVirtual": 0,
                            "isCheck": 0,
                            "maxCheck": None,
                            "isCreditNote": 1,
                            "isClientCredit": 0,
                            "isCash": 0,
                            "isCreditMemo": 0,
                            "state": 0,
                            "maxClientCuota": 0,
                            "ledgerAccount": "1112301",
                            "ledgerCode": None,
                            "isAgreementBank": 0,
                            "agreementCode": None
                        }
                    ]
                }

            }

        if method == "POST":
            return {
                "status_code": 200,
                "content": {
                    "href": "https://api.bsale.cl/v1/payment_types/1.json",
                    "id": 1,
                    "name": "new payment type",
                    "isVirtual": 0,
                    "isCheck": 0,
                    "maxCheck": None,
                    "isCreditNote": 0,
                    "isClientCredit": 0,
                    "isCash": 0,
                    "isCreditMemo": 0,
                    "state": 0,
                    "maxClientCuota": 0,
                    "ledgerAccount": "111-01",
                    "ledgerCode": "1234",
                    "isAgreementBank": 0,
                    "agreementCode": None
                }
            }

    if endpoint == '/v1/' + Endpoints.COUNT_PAYMENT_TYPES:
        return {
            "status_code": 200,
            "content": {
                "count": 4
            }
        }

    if endpoint == '/v1/' + Endpoints.PAYMENT_TYPES_ID.format(1):
        return {
            "status_code": 200,
            "content": {
                "href": "https://api.bsale.cl/v1/payment_types/1.json",
                "id": 1,
                "name": "payment type",
                "isVirtual": 0,
                "isCheck": 0,
                "maxCheck": None,
                "isCreditNote": 0,
                "isClientCredit": 0,
                "isCash": 0,
                "isCreditMemo": 1,
                "state": 0,
                "maxClientCuota": 0,
                "ledgerAccount": "",
                "ledgerCode": None,
                "isAgreementBank": 0,
                "agreementCode": None
            }
        }

    if endpoint == '/v1/' + Endpoints.PAYMENT_TYPES_DINAMIC_ATTR.format(1):
        return {
            "status_code": 200,
            "content": {
                "href": "https://api.bsale.cl/v1/dynamic_attributes.json",
                "count": 6,
                "limit": 25,
                "offset": 0,
                "items": [
                    {
                        "href": "https://api.bsale.cl/v1/"
                                "dynamic_attributes/2.json",
                        "id": 2,
                        "name": "Banco",
                        "tip": "",
                        "type": 4,
                        "isMandatory": 1,
                        "state": 0,
                        "payment_type": {
                            "href": "https://api.bsale.cl/v1/"
                                    "payment_types/5.json",
                            "id": "5"
                        }
                    },
                    {
                        "href": "https://api.bsale.cl/v1/"
                                "dynamic_attributes/3.json",
                        "id": 3,
                        "name": "Número",
                        "tip": "",
                        "type": 4,
                        "isMandatory": 1,
                        "state": 0,
                        "payment_type": {
                            "href": "https://api.bsale.cl/v1/"
                                    "payment_types/5.json",
                            "id": "5"
                        }
                    },
                    {
                        "href": "https://api.bsale.cl/v1/"
                                "dynamic_attributes/19.json",
                        "id": 19,
                        "name": "Nº Autoriza DICOM",
                        "tip": "",
                        "type": 3,
                        "isMandatory": 1,
                        "state": 1,
                        "payment_type": {
                            "href": "https://api.bsale.cl/v1/"
                                    "payment_types/5.json",
                            "id": "5"
                        }
                    },
                    {
                        "href": "https://api.bsale.cl/v1/"
                                "dynamic_attributes/94.json",
                        "id": 94,
                        "name": "Opcion",
                        "tip": "",
                        "type": 7,
                        "isMandatory": 0,
                        "state": 0,
                        "payment_type": {
                            "href": "https://api.bsale.cl/v1/"
                                    "payment_types/5.json",
                            "id": "5"
                        },
                        "details": {
                            "href": "https://api.bsale.cl/v1/"
                                    "dynamic_attributes/94/details.json",
                            "count": 3,
                            "limit": 25,
                            "offset": 0,
                            "items": [
                                {
                                    "href": "https://api.bsale.cl/v1/"
                                            "dynamic_attributes/94/"
                                            "details/60.json",
                                    "id": 60,
                                    "name": "A",
                                    "state": 0
                                },
                                {
                                    "href": "https://api.bsale.cl/v1/"
                                            "dynamic_attributes/94/"
                                            "details/61.json",
                                    "id": 61,
                                    "name": "B",
                                    "state": 0
                                },
                                {
                                    "href": "https://api.bsale.cl/v1/"
                                            "dynamic_attributes/"
                                            "94/details/62.json",
                                    "id": 62,
                                    "name": "C",
                                    "state": 0
                                }
                            ]
                        }
                    },
                    {
                        "href": "https://api.bsale.cl/v1/"
                                "dynamic_attributes/18.json",
                        "id": 18,
                        "name": "Titular",
                        "tip": "",
                        "type": 4,
                        "isMandatory": 1,
                        "state": 0,
                        "payment_type": {
                            "href": "https://api.bsale.cl/v1/"
                                    "payment_types/5.json",
                            "id": "5"
                        }
                    },
                    {
                        "href": "https://api.bsale.cl/v1/"
                                "dynamic_attributes/17.json",
                        "id": 17,
                        "name": "Vencimiento",
                        "tip": "",
                        "type": 1,
                        "isMandatory": 1,
                        "state": 1,
                        "payment_type": {
                            "href": "https://api.bsale.cl/v1/"
                                    "payment_types/5.json",
                            "id": "5"
                        }
                    }
                ]
            }
        }
    return "next"
