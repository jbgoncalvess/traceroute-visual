""" Pingando para fora """

def busca(ping):
    from scapy.all import IP, ICMP, sr1  # Importar com "from" para não ter que usar scapy.all.  ...
    from IPinfo_geoloc import get_lat_long
    from Construcao_map import map

    ttl_limit = 30  # Define um limite máximo de TTL para evitar loops infinitos
    ip_anterior = 0  # Valor inicial para fazer a comparação
    caminho_geral = []  #Onde estão os dados do data, sem casts e diversos
    localizacoes=[] #Dicionário com os dados com chave e valor certinho pra "Construcao_map - map"

    for ttl in range(1, ttl_limit + 1):

        packet = IP(dst=ping, ttl=ttl) / ICMP()  # Enviando echo_request
        response = sr1(packet, verbose=0, timeout=1)  # Pacote e tempo limite

        if response and ip_anterior == response.src:  # NÃO FICAR MOSTRANDO O MESMO IP, se "ip_anterior == resposta nova", sai do laço.
            break

        if response:
            #print('TTL: {} -- IP: {}'.format(ttl, response.src))  # TTL e IPv4 do salto
            caminho_geral.append(get_lat_long(response.src))  # Se o IPv4 é válido, chamo o IPinfo e pego o data(conjunto de info)
            ip_anterior = response.src  # Para não repetir o IP, após chegar na rede desejada, armazeno a ultima resposta para comparar

    for dados_local in caminho_geral:   # Dados local é cada página do meu dicionário
        if 'bogon' not in dados_local:
            #print("IP:", dados_local["ip"])
            localizacoes.append({"ip": dados_local["ip"], "lat": float(dados_local["loc"].split(",")[0]), "lon": float(dados_local["loc"].split(",")[1])})

    #print(localizacoes) #Teste
    #print(localizacoes[1]["lat"])   #Teste

    map(localizacoes)

    #Cada página do meu dicionário deve ficar assim:     "ip": "192.168.1.1", "lat": 37.7749, "lon": -122.4194