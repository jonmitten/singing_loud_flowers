import RPi.GPIO as gpio
import time
import datetime
import paho.mqtt.client as mqtt
import socket

HOSTNAME = socket.getfqdn()

# Set up the GPIO pins
gpio.setmode(gpio.BCM)  # Use BCM numbering
test_pir_pin = 14
test_led_pin = 18
gpio.setup(test_pir_pin, gpio.IN)  # Set test_pir_pin as input
gpio.setup(test_led_pin, gpio.OUT)

# MQTT Pub/Sub Config
MQTT_BROKER = "192.168.1.55"  # rpi5
MQTT_PORT = 1883
MQTT_TOPIC = "singing_loud_flowers"
MQTT_MESSAGE = f"motion detected on {HOSTNAME}"
print(f"I am: {HOSTNAME}")

# MQTT client setup
client = mqtt.Client()


def on_connect(client, userdata, flags, rc):
  print("Connected with result code " + str(rc))
  client.subscribe(MQTT_TOPIC)


def on_message(client, userdata, msg):
  if msg.payload.decode().find(HOSTNAME) == -1:
    print(f"Message received: {msg.payload.decode()}")
    print('blink on_message')
    print(f"I am {HOSTNAME}")
    blink(10, .1)
  else:
    print(f"I'm reporting on my own sensor finding :(")


client.on_connect = on_connect
client.on_message = on_message

try:
  client.connect(MQTT_BROKER, MQTT_PORT, 60)
  client.loop_start()  # start the MQTT client loop

except Exception as e:
  print(f"Error connecting to MQTT broker: {e}")
  gpio.cleanup()
  exit(1)


def blink(times: int = 10, frequency: float = 1.0):
  """
    LED indicator of motion detection.
    Should coincide with MQTT publication
    """
  print(f"enter blink: {times} and {frequency}")
  for i in range(times):
    print("LED on")
    gpio.output(test_led_pin, gpio.HIGH)
    time.sleep(frequency)
    print("LED off")
    gpio.output(test_led_pin, gpio.LOW)
    time.sleep(frequency)
  return None


def motion_detected(channel):
  """
    Run on motion detect.
    """
  try:
    client.publish(MQTT_TOPIC, MQTT_MESSAGE)
    print("motion detection published")
  except Exception as e:
    print(f"Error publishing MQTT message: {e}")
  print(f"Motion detected on {HOSTNAME}!")
  print(datetime.datetime.now())
  print('blink motion detected')
  blink(2, 1.0)


try:
  # Add event detection for a falling edge on pin 14 and link it to the callback function
  gpio.add_event_detect(test_pir_pin, gpio.FALLING, callback=motion_detected, bouncetime=300)
  # Keep the script running to detect motion
  while True:
    time.sleep(1)
    if test_led_pin == gpio.HIGH:
      print(f"{test_led_pin} is HIGH")
    elif test_led_pin == gpio.LOW:
      print(f"{test_led_pin} is LOW")
except KeyboardInterrupt:
  print("Exiting program")
except Exception as e:
  print(f"An error occurred: {e}")
finally:
  # Clean up GPIO settings before exiting
  print('cleaning up')
  gpio.cleanup()
  print('stopping loop')
  client.loop_stop()
  print('disconnecting')
  client.disconnect()
