import socket
import config
import os
import traceback
import hashlib
from emailreport import EmailReport


host_name = socket.gethostname()

SUCCESS_CODE = 0
EXCEPTION_CODE = 1
VALIDATION_CODE = 2

server_id = int(int(hashlib.sha1(host_name).hexdigest(), 16) % (10 ** 2))


print "host_name : {}".format( host_name )
print "server id : {}".format( server_id )

PORT = 0
DB_NAME = config.LOCAL_DB_NAME
DB_USER = config.LOCAL_USER
DB_HOST = config.LOCAL_HOST
DB_PASSWORD = config.LOCAL_PASSWORD
DB_PORT = 5432


class Enviroment(object):
    LOCAL = 1
    ONDEV = 2
    ONTEST = 3
    PRODUCTION = 4
    DESIGNER = 5


def forceOntest():

    global DB_NAME
    global DB_USER
    global DB_HOST
    global DB_PASSWORD
    global DB_PORT
    global enviroment

    DB_NAME = config.ONTEST_DB_NAME
    DB_USER = config.ONTEST_USER
    DB_HOST = config.ONTEST_HOST
    DB_PASSWORD = config.ONTEST_PASSWORD
    try:
        DB_PORT = config.ONTEST_DB_PORT
    except:
        pass

    enviroment = Enviroment.ONTEST


def setDesignerMode():
    global DB_NAME
    global DB_USER
    global DB_HOST
    global DB_PASSWORD
    global DB_PORT
    global enviroment

    DB_NAME = config.DESIGNER_DB_NAME
    DB_USER = config.DESIGNER_USER
    DB_HOST = config.DESIGNER_HOST
    DB_PASSWORD = config.DESIGNER_PASSWORD

    try:
        DB_PORT = config.DESIGNER_DB_PORT
    except:
        pass

    enviroment = Enviroment.DESIGNER


enviroment = Enviroment.PRODUCTION


if "development" in host_name:
    enviroment = Enviroment.ONDEV
if host_name == "prokamikaze":
    enviroment = Enviroment.ONTEST
if "local" in host_name or os.name == "nt" or host_name == "estefi-Aspire-S3" or \
        "Mac" in host_name or "MBP" in host_name or "mbp" in host_name:
    enviroment = Enviroment.LOCAL

if enviroment == Enviroment.LOCAL:

    PORT = config.DEVELOPMENT_PORT
    DB_NAME = config.LOCAL_DB_NAME
    DB_USER = config.LOCAL_USER
    DB_HOST = config.LOCAL_HOST
    DB_PASSWORD = config.LOCAL_PASSWORD
    try:
        DB_PORT = config.LOCAL_DB_PORT
    except:
        pass

elif enviroment == Enviroment.ONDEV:

    PORT = config.DEVELOPMENT_PORT
    DB_NAME = config.ONDEV_DB_NAME
    DB_USER = config.ONDEV_USER
    DB_HOST = config.ONDEV_HOST
    DB_PASSWORD = config.ONDEV_PASSWORD

    try:
        DB_PORT = config.ONDEV_DB_PORT
    except:
        pass

elif enviroment == Enviroment.ONTEST:

    PORT = config.TESTING_PORT
    DB_NAME = config.ONTEST_DB_NAME
    DB_USER = config.ONTEST_USER
    DB_HOST = config.ONTEST_HOST
    DB_PASSWORD = config.ONTEST_PASSWORD
    try:
        DB_PORT = config.ONTEST_DB_PORT
    except:
        pass

else:

    PORT = config.PRODUCTION_PORT
    DB_NAME = config.PRODUCTION_DB_NAME
    DB_USER = config.PRODUCTION_USER
    DB_HOST = config.PRODUCTION_HOST
    DB_PASSWORD = config.PRODUCTION_PASSWORD

    try:
        DB_PORT = config.PRODUCTION_DB_PORT
    except:
        pass


def getConfig(**kwargs):
    """
    args:
    local="local config"
    ondev="ondev config"
    test="test config"
    prod="production config"
    """

    if enviroment == Enviroment.LOCAL:
        return kwargs["local"]
    elif enviroment == Enviroment.ONDEV:
        return kwargs["ondev"]
    elif enviroment == Enviroment.ONTEST:
        return kwargs["ontest"]
    elif enviroment == Enviroment.PRODUCTION:
        return kwargs["prod"]
    elif enviroment == Enviroment.DESIGNER:
        return kwargs["design"]


def send_message(message, system="loadingplay"):
    EmailReport.sendEmail(
        "ricardo.silva.16761@gmail.com",
        "error en : {}".format(system),
        message )


def report(message, system="loadingplay"):

    try:
        message = "{} | traceback: {}".format(
            message, 
            traceback.format_stack())
    except:
        pass

    if enviroment == Enviroment.LOCAL:
        print "\033[91m{}\033[0m".format(message)
    elif enviroment == Enviroment.ONDEV:
        try:
            print message
        except:
            send_message(message, system)
        # send_message(message, system)
    elif enviroment == Enviroment.PRODUCTION:
        send_message(message, system)


def encode(sstr):
    if type(sstr) == unicode:
        return sstr.encode("UTF-8")
    return sstr


print "port : {}".format(PORT)
