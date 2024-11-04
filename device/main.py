import paho.mqtt.client as mqtt
import time
import os

BROKER = "mosquitto"
TOPIC = "devices/status"
DEVICE_ID = os.getenv("DEVICE_ID", "unknown_device")

def on_connect(client, userdata, flags, rc):
    print(f"{DEVICE_ID} connected to broker")
    client.subscribe("devices/response")

def on_message(client, userdata, msg):
    print(f"{DEVICE_ID} received response: {msg.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, 1883, 60)

client.loop_start()

try:
    while True:
        message = f"Status from {DEVICE_ID}"
        client.publish(TOPIC, message)
        print(f"{DEVICE_ID} sent: {message}")
        time.sleep(5)
except KeyboardInterrupt:
    client.loop_stop()
