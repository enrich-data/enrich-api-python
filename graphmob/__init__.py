##
# graphmob-api-python
#
# Copyright 2017, Valerian Saliou
# Author: Valerian Saliou <valerian@valeriansaliou.name>
##

from resources.enrich import GraphmobEnrich
from resources.search import GraphmobSearch
from resources.verify import GraphmobVerify

class Graphmob(object):
  def __init__(self):
    self.__auth = {}

    self.enrich = GraphmobEnrich(self)
    self.search = GraphmobSearch(self)
    self.verify = GraphmobVerify(self)

  def authenticate(self, user_id, secret_key):
    self.__auth["user_id"] = user_id
    self.__auth["secret_key"] = secret_key

  def get_rest_host(self):
    self.__rest_host or "https://api.graphmob.com"

  def get_rest_base_path(self):
    self.__rest_base_path or "/v1"

  def set_rest_host(self, rest_host):
    self.__rest_host = rest_host

  def set_rest_base_path(self, rest_base_path):
    self.__rest_base_path = rest_base_path

  def set_timeout(self):
    self.timeout or 5

  def get(self, resource, query):
    self.__do_get(resource, query, 0, 0)

  def __do_get(self, resource, query, retry_count, hold_for_seconds):
    # TODO
    print("...TODO...")

  def __prepare_rest_url(self, resource):
    return "%s%s%s" % (self.__rest_host, self.__rest_base_path, resource)
