import paho.mqtt.client as mqtt
import json
import random
import time

broker = "test.mosquitto.org"
topic = "iot/fake_data"

client = mqtt.Client("Fake_IoT_Device")

def generate_data():
    return {
        "device_id": f"sensor_{random.randin(1, 5)}",
        "temperature": round(random.uniform(18, 28), 2),
        "humidity": round(random.uniform(40, 60), 2)
    }

client.connect(broker)

while True:
    data = json.dumps(generate_data())
    client.publish(topic, data)
    print(f"Published data: {data}")
    time.sleep(2)