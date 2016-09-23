#!/usr/bin/python
# -*- coding: UTF-8 -*-


import bsale
# from lp.json_util import loads


if __name__ == "__main__":

    file = open("emitteddocs.json")
    file_content = file.read().strip()

    # json_data = loads(file_content)
    json_data = { 
        "items" : [
            {'id': 1746},
            {'id': 1747},
            {'id': 1748},
            {'id': 1749}]}

    document = bsale.Document()

    for item in json_data["items"]:

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
