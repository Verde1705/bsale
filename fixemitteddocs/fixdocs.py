#!/usr/bin/python
# -*- coding: UTF-8 -*-


import bsale
from lp.json_util import loads


if __name__ == "__main__":

    file = open("emitteddocs.json")
    file_content = file.read().strip()

    json_data = loads(file_content)
    # json_data = { 
    #     "items" : [
    #         # {'id': 1747},
    #         # {'id': 1748},
    #         # {'id': 1749},
    #         # {'id': 1750},
    #         # {'id': 1751},
    #         # {'id': 1752},
    #         # {'id': 1753},
    #         # {'id': 1754},
    #         # {'id': 1755},
    #         # {'id': 1756},
    #         # { 'id' : 1757}
    #       ]}

    # last 1796

    document = bsale.Document()

    counter = 0

    for item in json_data["items"]:

        if counter < 50 and item["id"] > 1757:

            detail = document.GetDetailDocument(item["id"])
            details = []
            for items in detail["items"]:
                det = {
                    "documentDetailId": items["id"],
                    "quantity": int(items["quantity"]),
                    "unitValue": (items['netAmount']/1.19)
                }
                details.append(det)

            # client = {
            #     "code": "1-9",
            #     "city": "Puerto Varas",
            #     "municipality": "comuna",
            #     "activity": "giro",
            #     "address": "direccion"
            #   }

            client = {
                "municipality": "Las Condes",
                "activity": "Sin dato",
                "city": "Santiago",
                "address": "Alonso de Cordova",
                "code": "22222222-2"
            }

            params = {
              "documentTypeId": 2,
              "officeId": 1,
              "referenceDocumentId": item["id"],
              "expirationDate": 1474502400,
              "emissionDate": 1474502400,
              "motive": "prueba api",
              "declareSii": 1,
              "priceAdjustment": 0,
              "editTexts": 0,
              "type": 0,
              "details":details,
              "client":client
            }

            print document.CreateCreditNote(params)

        if counter >= 50:
            break

        counter += 1
