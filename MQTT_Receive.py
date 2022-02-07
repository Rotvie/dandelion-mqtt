import random
from paho.mqtt import client as mqtt_client
#from datetime import datetime 
import csv 


broker = 'broker.emqx.io'
port = 1883
topic = "dandelion"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'



def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"{msg.payload.decode()}")
        txt = msg.payload.decode().split(", ")
        with open('Humedad.csv','a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([txt[0]])
        with open('Temperatura.csv','a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([txt[1]])

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    while True:
        subscribe(client)
        client.loop_start()

if __name__ == '__main__':
    run()
