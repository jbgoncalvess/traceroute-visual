import geoip2.webservice

conta_ID = 913514
chave_API = "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"

with geoip2.webservice.Client(conta_ID, chave_API) as cliente:


