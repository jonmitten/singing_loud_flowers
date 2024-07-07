import paho.mqtt.client as mqtt
broker = '192.168.1.55'
port = 1883
topic = "test/topic"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(topic)

def led_message_received(client, userdata, msg):
  pass

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    # Here you can call any function based on the message received
    

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port, 60)
client.loop_forever()
