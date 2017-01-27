'''
Created on 13/12/2012

@author: ricardo
'''

import hashlib
import random
import tornado
import tornado.web
import requests
import json

import traceback
import json as json_util
from tornado.template import Loader

# from bson import json
# from lputils import MoneyFormat
# from loadingplay.multilang.lang import lpautoSelectCurrentLang

from lp.model.basemodel import BaseModel
from lp.globals import enviroment, Enviroment
from lp.utils import Timer


translation_dictionary = {}


class BaseHandler(tornado.web.RequestHandler):

    @property
    def referer(self):
        # TODO: deberia guardar el old referer en una variable de session
        self._referer = self.request.headers['Referer']
        self._referer = self._referer.replace("/auth/loadingplay", "/").replace("/registrar/usuario", "/")

        return self._referer

    @property
    def db(self):
        return self.application.db

    @property
    def side_menu(self):
        return self.application.side_menu

    def set_active(self, active_name):
        for x in self.side_menu:
            # x["class"] = "panel"
            if x["name"] == active_name:
                x["class"] += " active"

            if "sub_menu" in x:
                for y in x['sub_menu']:
                    y['class'] = ""
                    if y["name"] == active_name:
                        # print "llegaaaa"
                        x["class"] += " active"
                        y["class"] = " active"

    def __init__(self, application, request, **kwargs):
        tornado.web.RequestHandler.__init__(self, application, request, **kwargs)
        # detecto el lenguage del navegador del usuario
        # lpautoSelectCurrentLang(self)

    def set_current_user(self, user):
        if user:
            self.set_secure_cookie("user",  json_util.dumps(user) )
        else:
            self.clear_cookie("user")

    def get_current_user(self):
        user_json = self.get_secure_cookie("user")
        if not user_json: 
            return None

        return json_util.loads( user_json )

    def get_usuarios(self):
        return self.db.user.find({"picture":{"$exists":True}}).limit(24)

    def get_login_url(self):
        return u"/auth/login"

    @staticmethod
    def reload_translate( variable_name="" ):
        global translation_dictionary
        q = """ SELECT text, variable_name FROM lang WHERE lang='en' """
        data = BaseModel.execute_query( q, {} )

        for d in data:
            translation_dictionary[d["variable_name"]] = d["text"]

    def translate( self, variable_name, default="" ):

        global translation_dictionary

        if variable_name in translation_dictionary:
            return translation_dictionary[variable_name]

        if len( translation_dictionary ) == 0:
            BaseHandler.reload_translate()

        return default

    def split_and_clear( self, args ):
        data = []

        for x in args:
            s = x.split( "[" )
            t = []
            for y in range(0, len(s)):
                t.append( s[y].replace( "]", "" ) )

            t.append( self.get_argument(x, "") )
            data.append( t )

        return data

    def parser_2(self, lst, obj):
        if len( lst ) == 2:
            obj[lst[0]] = lst[1]
        else:
            try:
                if obj[lst[0]] is None:
                    obj[lst[0]] = {}
            except:
                obj[lst[0]] = {}
            self.parser_2( lst[1:len(lst)], obj[lst[0]] )

    def parser(self, arguments, data):

        for arg in arguments:
            if len( arg ) == 2:
                data[arg[0]] = arg[1]
            elif ( len( arg ) > 2 ):

                try:
                    if data[arg[0]] is None:
                        pass
                except:
                    data[arg[0]] = {}

                self.parser_2( arg[1:len(arg)], data[arg[0]] )

    def parse_arguments(self):
        data = {}
        self.parser( self.split_and_clear( self.request.arguments ), data )

        return data

    def dumps( self, data ):
        return json_util.dumps( data )

    def month_name(self, month_number):
        if month_number == 1:
            return "Enero"
        elif month_number == 2:
            return "Febrero"
        elif month_number == 3:
            return "Marzo"
        elif month_number == 4:
            return "Abril"
        elif month_number == 5:
            return "Mayo"
        elif month_number == 6:
            return "Junio"
        elif month_number == 7:
            return "Julio"
        elif month_number == 8:
            return "Agosto"
        elif month_number == 9:
            return "Septiebre"
        elif month_number == 10:
            return "Octubre"
        elif month_number == 11:
            return "Noviembre"
        elif month_number == 12:
            return "Diciembre"

    def nocache_static( self ):
        if "nocache_static" not in tornado.options.options:
            return "static"
        return tornado.options.options["nocache_static"]

    def render(self, template_name ,**kwargs):
        # menu
        uri = self.request.uri
        menu = uri
        # menu

        # global vars
        kwargs["menu"] = menu
        kwargs["user"] = self.get_current_user()
        kwargs["t"] = self.translate
        kwargs["money_format"] = self.money_format
        kwargs["random"] = random.random
        kwargs["dumps"] = self.dumps
        kwargs["nocache_static"] = self.nocache_static()
        kwargs["enviroment"] = "local" if enviroment == Enviroment.ONDEV else "other"

        # overrided method
        tornado.web.RequestHandler.render(self, template_name, **kwargs)

    def showRestError(self, message, code=100, _type=""):
        json = {
            "error": {
                "message": message, 
                "type": _type, 
                "code": code
            }
        }

        self.write( json )

    def showRestSuccess(self, message):
        json = {
            "success" : True,
            "message" : message
        }

        self.write(json)

    def write_error(self, status_code=500, **kwargs):

        tb_text = []
        display = ""

        # in debug mode, try to send a traceback
        self.set_header('Content-Type', 'text/plain')
        for line in traceback.format_exception(*kwargs["exc_info"]):
            tb_text.append(line)

        self.set_status(status_code)
        self.set_header('Content-Type', 'text/html; charset=UTF-8')

        if enviroment == Enviroment.PRODUCTION:
            display = 'display:none'

        self.finish("""
        <html>
            <title>%(code)d: %(message)s</title>
            <body>
                <div>
                    %(code)d: %(message)s
                </div>
                <div>
                    <a href="/" >Volver</a>
                </div>
                <div style="%(display)s" >
                    %(traceback)s
                </div>
            </body>
        </html>
        """ % {
            "code" : status_code,
            "message" : self._reason,
            "traceback" : "".join(tb_text).replace("\n", "<br>"),
            "display" : display
        })

        # if self.settings.get("serve_traceback") and "exc_info" in kwargs:
        #     # in debug mode, try to send a traceback
        #     self.set_header('Content-Type', 'text/plain')
        #     for line in traceback.format_exception(*kwargs["exc_info"]):
        #         tb_text.append(line)
        #     self.write("".join(tb_text))
        #     self.finish()
        # else:
        #     self.set_status(status_code)
        #     if kwargs['reason']:
        #         self.finish(kwargs['reason'])
        #     else: 
        #         self.finish("<html><title>%(code)d: %(message)s</title>"
        #             "<body>%(code)d: %(message)s</body></html>" % {
        #                 "code": status_code,
        #                 "message": self._reason,
        #             })

    def md5(self, data):
        return hashlib.md5(data.encode("utf")).hexdigest()

    def template_loader(self):
        return Loader( self.settings["template_path"] )

    def money_format(self, value):
        try:
            return '{:20,.0f}'.format(value).replace( ",", "." ).strip()
        except:
            return ''

    def check_xsrf_cookie(self):
        # --- disable xsrf cookie ---
        return True

    def initialize(self):
        try:
            self.timer = Timer()
        except:
            pass

    def prepare(self):
        try:
            self.timer.start()
        except:
            pass

        tornado.web.RequestHandler.prepare(self)

    def before_finish(self):
        """ called once finish is called but before executed

        override this methd to send stuff just before finish
        """
        pass

    # def finish(self, chunk=None):
    #     try:
    #         if enviroment == Enviroment.PRODUCTION:
    #             self.timer.end()
    #             url = "{}://{}{}".format(
    #                     self.request.protocol,
    #                     self.request.host,
    #                     self.request.uri
    #                 )

    #             data = {
    #                 "url" : url,
    #                 "execution_time" : "{}".format(self.timer.secs)
    #             }
    #             requests.put('http://performance.loadingplay.com/api/v1/report', data=json.dumps(data))

    #         self.before_finish()
    #     except Exception, ex:
    #         print str(ex)
    #         pass
    #     tornado.web.RequestHandler.finish(self, chunk=chunk)
