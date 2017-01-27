#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import os
import urllib
import base64

from tornado.httpclient import HTTPClient
from lp.globals import report


class ImageClient(object):
    """
    client for upload images within static.loadingplay.com
    """

    def __init__(self):
        self._id = ""
        self._url = ""
        self._name = ""
        self._image = ""
        self._thumb_1 = ""
        self._thumb_200 = ""
        self._thumb_500 = ""

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._id = value

    @property
    def thumb_1(self):
        return self._thumb_1

    @thumb_1.setter
    def thumb_1(self, value):
        self._thumb_1 = value

    @property
    def thumb_200(self):
        return self._thumb_200

    @thumb_200.setter
    def thumb_200(self, value):
        self._thumb_200 = value

    @property
    def thumb_500(self):
        return self._thumb_500

    @thumb_500.setter
    def thumb_500(self, value):
        self._thumb_500 = value

    @staticmethod
    def initFromJSON(json_data):

        instance = ImageClient()

        instance._id = json_data["id"] if "id" in json_data else ""
        instance._url = json_data["url"] if "url" in json_data else ""
        instance._name = json_data["name"] if "name" in json_data else ""
        instance._image = json_data["image"] if "image" in json_data else ""
        instance._thumb_1 = json_data["thumb_1"] if "thumb_1" in json_data else ""
        instance._thumb_200 = json_data["thumb_200"] if "thumb_200" in json_data else ""
        instance._thumb_500 = json_data["thumb_500"] if "thumb_500" in json_data else ""

        return instance

    @staticmethod
    def uploadFromData(name, base64_body):
        instance = None
        extension = "png"

        try:
            splitted_name = name.split(".")
            if len(splitted_name) > 1:
                extension = splitted_name[1]

            json_data = ImageClient._uploadImage( 
                            name, 
                            extension, 
                            base64_body )

            # instantiate an Image with json
            instance = ImageClient()

            instance._id = json_data["id"]
            instance._url = json_data["url"]
            instance._name = json_data["name"]
            instance._image = json_data["image"]
            instance._thumb_1 = json_data["thumb_1"]
            instance._thumb_200 = json_data["thumb_200"]
            instance._thumb_500 = json_data["thumb_500"]

            return instance
        except Exception, ex:
            report("ImageClient->uploadFromData : {}".format(str(ex)))
            pass

    @staticmethod
    def uploadFromDisk(uri):
        """
        load image from disk, for the given uri
        """

        splitted_uri = None
        splitted_name = None
        image_name = None
        image_extension = None
        image_body = None
        instance = None

        try:

            # get file parameters
            splitted_uri = uri.split(os.sep)
            image_name = splitted_uri[len(splitted_uri)-1]
            splitted_name = image_name.split(".")
            image_extension = splitted_name[1]

            # load content from disk
            f = open( uri )
            image_body = f.read()
            f.close()

            if image_body is not None:

                # encode and upload
                base64_body = base64.b64encode(str(image_body))
                json_data = ImageClient._uploadImage( 
                                image_name, 
                                image_extension, 
                                base64_body )

                # instantiate an Image with json
                instance = ImageClient()

                instance._id = json_data["id"]
                instance._url = json_data["url"]
                instance._name = json_data["name"]
                instance._image = json_data["image"]
                instance._thumb_1 = json_data["thumb_1"]
                instance._thumb_200 = json_data["thumb_200"]
                instance._thumb_500 = json_data["thumb_500"]

                return instance
        except Exception, e:
            report("ImageClient->uploadFromDisk : {}".format(str(e)))
            pass

    @staticmethod
    def _uploadImage(name, extension, base64_body):
        client = HTTPClient()

        data = {
            "name" : name,
            "extension" : extension,
            "data" : base64_body
        }

        response = client.fetch(
                    "https://static.loadingplay.com/image/upload",
                    body=urllib.urlencode( data ),
                    method="POST")

        return json.loads(response.body)
