import ipaddress
import geoip2.webservice
import requests
from scapy.all import IP, ICMP, sr1

# Função para verificar e ajustar o hostname
def verifica(hostname):
    try:
        ipaddress.IPv4Address(hostname)
    except:
        if not hostname.startswith("www."):
            hostname = "www." + hostname
    return hostname

# Função para obter localização com GeoIP2
def get_lat_lon(ip):
    conta_ID = 913514
    chave_API = "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"

    try:
        with geoip2.webservice.Client(conta_ID, chave_API) as cliente:
            response = cliente.city(ip)
            if response.city.name:
                return response
    except geoip2.errors.AddressNotFoundError:
        pass

    return {}

# Função para obter localização com IPinfo
def get_lat_long(ip_address, loc_anterior):
    api_key = "fee63210f68755"
    url = f"https://ipinfo.io/{ip_address}/json?token={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if 'bogon' not in data and loc_anterior != data["loc"]:
            return [float(data["loc"].split(",")[0]), float(data["loc"].split(",")[1]), data["city"]]
    return []

# Função para rastrear rota de pacotes e obter localização
def busca(ping):
    ttl_limit = 30
    ip_anterior = 0
    caminho_geral = []
    localizacoes = []
    loc_anterior = {}

    for ttl in range(1, ttl_limit + 1):
        packet = IP(dst=ping, ttl=ttl) / ICMP()
        response = sr1(packet, verbose=0, timeout=1)

        if response and ip_anterior == response.src:
            break

        if response:
            caminho_geral.append(get_lat_long(response.src, loc_anterior))
            if caminho_geral[-1]:
                localizacoes.append(caminho_geral[-1])
                loc_anterior = "{:.4f},{:.4f}".format(localizacoes[-1][0], localizacoes[-1][1])
            ip_anterior = response.src

    return localizacoes
