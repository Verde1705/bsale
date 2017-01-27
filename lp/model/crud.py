#!/usr/bin/python
# -*- coding: UTF-8 -*-

from lp.model.basemodel import BaseModel
from lp.globals import report
import psycopg2
import re


class SimpleCRUD(BaseModel):
    """
    basic implementation for a CRUD,

    @example : 
        for example if you execute 
        SimpleCRUD.create( "table_name", { "foo" : 1, "bar": 2 ] } )

        will be executed:
        INSERT INTO <table_name> ( "foo", "bar" ) 
                VALUES (DEFAULT, "foo", "bar")
        RETURNING id
    """

    @staticmethod
    def secureField(**elements):
        """
        ensures anti sql injection
        """
        secured_elements = {}

        for k in elements:
            secured_elements[k] = psycopg2 \
                                    .extensions \
                                    .adapt(elements[k]).getquoted()

        return secured_elements

    @staticmethod
    def getValues(**elements):
        """
        return query formatted values
        """

        secured_elements = SimpleCRUD.secureField(**elements)
        values = []
        for k, v in secured_elements.iteritems():
            # v = re.sub(r'[^%]%{1}', '%%', v)
            try:
                v = v.replace("%", "%%")
            except:
                pass
            values.append( v )
        return ", ".join(values)

    @staticmethod
    def getUpdateValues(**elements):
        """
        return query formatted values
        """

        secured_elements = SimpleCRUD.secureField(**elements)
        values = []
        for k, v in secured_elements.iteritems():
            # v = re.sub(r'[^%]%{1}', '%%', v)
            v = v.replace("%", "%%")
            values.append( "{variable} = {value}".format(variable=k, 
                                                         value=v) )
        return ", ".join(values)

    @staticmethod
    def getRows(**elements):
        """
        return query formatted keys
        """

        secured_elements = SimpleCRUD.secureField(**elements)

        keys = []

        for v in secured_elements:
            keys.append(v)

        return ", ".join(keys)

    @staticmethod
    def getWhere(**elements):
        secured_elements = SimpleCRUD.secureField(**elements)
        comparable_elements = []

        for k in secured_elements:
            comparable_elements.append( 
                "{} = {}".format( k, secured_elements[k] ) )

        return " AND ".join(comparable_elements)

    @staticmethod
    def create( table_name, **elements ):
        """
        for example if you execute 
        SimpleCRUD.create( "table_name", { "foo" : 1, "bar": 2 ] } )

        will be executed:
        INSERT INTO <table_name> ( "foo", "bar" ) 
            VALUES (DEFAULT, "foo", "bar")
        RETURNING id

        and id is returned
        """

        query_data      = SimpleCRUD.getValues(**elements)
        query_headers   = SimpleCRUD.getRows(**elements)

        query = """ INSERT INTO "{}" (id, {}) 
                    VALUES (DEFAULT, {})
                    RETURNING id; """\
                .format( 
                    table_name, 
                    query_headers, 
                    query_data )

        try:
            data = BaseModel.execute_query(query)[0]

            if "id" in data:
                return data["id"]
            elif len(data) > 0:
                return data[0]
            else:
                return data
        except Exception,ex:
            report("SimpleCRUD -> create : {}".format(str(ex)))

    @staticmethod
    def read( table_name, **elements ):
        """
        execute a query like this:

        SELECT * FROM <table_name>
        WHERE  a = a AND
                b = b AND
                c = c
        LIMIT 1;
        """

        query_data = SimpleCRUD.getWhere(**elements)
        query = """ SELECT * FROM "{}"
                    WHERE {}
                    LIMIT 1
                """.format(table_name, query_data)

        try:
            return BaseModel.execute_query( query, {} )[0]
        except:
            pass

    @staticmethod
    def delete(table_name, **elements):
        query_data = SimpleCRUD.getWhere(**elements)
        query = """ DELETE FROM "{}"
                    WHERE {}
                    RETURNING id
                """.format(table_name, query_data)

        try:
            data = BaseModel.execute_query(query, {})[0]
            if data is None:
                return False
            else:
                return True
        except:
            return False

    @staticmethod
    def update(table_name, content_id, **elements):

        update_values = SimpleCRUD.getUpdateValues(**elements)
        query = """ UPDATE "{}"
                    SET {}
                    WHERE id = %(id)s
                    RETURNING id
                """.format(table_name, update_values)

        parameters = {
            "id": content_id
        }

        try:
            data = BaseModel.execute_query(query, parameters)[0]
            if "id" in data:
                return data["id"]
            elif len(data) > 0:
                return data[0]
            else:
                return data
        except Exception,ex:
            report("SimpleCRUD -> update : {}".format(str(ex)))
