""" Pingando para fora """

def busca(ping):
    from scapy.all import IP, ICMP, sr1  # Importar com "from" para não ter que usar scapy.all.  ...
    from IPinfo_geoloc import get_lat_long
    from GeoIP2 import get_lat_lon

    ttl_limit = 30  # Define um limite máximo de TTL para evitar loops infinitos
    ip_anterior = 0  # Valor inicial para fazer a comparação
    caminho_geral = []  #Onde estão os dados do data, sem casts e diversos
    localizacoes=[] #Dicionário com os dados com chave e valor certinho pra "Construcao_map - map"
    dados_formatados = []
    localizacoes_geo = []
    loc_anterior = {}

    if not localizacoes:
        localizacoes = [[-29.72496799019496, -53.71152216125474, 'CE'],
                        [-29.71185254678608, -53.71825797209584, "Redes CTISM"],
                        [-29.720899943160862, -53.71377175917256, 'CPD UFSM']
                        ]


    for ttl in range(1, ttl_limit + 1):

        packet = IP(dst=ping, ttl=ttl) / ICMP()  # Enviando echo_request
        response = sr1(packet, verbose=0, timeout=1)  # Pacote e tempo limite

        if response and ip_anterior == response.src:  # NÃO FICAR MOSTRANDO O MESMO IP, se "ip_anterior == resposta nova", sai do laço.
            break

        if response:
            #print('TTL: {} -- IP: {}'.format(ttl, response.src))  # TTL e IPv4 do salto
            #dados_formatados.append(get_lat_lon(response.src)) # GeoIP2
            caminho_geral.append(get_lat_long(response.src, loc_anterior))  # Se o IPv4 é válido, chamo o IPinfo e pego o data(conjunto de info)
            #print(caminho_geral)
            #loc_anterior = {'loc': {str(caminho_geral[-1])} }
            if caminho_geral[-1]:
                localizacoes.append(caminho_geral[-1])  # Tratando listas vazias
                loc_anterior = "{:.4f},{:.4f}".format((localizacoes[-1][0]), (localizacoes[-1][1])) # Posição anterior já formatada, passada por parâmetro
                print('teste')
                print(loc_anterior)
                #print(localizacoes)
            ip_anterior = response.src  # Para não repetir o IP, após chegar na rede desejada, armazeno a ultima resposta para comparar
    # for dados_local in caminho_geral:   # Tratar Dados de listas vazias
    #     if dados_local:
    #         localizacoes.append(dados_local)

    print(localizacoes)
    return localizacoes

    #map(localizacoes)

    #Cada página do meu dicionário deve ficar assim:     "ip": "192.168.1.1", "lat": 37.7749, "lon": -122.4194