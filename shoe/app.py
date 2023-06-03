from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def shoe_list():
    shoes = [
        {"id": 1, "name": "Air Jordan", "brand": "Nike"},
        {"id": 2, "name": "Yeezy Boost", "brand": "Adidas"},
        {"id": 3, "name": "Classic Leather", "brand": "Reebok"},
        # etc...
    ]
    return jsonify(shoes)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1001)
