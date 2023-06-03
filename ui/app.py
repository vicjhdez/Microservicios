from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shoes')
def get_shoes():
    shoe_service_url = 'http://shoe:1001/'
    response = requests.get(shoe_service_url)
    shoes = response.json()
    return jsonify(shoes)

@app.route('/offers')
def get_offers():
    offers_service_url = 'http://offers:1002/'
    response = requests.get(offers_service_url)
    offers = response.json()
    return jsonify(offers)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
