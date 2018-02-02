##
# enrich-api-python
#
# Copyright 2017, Valerian Saliou
# Author: Valerian Saliou <valerian@valeriansaliou.name>
##

class VerifyResource(object):
  def __init__(self, parent):
    self.parent = parent

  def validate_email(self, query):
    return self.parent.get("/verify/validate/email", query)
