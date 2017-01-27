#!/usr/bin/python
# -*- coding: UTF-8 -*-
import hashlib
from tornado.options import options
from ..globals import *


# ---- import psycopg ---
psycopg2 = None

try:
    import psycopg2
    import psycopg2.extras
except:
    pass

conn = None
trying_count = 0


def openConnection():
    try:
        global conn
        if psycopg2 is not None:

            db_port = 5432

            try:
                db_port = options.db_port
            except:
                pass

            conn = psycopg2.connect(
                    "dbname='{}' user='{}' host='{}' password='{}' port='{}'"
                    .format(
                        options.db_name,
                        options.db_user,
                        options.db_host,
                        options.db_password,
                        db_port))
        else:
            raise Exception( "psycopg2 is none" )

    except Exception, e:
        raise Exception( 
            "I am unable to connect to the database : {}".format( str( e ) ) )


class BaseModel(object):

    NONE = 0
    ERROR = 2
    VALIDATION_ERROR = 1
    SUCCESS = 3

    def __init__(self):
        pass

    # you must close the cursor after use it
    def db(self, conn):
        return conn

    def cursor():
        return BaseModel.cursor()

    @staticmethod
    def db():
        try:
            if conn is None or conn.closed != 0:
                openConnection()

            return conn
        except Exception, e:
            print str(e)
            raise Exception(
                "I am unable to connect to the database : {}".format( str( e ) ))

    @staticmethod
    def cursor(conn, cursor_factory=psycopg2.extras.DictCursor):
        try:

            if psycopg2 is not None:
                if cursor_factory is None:
                    cur = conn.cursor()
                else:
                    cur = conn.cursor(cursor_factory=cursor_factory)
            else:
                raise Exception( "psycopg2 is none" )

            return cur
        except Exception, e:
            raise Exception("unable to create cursor : {}".format( str( e ) ))

    @classmethod
    def execute_query(cls, query, params={}, use_real=False):
        """
        execute a query using psycopg2.extras.DictCursor
        """
        if use_real:
            return cls.execute_query_builder(
                        query, 
                        params,
                        psycopg2.extras.RealDictCursor)
        else:
            return cls.execute_query_builder(
                        query, 
                        params, 
                        psycopg2.extras.DictCursor)

    @classmethod
    def execute_query_real(cls, query, params={}):
        """
        execute a query using psycopg2.extras.RealDictCursor
        """
        return cls.execute_query( 
                    query, 
                    params, 
                    True )

    @classmethod
    def execute_query_builder(cls, query, params, builder=psycopg2.extras.DictCursor):
        """
        executes a query with an especific constructor
        """
        try:
            conn = cls.db()
            cur = BaseModel.cursor(conn, builder)

            cur.execute( query, params )
            conn.commit()

            try:
                return cur.fetchall()
            except Exception, e:
                # raise e
                pass

        except Exception, e:
            raise e
            # print cur.mogrify( query, params )
            # print "error : {}".format( str(e) )
        finally:
            conn.close()
            cur.close()

    @staticmethod
    def mogrify(query, params):
        try:
            conn = BaseModel.db()
            cur = BaseModel.cursor(conn)

            return cur.mogrify( query, params )

        except Exception, e:
            raise e
            # print cur.mogrify( query, params )
            # print "error : {}".format( str(e) )
        finally:
            conn.close()
            cur.close()

    @staticmethod
    def md5(data):
        return hashlib.md5(data.encode("utf")).hexdigest()

    @staticmethod
    def error(error_code, error_message, result={}):
        return { "error" : error_code, "message" : error_message, "result": result }

    @staticmethod
    def returnResult(state, message, result=None):
        return {"state": state,"message": message, "result": result}
