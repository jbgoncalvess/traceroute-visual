import requests

def get_data(ip_address):
    pass


def get_lat_long(ip_address):
    api_key = "fee63210f68755"  # Minha chave de API - "TROCAR"

    url = f"https://ipinfo.io/{ip_address}/json?token={api_key}"  # URL do serviço de geocodificação

    response = requests.get(url)  # Faça a solicitação HTTP com a bib requests

    if response.status_code == 200:  # Se solicitação HTTP foi bem sucedida, verificação
        data = response.json()  # Passa os dados (.json) da página para o meu código
        return data  #Retorna o "data", que é um dado que contém várias informações. EX = cidade, ip, país

    else:
        print("Erro ao obter informações geográficas")

#get_lat_long("8.8.8.8") #- Testando a função