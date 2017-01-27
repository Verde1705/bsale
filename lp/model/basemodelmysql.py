from tornado.options import options

MySQLdb = None
try:
    import MySQLdb
except:
    pass


class BaseModelMysql():

    @staticmethod
    def db():
        if MySQLdb is not None:
            return MySQLdb.connect(host=options.db_host, user=options.db_user, passwd=options.db_password,db=options.db_name,charset="utf8")

    @staticmethod
    def cur( db ):
        return db.cursor()

    @staticmethod
    def execute( query, data ):

        db = BaseModelMysql.db()
        cur = BaseModelMysql.cur( db )

        try:
            cur.execute(query,data)
            db.commit()
            return cur.fetchall()
        except:
            pass
        finally:
            db.close()
            cur.close()
