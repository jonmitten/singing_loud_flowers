import RPi.GPIO as gpio
import time
import paho.mqtt.client as mqtt
import socket

test_button_pin = 27
print(socket.getfqdn())
# MQTT setup
MQTT_BROKER = "192.168.1.55"
MQTT_PORT = 1883
MQTT_TOPIC = "singing_loud_flowers"
MQTT_MESSAGE = "Button was pressed!"

# Set up GPIO mode
gpio.setmode(gpio.BCM)

# Set up GPIO pin 27 as an input with a pull-up resistor
gpio.setup(test_button_pin, gpio.IN, pull_up_down=gpio.PUD_UP)


def button_callback(channel):
  print("Button was pressed!")
  client.publish(MQTT_TOPIC, MQTT_MESSAGE)


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
client.connect(MQTT_BROKER, MQTT_PORT, 60)

try:
  # Keep the script running to detect button presses
  while True:
    time.sleep(1)
except KeyboardInterrupt:
  print("Exiting program")

# Clean up GPIO settings before exiting
gpio.cleanup()
