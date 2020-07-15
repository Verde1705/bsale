#!/usr/bin/python
# -*- coding: UTF-8 -*-

from .constants import Endpoints
from .endpoint import Endpoint


class Coin(Endpoint):

    @classmethod
    def Get(
        self,
        limit=None,
        offset=None,
        fields=None,
        expand=None,
        name=None,
        symbol=None,
        state=None,
        default=None
    ):
        """ Get all the coins from bsale account

        Args:
            limit         (int)    : limita la cantidad de items de una
                                    respuesta JSON, por defecto el limit
                                    es 25, el máximo permitido es 50.
            offset        (int)    : permite paginar los items de una
                                    respuesta JSON, por defecto el
                                    offset es 0.
            fields        (list)   : solo devolver atributos específicos de
                                    un recurso.
            expand        (list)   : permite expandir instancias y
                                    colecciones.
            name          (string) : Permite filtrar por nombre de la moneda.
            symbol        (string) : filtra por símbolo de la moneda.

            state         (int)    : boolean (0 o 1) indica si las formas de
                                    pago están activas(0) inactivas(1).

            default       (bool)    : permite filtrar la moneda por
                                    defecto del sistema.


        Returns:
            (dict) Dictionary with the JSON representation of response
        """

        return self.get(
            Endpoints.COINS,
            limit=limit,
            offset=offset,
            fields=fields,
            expand=expand,
            name=name,
            symbol=symbol,
            state=state,
            default=default
        )

    @classmethod
    def GetOne(self, coin_id):
        """ Get One spesific coin  from bsale account

        Args:
            payment_id (int) : payment  identificator

        Returns:
            (dict) Dictionary with the JSON representation of response
        """

        return self.get(
            Endpoints.COIN_ID.format(coin_id)
        )

    @classmethod
    def GetExchangeRate(
        self,
        coin_id,
        timestamp
    ):
        """ Get the exchange rate for one coin in a spesific time

        Args:
            coin_id      (int)  : unique identifier for coin
            timestamp    (int)  : time on unix format
        Returns:
            (dict) Dictionary with the JSON representation of response
        """

        return self.get(
            Endpoints.COIN_EXCANGE_RATE.format(coin_id, timestamp)
        )

    @classmethod
    def Count(self):
        """ Count all the payment on a bsale account

        Returns:
            (dict) Dictionary with the JSON representation of response
        """
        return self.get(
            Endpoints.COUNT_COIN
        )
