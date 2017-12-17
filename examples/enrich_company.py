##
# enrich-api-python
#
# Copyright 2017, Valerian Saliou
# Author: Valerian Saliou <valerian@valeriansaliou.name>
##

from enrich_api import Enrich

client = Enrich()

client.authenticate(
  "ui_a311da78-6b89-459c-8028-b331efab20d5",
  "sk_f293d44f-675d-4cb1-9c78-52b8a9af0df2"
)

data = client.enrich.company({
  "name": "Crisp IM"
})

print(data)
