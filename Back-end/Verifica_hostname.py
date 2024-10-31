import ipaddress

def verifica(hostname):
    try:
        ipaddress.IPv4Address(hostname)
    except:
        if not hostname.startswith("www."):
            hostname = "www."+hostname

    return hostname