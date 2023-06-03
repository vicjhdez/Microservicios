from flask import Flask, request, jsonify
from flask_cors import CORS  # Importa flask_cors
import requests

app = Flask(__name__)
CORS(app)  # Habilita las solicitudes CORS de cualquier origen

@app.route('/api/<service>', methods=['GET'])
def proxy(service):
    if service == "shoes":
        res = requests.get('http://shoe')  # Deberías reemplazar esto con la URL del microservicio de shoe
    elif service == "offers":
        res = requests.get('http://offers')  # Deberías reemplazar esto con la URL del microservicio de offers
    else:
        return jsonify({"error": "Unknown service"}), 400
    return res.json()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9999)
