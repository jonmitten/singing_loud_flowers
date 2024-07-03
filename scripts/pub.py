import paho.mqtt.client as mqtt

broker = '192.168.1.55'
port = 1883
topic = "test/topic"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.publish(topic, "Hello from Raspberry Pi!")

client = mqtt.Client()
client.on_connect = on_connect
client.connect(broker, port, 60)
client.loop_forever()
