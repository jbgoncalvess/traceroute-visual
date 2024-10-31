import geoip2.webservice
import geoip2.errors

def get_lat_lon(ip):
    conta_ID = 913514
    chave_API = "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"

    try:
        with geoip2.webservice.Client(conta_ID, chave_API) as cliente:

            response = cliente.city(ip)
            if  response.city.name:
                #print(response)
                #dados_loc = ({'city': (response.city.name), 'lat': (response.location.latitude), 'lon': (response.location.longitude)})
                # print(dados_loc)
                #return dados_loc
                return response
    except geoip2.errors.AddressNotFoundError:
        pass

    return {}
                # print(response.country.names["pt-BR"])
                # print(response.city.names["pt-BR"])
                # print(response.location.latitude)
                # print(response.location.longitude)
                # print(response.traits.network)

#get_lat_lon('8.8.8.8')