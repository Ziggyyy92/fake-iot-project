from flask import Flask, jsonify
from data_generator import generate_fake_temperature_data

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    data = generate_fake_temperature_data(10).to_dict(orient='records')
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
