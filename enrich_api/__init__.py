##
# enrich-api-python
#
# Copyright 2017, Valerian Saliou
# Author: Valerian Saliou <valerian@valeriansaliou.name>
##

import json
from urllib import request, parse, error
from base64 import b64encode as b64

from .resources.enrich import EnrichResource
from .resources.verify import VerifyResource

class Enrich(object):
  NOT_FOUND_STATUS_CODE = 404

  def __init__(self):
    self.__auth = {}

    self.__rest_host = None
    self.__rest_base_path = None
    self.__timeout = None

    self.enrich = EnrichResource(self)
    self.verify = VerifyResource(self)

  def authenticate(self, user_id, secret_key):
    self.__auth["user_id"] = user_id
    self.__auth["secret_key"] = secret_key

  def get_rest_host(self):
    return self.__rest_host or "https://api.enrich.email"

  def get_rest_base_path(self):
    return self.__rest_base_path or "/v1"

  def get_timeout(self):
    return self.__timeout or 40

  def set_rest_host(self, rest_host):
    self.__rest_host = rest_host

  def set_rest_base_path(self, rest_base_path):
    self.__rest_base_path = rest_base_path

  def set_timeout(self, timeout):
    self.__timeout = timeout

  def get(self, resource, query):
    return self.__do_get(resource, query)

  def __do_get(self, resource, query):
    url = "%s?%s" % (self.__prepare_rest_url(resource), parse.urlencode(query))

    headers = {
      "User-Agent": "enrich-api-python/2.0.0",
      "Authorization": self.__generate_auth()
    }

    req = request.Request(url, None, headers)

    try:
      with request.urlopen(req, None, self.get_timeout()) as response:
        data = response.read()
        status = response.code
        raised_error = None
    except error.HTTPError as e:
      data = None
      status = e.code
      response = None

      # Consider 'Not Found' as a 'normal' error
      raised_error = None if status == self.NOT_FOUND_STATUS_CODE else e

    # Raise intercepted error?
    if raised_error:
      raise raised_error

    return json.loads(data) if data else None

  def __generate_auth(self):
    raw = "%s:%s" % (self.__auth["user_id"], self.__auth["secret_key"])
    key = b64(raw.encode("ascii"))

    return "Basic %s" % key.decode("ascii")

  def __prepare_rest_url(self, resource):
    return self.get_rest_host() + self.get_rest_base_path() + resource
