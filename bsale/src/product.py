#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests

class Product():
    """docstring for Product"""

    def test(self):
        print "llega"

    def Get(self):

        # require 'net/http'
        # require 'openssl'
        # require 'json'

        # url = 'https://api.bsale.cl/v1/clients.json'
        # uri = URI.parse(url)
        # http = Net::HTTP.new(uri.host, uri.port)

        # # Activa SSL
        # http.use_ssl = true
        # http.verify_mode = OpenSSL::SSL::VERIFY_NONE

        # request = Net::HTTP::Get.new(uri.request_uri)

        # # Configura cabeceras
        # request['Content-Type'] = 'application/json'
        # request['access_token'] = 'tu token de acceso'
        # response = http.request(request)
        # respuesta = JSON.parse(response.body)
        url = 'https://api.bsale.cl/v1/clients.json'

        r = requests.get(url)

        return r.json()

