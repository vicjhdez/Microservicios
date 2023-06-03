from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def offer_list():
    offers = [
        {"shoe_id": 1, "discount": "20%", "expiry": "2023-06-30"},
        {"shoe_id": 2, "discount": "15%", "expiry": "2023-06-20"},
        # etc...
    ]
    return jsonify(offers)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1002)
