import paho.mqtt.client as mqtt
import time

BROKER = "mosquitto"
TOPIC = "devices/status"

def on_connect(client, userdata, flags, rc):
    print("Device Manager connected to broker")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print(f"Device Manager received: {msg.topic} {msg.payload.decode()}")
    # Invia una risposta ai dispositivi
    client.publish("devices/response", f"Acknowledged message from {msg.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, 1883, 60)

client.loop_start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    client.loop_stop()
