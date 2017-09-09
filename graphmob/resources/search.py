##
# graphmob-api-python
#
# Copyright 2017, Valerian Saliou
# Author: Valerian Saliou <valerian@valeriansaliou.name>
##

class GraphmobSearch(object):
  def __init__(self, parent):
    self.parent = parent

  def lookup_companies(query, page_number=1):
    return self.get("/search/lookup/companies/%d" % page_number, query)

  def lookup_emails(query, page_number=1):
    return self.get("/search/lookup/emails/%d" % page_number, query)

  def suggest_companies(query, page_number=1):
    return self.get("/search/suggest/companies/%d" % page_number, query)
