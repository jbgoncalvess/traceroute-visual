from Rota_pacotes import busca
from flask import Flask, jsonify, request
from flask_cors import CORS
from Verifica_hostname import verifica
import ipaddress
app = Flask(__name__)
CORS(app)


# ip_dominio_desejado = input("Digite o ip ou domínio desejado:\n")
# print("CARREGANDO")
# localizacoes = busca(ip_dominio_desejado)


@app.route('/hostname', methods=['POST'])
def post_hostname():
    # Recebo os dados do
    #hostname = '8.8.8.8'
    hostname = request.get_json()
    hostname = verifica(hostname)

    print(hostname)
    #print(type(hostname))
    # print(hostname)  # teste
    # Chamo a o código do back logo que recebo os dados do cliente
    localizacoes = busca(hostname)
    # Já retorno as coordenadas e locais para o cliente
    return jsonify(localizacoes)




# @app.route('/dados', methods=['GET'])
# def get_cidades():
#     # Use os dados do cliente armazenados na variável global
#     print(hostname)
#     localizacoes = busca(hostname)
#     return jsonify(localizacoes)


# 3.115.220.200 JAPÃO
# 104.132.255.100 PORTUGAL
# 102.130.39.220 RUANDA
# 101.100.100.100 NOVA ZELANDIA
# 1.55.55.55 VIETNA
# 109.170.127.220 RUSSIA


# 170.79.214.36
# TTL: 8 -- IP: 170.79.213.121
# TTL: 9 -- IP: 170.79.213.229
