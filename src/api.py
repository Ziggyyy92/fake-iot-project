import eventlet
eventlet.monkey_patch() # Neophodno za SocketIO
from flask import Flask, jsonify, render_template
from flask_socketio import SocketIO, emit
import random
import datetime


app = Flask(__name__)
socketio = SocketIO(app) # Inicijalizacija SocketIO

# Skladistenje podataka u memoriju za simulaciju
device_data = []

@app.route('/api/data')
def get_data():
    """Endpoint za povlacenje svih trenutaka podataka."""
    return jsonify(device_data)

def generate_fake_data():
    """Simulira prikupljanje podataka sa IoT uredjaja."""
    while True:
        new_data = {
            "device_id": f"device_{random.randint(1, 5)}",
            "timestamp": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "temperature": round(random.uniform(20, 40), 2),
            "humidity": round(random.uniform(30, 80), 2)
        }
        device_data.append(new_data)

        # Emituje nove podatke svim povezanim klijentima putem WebSocket-a
        socketio.emit('new_data', new_data)

        # Ceka 3 sekunde pre generisanja novih podataka
        socketio.sleep(3)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Pokrece generisanje podataka u pozadini i server sa WebSocket podrskom
    socketio.start_background_task(generate_fake_data)
    socketio.run(app, host='0.0.0.0', port=5000)
