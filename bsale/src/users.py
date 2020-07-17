#!/usr/bin/python
# -*- coding: UTF-8 -*-


from .constants import Endpoints
from .endpoint import Endpoint


class Users(Endpoint):

    @classmethod
    def Get(
        self,
        limit=None,
        offset=None,
        fields=None,
        expand=None,
        firstname=None,
        lastname=None,
        email=None,
        officeid=None,
        state=None
    ):
        """
        # Parametros

        # limit, limita la cantidad de items de una respuesta JSON,
          por defecto el limit es 25, el máximo permitido es 50.
        # offset, permite paginar los items de una respuesta JSON,
          por defecto el offset es 0.
        # fields, solo devolver atributos específicos de un recurso
        # expand, permite expandir instancias y colecciones.
        # firstname, filtra los usuarios por nombre.
        # lastname, filtra los usuarios por apellido.
        # email, filtra los usuarios por email.
        # officeid, recupera los usuarios por la sucursal que tienen asignada.
        # state, boolean (0 o 1) indica si los usuarios están
          activos(0) inactivos (1).

        # Ejemplos

        # GET /v1/users.json?limit=10&offset=0
        # GET /v1/users.json?fields=[firstname,lastname]
        # GET /v1/users.json?officeid=1
        # GET /v1/users.json?expand=[office]
        # GET /v1/users.json?state=0
        """

        # get all parameters
        return self.get(
            Endpoints.USERS,
            limit=limit,
            offset=offset,
            fields=fields,
            expand=expand,
            firstname=firstname,
            lastname=lastname,
            email=email,
            officeid=officeid,
            state=state
        )

    @classmethod
    def GetSalesSummary(
        self,
        userid,
        startdate=None,
        enddate=None
    ):
        """
        # Parametros

        # userid, recupera las ventas para un usuario específico (Integer).
        # startdate, fecha de inicio de ventas , por defecto es la fecha
          del dia de la petición (Integer).
        # enddate, fecha fin de ventas, por defecto es la fecha del dia
          de la petición (Integer).

        # Ejemplos

        # GET /v1/users/sales_summary.json?userid=113
        # GET /v1/users/sales_summary.json?
            startdate=1438560000&enddate=1438560000
        # GET /v1/users/sales_summary.json
            ?startdate=1438560000&enddate=1438560000&userid=113
        """

        # get all parameters
        return self.get(
            Endpoints.USERS_SALES_SUMMARY,
            userid=userid,
            startdate=startdate,
            enddate=enddate
        )
