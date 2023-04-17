import paho.mqtt.client as mqtt
import json
import requests

# FlexMeasures API parameters
flexmeasures_url = "http://localhost:5000"
username = "toy-user@flexmeasures.io"
password = "toy-password"

# MQTT broker parameters
broker_address = "localhost"
broker_port = 1883
topic = "iot/sensor-data"

# Authentication of FlexMeasures
auth = (username, password)

# Callback function to handle incoming MQTT messages
def on_message(client, userdata, message):
    # Parse incoming message
    payload = message.payload.decode()
    data = json.loads(payload)
    
    # Create sensor-data in FlexMeasures
    sensor_data = {
        "sensor_id": data["sensor_id"],
        "value": data["value"],
        "timestamp": data["timestamp"]
    }
    response = requests.post(flexmeasures_url + "sensor-data", json=sensor_data, auth=auth)
    if response.status_code == 201:
        print("Sensor data created successfully")
    else:
        print("Error creating sensor data:", response.text)

# MQTT client instance
client = mqtt.Client()

# Connect to MQTT broker
client.connect(broker_address, broker_port)

# Subscribe to MQTT topic
client.subscribe(topic)

# Set callback function for incoming MQTT messages
client.on_message = on_message

# Start MQTT client loop
client.loop_forever()
