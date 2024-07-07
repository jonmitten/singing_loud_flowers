import RPi.GPIO as gpio
import time
import paho.mqtt.client as mqtt
import socket

test_button_pin = 27
test_led_pin = 18
print(socket.getfqdn())
# MQTT setup
MQTT_BROKER = "192.168.1.55"
MQTT_PORT = 1883
MQTT_TOPIC = "singing_loud_flowers"
MQTT_MESSAGE = "MQTT Pub Sub Button Test!"

# Set up GPIO mode
gpio.setmode(gpio.BCM)

# Set up GPIO pin 27 as an input with a pull-up resistor
gpio.setup(test_button_pin, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(test_led_pin, gpio.OUT)


# Define callback functions
def button_callback(channel):
  print("Button was pressed!")
  print(f"publishing {MQTT_MESSAGE} to {MQTT_TOPIC} on {MQTT_BROKER}")
  client.publish(MQTT_TOPIC, MQTT_MESSAGE)
  print('This is a edge event callback function!')
  print('Edge detected on channel %s' % channel)
  print('This is run in a different thread to your main program')


def on_connect(client, userdata, flags, rc):
  print(f"Connected with result code {rc}")
  client.subscribe(MQTT_TOPIC)


def on_message(client, userdata, msg):
  print(f"Message received: {msg.topic} {msg.payload.decode()}")
  
  for i in range(3):
    print("LED on")
    gpio.output(test_led_pin, gpio.HIGH)
    time.sleep(.5)
    print("LED off")
    gpio.output(test_led_pin, gpio.LOW)
    time.sleep(.5)


# Add event detection for a falling edge on pin 27 and link it to the callback function
gpio.add_event_detect(
  test_button_pin,
  gpio.FALLING,
  callback=button_callback,
  bouncetime=300
)

print("Button press detector running. Press the button to test.")

# MQTT client setup
client = mqtt.Client()
# Assign the callback functions
client.on_connect = on_connect
client.on_message = on_message

try:
  # Keep the script running to detect button presses
  while True:
    time.sleep(1)
except KeyboardInterrupt:
  print("Exiting program")

# Clean up GPIO settings before exiting
gpio.cleanup()
