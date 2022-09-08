#!/usr/bin/python
# -*- coding: UTF-8 -*-
from .constants import Endpoints
from .endpoint import Endpoint


class ProductType(Endpoint):

    @classmethod
    def Get(
        self,
        limit=None,
        offset=None,
        fields=None,
        expand=None,
        name=None,
        state=None,
    ):
        """ Get all the product types from bsale account

        Args:
            limit         (int)  : limita la cantidad de items de una
                                    respuesta JSON, por defecto el limit
                                    es 25, el máximo permitido es 50.
            offset        (int)  : permite paginar los items de una
                                    respuesta JSON, por defecto el
                                    offset es 0.
            fields        (list) : solo devolver atributos específicos de
                                    un recurso.
            expand        (list) : expandir atributos de un recurso.
            name          (str)  : nombre del tipo de producto.
            state         (str)  : estado del tipo de producto.
        Returns:
            (dict) Dictionary with the JSON representation of response
        """

        return self.get(
            Endpoints.PRODUCT_TYPES,
            limit=limit,
            offset=offset,
            fields=fields,
            expand=expand,
            name=name,
            state=state,
        )

    @classmethod
    def GetOne(self, product_type_id):
        """ Get One of the product types from bsale account

        Args:
            product_type_id (int) : product type identificator

        Returns:
            (dict) Dictionary with the JSON representation of response
        """

        return self.get(
            Endpoints.PRODUCT_TYPES_ID.format(product_type_id)
        )

    @classmethod
    def Count(self):
        """ Count all the product types on a bsale account

        Returns:
            (dict) Dictionary with the JSON representation of response
        """
        return self.get(
            Endpoints.COUNT_PRODUCT_TYPES,
        )

    @classmethod
    def GetAttributes(
        self,
        product_type_id,
    ):
        """ Get all atrributes on a product type

        Returns:
            (dict) Dictionary with the JSON representation of response
        """

        return self.get(
            Endpoints.PRODUCT_TYPES_ATRIBUTES.format(product_type_id)
        )

    @classmethod
    def Create(
        self,
        name,
        attributes=None
    ):
        """ POST a new product type on a bsale account

        Args:
            name          (str): nombre del tipo de producto
            atrributes    (list): lista de atributos del tipo de producto

        Returns:
            (dict) Dictionary with the JSON representation of response
        """

        params = {
            "name": name,
            "attributes": attributes

        }

        return self.post(Endpoints.PRODUCT_TYPES, params)
