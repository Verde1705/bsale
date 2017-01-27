import psycopg2
import psycopg2.extras
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class ScriptLoader(object):
    """
    this script load a file with sql data to a selected database
    """

    def __init__(self):
        """
        default constructor
        """
        super(ScriptLoader, self).__init__()

        self._dbname = "gamelab"
        self._user = "ricardo"
        self._host = "ondev.today"
        self._password = "escuela16761"
        self._script_file = "sql_script.sql"

    @property
    def dbname(self):
        return self._dbname

    @dbname.setter
    def dbname(self, value):
        self._dbname = value

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, value):
        self._host = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def script_file(self):
        return self._script_file

    @script_file.setter
    def script_file(self, value):
        self._script_file = value

    def openConnection(self):
        return psycopg2.connect( 
                "dbname='"+self.dbname+
                "' user='"+self.user+
                "' host='"+self.host+
                "' password='"+self.password+"'" )

    def getCursor(self, conn):
        return conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


    # def dropTablesQuery(self):
    #     try:
    #         conn = self.openConnection()
    #         cur = self.getCursor(conn)
    #     except:
    #         return False

    #     try:
    #         # getting tables
    #         drop_query = """SELECT 'DROP TABLE '
    #                                     || string_agg(quote_ident(t.tablename), ', ')
    #                                     || ' CASCADE'
    #                                 FROM   pg_tables t
    #                                 WHERE  t.tableowner = '{}';""".format( self.user )

    #         cur.execute( drop_query )
    #         conn.commit()

    #         data = cur.fetchall()

    #         for d in data:
    #             print "{}".format( d )
    #             cur.execute( d[0] )
    #             conn.commit()

    #         return True
    #     except Exception, e:
    #         print "cant drop tables : {}".format(str(e))
    #         return False
    #     finally:
    #         conn.close()
    #         cur.close()

    # def dropSequencesQuery(self):
    #     try:
    #         conn = self.openConnection()
    #         cur = self.getCursor(conn)
    #     except:
    #         return False

    #     try:
    #         # getting tables
    #         drop_query = """SELECT 'DROP SEQUENCE '
    #                                     || string_agg(quote_ident(t.tablename), ', ')
    #                                     || ' CASCADE'
    #                                 FROM   pg_sequences t
    #                                 WHERE  t.sequenceowner = '{}';""".format( self.user )

    #         cur.execute( drop_query )
    #         conn.commit()

    #         data = cur.fetchall()

    #         for d in data:
    #             print "{}".format( d )
    #             cur.execute( d[0] )
    #             conn.commit()

    #         return True
    #     except Exception, e:
    #         print "cant drop seuqnces : {}".format(str(e))
    #         return False
    #     finally:
    #         conn.close()
    #         cur.close()

    def dropDatabase(self, db, user, password):

        conn = psycopg2.connect( 
                        "dbname='"+db+"' user='"+user+
                        "' host='"+self.host+
                        "' password='"+password+"'" )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()

        try:
            cur.execute( 
                "DROP DATABASE " + self.dbname + ";" )

        except Exception, e:
            print "cant delete database {} : {}".format( self.dbname, str( e ) )

    def createNewDatabase(self, db, user, password):
        conn = psycopg2.connect( 
                        "dbname='"+db+"' user='"+user+
                        "' host='"+self.host+
                        "' password='"+password+"'" )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()

        try:
            try:
                cur.execute( 
                    "CREATE DATABASE " + self.dbname + 
                    " WITH OWNER = " + self.user + ";" )

            except Exception, e:
                print str( e )


            try:
                cur.execute( 
                    "GRANT ALL PRIVILEGES ON DATABASE " + self.dbname +
                    " TO " + self.user + "" )
            except Exception, e:
                print str( e )

            cur.close()
            conn.close()
        except Exception, e:
            print str( e )

    def delete_old(self, database=None, user=None, password=None):
        """
        clean the current databse, must delete, 
        tables, sequences and views

        prerequisites : 
        self.dbname
        self.user
        self.host
        self.password

        Parameters:
            Sometime you need to connect to other database in order to delete,
            you can pass user, passwor and database.
        """

        u = self.user if user is None else user
        p = self.password if password is None else password
        d = self.dbname if database is None else database

        try:
            self.dropDatabase(d, u, p)
            self.createNewDatabase(d, u, p)
        except Exception, ex:
            print "error : {}".format(ex)

    def execute(self):
        """
        executes the indicated file

        prerequisites:
        self.script_file
        """
        try:
            f = open( self.script_file, "r" )
            script = str(f.read())

            conn = psycopg2.connect( 
                        "dbname='"+self.dbname+
                        "' user='"+self.user+
                        "' host='"+self.host+
                        "' password='"+self.password+"'" )
            cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

            cur.execute( script )

            conn.commit()

            cur.close()
            conn.close()
            f.close()
        except Exception,e:
            print "file : {}".format( self.script_file )
            print str( e )
