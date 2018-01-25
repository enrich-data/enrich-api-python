##
# enrich-api-python
#
# Copyright 2017, Valerian Saliou
# Author: Valerian Saliou <valerian@valeriansaliou.name>
##

class SearchResource(object):
  def __init__(self, parent):
    self.parent = parent

  def lookup_people(self, query, page_number=1):
    return self.parent.get("/search/lookup/people/%d" % page_number, query)

  def lookup_companies(self, query, page_number=1):
    return self.parent.get("/search/lookup/companies/%d" % page_number, query)

  def lookup_emails(self, query, page_number=1):
    return self.parent.get("/search/lookup/emails/%d" % page_number, query)

  def suggest_companies(self, query, page_number=1):
    return self.parent.get("/search/suggest/companies/%d" % page_number, query)
