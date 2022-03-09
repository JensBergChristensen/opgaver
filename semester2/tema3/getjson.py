import random
import json
from paho.mqtt import client as mqtt_client


broker = 'eu1.cloud.thethings.network'
port = 1883
topic = "#"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = 'skoleopgavetestgps42069@ttn'
password = 'NNSXS.XBCHKF5TZ2KKNDS233NV6IS4RIRDHYIF3TDWOWQ.UMMEQPJX32QC27466MWI6OMBQJ2BKXH424Y7OJEDLDLG7MEQS6KA'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        #print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        try:
            #print(msg.payload)
            x = json.loads(msg.payload.decode('utf-8'))
            print("test print: ", x["uplink_message"]["decoded_payload"]["info"])
        except Exception as e:
            print(e)
            pass
    client.subscribe(topic)
    client.on_message = on_message



def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
