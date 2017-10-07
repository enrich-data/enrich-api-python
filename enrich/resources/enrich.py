##
# enrich-api-python
#
# Copyright 2017, Valerian Saliou
# Author: Valerian Saliou <valerian@valeriansaliou.name>
##

class EnrichResource(object):
  def __init__(self, parent):
    self.parent = parent

  def person(self, query):
    return self.parent.get("/enrich/person", query)

  def company(self, query):
    return self.parent.get("/enrich/company", query)

  def network(self, query):
    return self.parent.get("/enrich/network", query)
