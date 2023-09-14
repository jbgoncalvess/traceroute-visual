import requests

def get_lat_long(ip_address):
    api_key = "fee63210f68755"  # Minha chave de API - "TROCAR"

    url = f"https://ipinfo.io/{ip_address}/json?token={api_key}"  # URL do serviço de geocodificação

    response = requests.get(url)  # Faça a solicitação HTTP com a bib requests

    barra = "\033[91m" + "="  # Vermelho
   # print("{}".format(barra), end="") # Usuário saber que não travou (Carregando)

    if response.status_code == 200:  # Se solicitação HTTP foi bem sucedida, verificação
        data = response.json()  # Passa os dados (.json) da página para o meu código
        return data  #Retorna o "data", que é um dado que contém várias informações. EX = cidade, ip, país
        '''if 'bogon' not in data:
            # Exiba os dados geográficos
            print("IP:", data["ip"])
            print("Cidade:", data["city"])
            print("Região:", data["region"])    # Dados que eu posso puxar do json
            print("País:", data["country"])
            print("Latitude:", data["loc"].split(",")[0])
            print("Longitude:", data["loc"].split(",")[1])'''
    else:
        print("Erro ao obter informações geográficas")

#get_lat_long("8.8.8.8") #- Testando a função