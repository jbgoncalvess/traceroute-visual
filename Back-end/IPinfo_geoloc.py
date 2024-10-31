import requests

def get_lat_long(ip_address, loc_anterior):
    api_key = "fee63210f68755"  # Minha chave de API - "TROCAR"
    url = f"https://ipinfo.io/{ip_address}/json?token={api_key}"  # URL do serviço de geocodificação
    response = requests.get(url)  # Faça a solicitação HTTP com a bib requests

    if response.status_code == 200:  # Se solicitação HTTP foi bem sucedida, verificação
        data = response.json()  # Passa os dados (.json) da página para o meu código
        if 'bogon' not in data and loc_anterior != data["loc"]: # Comparo com anterior que recebo como parâmetro já formatado
            if data['ip'] == '200.18.74.1':
                return [-29.6842, -53.8069, 'Santa Maria']      # Tratando erro de 'Rio grande' 'SM'
            # print(data)
            print(data["loc"])
            return [float(data["loc"].split(",")[0]), float(data["loc"].split(",")[1]), data["city"]]   # Agora, já retorno formatado

        return []  #Retorna lista vazia, já que preciso retornar algo

    else:
        print("Erro ao obter informações geográficas")


#get_lat_long("101.100.100.100") #- Testando a função