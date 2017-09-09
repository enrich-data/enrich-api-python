##
# graphmob-api-python
#
# Copyright 2017, Valerian Saliou
# Author: Valerian Saliou <valerian@valeriansaliou.name>
##

class GraphmobVerify(object):
  def __init__(self, parent):
    self.parent = parent

  def validate_email(self, query):
    return self.parent.get("/verify/validate/email", query)

  def format_email(self, query):
    return self.parent.get("/verify/format/email", query)
