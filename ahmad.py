import paho.mqtt.client as mqtt
import json
import time
import random

# broker parameters
broker_address = "localhost"
broker_port = 1883
topic = "iot/sensor-data"

# Create MQTT client 
client = mqtt.Client()

# Connect to MQTT broker
client.connect(broker_address, broker_port)

# Send simulated data to MQTT broker
while True:
    data = {
        "sensor_id": "sensor1",
        "value": random.randint(1, 100),
        "timestamp": time.time()
    }
    message = json.dumps(data)
    client.publish(topic, message)
    time.sleep(1)
