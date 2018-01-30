#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import json

from constants import Endpoints, Environment
from endpoint import Endpoint


class PriceList(Endpoint):

    @classmethod
    def Get(
        self,
        limit=None,
        offset=None,
        fields=None,
        expand=None,
        name=None,
        coinid=None,
        state=None
    ):
        # limit, limita la cantidad de items de una respuesta JSON, si no se envía el limit es 25.
        # offset, permite paginar los items de una respuesta JSON, si no se envía el offset es 0.
        # fields, solo devolver atributos específicos de un recurso
        # expand, permite expandir instancias y colecciones.
        # name, Permite filtrar por nombre de la lista de precio.
        # coinid, filtra por la moneda.
        # state, boolean (0 o 1) indica si las listas de precio están activas(0) o inactivas (1).

        # GET /v1/price_lists.json?limit=10&offset=0
        # GET /v1/price_lists.json?fields=[name,description,state]
        # GET /v1/price_lists.json?coinid=1
        # GET /v1/price_lists.json?expand=[coin,details]

        return self.get(
            Endpoints.PRICE_LISTS,
            limit=limit,
            offset=offset,
            fields=fields,
            expand=expand,
            name=name,
            coinid=coinid,
            state=state
        )

    @classmethod
    def GetOne(self, price_list_id, expand=None):
        # Parametros

        # expand, permite expandir instancias y colecciones.
        # Ejemplos

        # GET /v1/price_lists/3.json?expand=[details, coin]

        return self.get(
            Endpoints.PRICE_LISTS_ID.format(price_list_id),
            expand=expand
        )

    @classmethod
    def Count(self):
        return self.get(
            Endpoints.COUNT_PRICE_LIST,
        )

    @classmethod
    def GetDetail(
        self,
        price_list_id,
        expand=None,
        variantid=None,
        code=None,
        barcode=None
    ):
        # expand, permite expandir instancias y colecciones.
        # variantid, filtra por el identificador de la variante (Integer)
        # code, filtra por el SKU de la variante (String).
        # barcode, filtra por el código de barras de la variante (String).

        # GET /v1/price_lists/1/details.json?expand=[variant]
        # GET /v1/price_lists/1/details.json?variantid=149
        # GET /v1/price_lists/1/details.json?code=12345
        # GET /v1/price_lists/1/details.json?barcode=45412431

        return self.get(
            Endpoints.PRICE_LIST_ID_DETAILS.format(price_list_id),
            expand=expand,
            variantid=variantid,
            code=code,
            barcode=barcode
        )

    @classmethod
    def GetOneDetail(
        self,
        price_list_id,
        detail_id,
        variantid=None,
        code=None,
        barcode=None
    ):
        # GET /v1/price_lists/3/details/663.json

        return self.get(
            Endpoints.PRICE_LIST_ID_DETAILS_ID.format(price_list_id, detail_id)
        )
        pass

    @classmethod
    def UpdateDetail(
        self,
        price_list_id,
        detail_id,
        variantValue=0
    ):
        params = {
            'id': detail_id,
            'variantValue': variantValue
        }

        url = Environment.URL + Endpoints.PRICE_LIST_ID_DETAILS_ID.format(price_list_id, detail_id)

        access_token = self.itoken.getToken()

        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            'access_token': access_token
        }
        r = requests.put(url, headers=headers, data=json.dumps(params))
        
        return r.json()
