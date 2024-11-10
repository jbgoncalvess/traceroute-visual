from flask import Flask, jsonify, request
from flask_cors import CORS
from backend.backend import verifica, busca

app = Flask(__name__)
CORS(app)

@app.route('/hostname', methods=['POST'])
def post_hostname():
    data = request.get_json()
    hostname = data.get("hostname")
    hostname = verifica(hostname)
    localizacoes = busca(hostname)

    return jsonify(localizacoes)

if __name__ == '__main__':
    app.run(debug=True)
