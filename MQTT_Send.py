import serial
import time
import random

from paho.mqtt import client as mqtt_client

ser = serial.Serial('COM4',9600)
ser.flushInput()

broker = 'broker.emqx.io'
port = 1883
topic = "dandelion"

client_id = f'python-mqtt-{random.randint(0, 1000)}'
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client):
    while True:
        time.sleep(3)
        ser_bytes = ser.readline()
        msg = str(ser_bytes.decode("utf-8")).replace("\r\n","")
        result = client.publish(topic, msg)
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()
