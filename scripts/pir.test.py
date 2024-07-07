import RPi.GPIO as gpio
import time
import datetime

# Set up the GPIO pin
test_pir_pin = 14
test_led_pin = 18
test_button_pin = 17

# Configure GPIO settings
gpio.setmode(gpio.BCM)  # Use BCM numbering

# Setup pins
gpio.setup(test_pir_pin, gpio.IN)  # Set test_pir_pin as input
gpio.setup(test_led_pin, gpio.OUT)
gpio.setup(test_button_pin, gpio.IN)

gpio.setwarnings(False)


def motion_detected(channel):
  """
  Run on motion detect.
  :param channel:
  :return:
  """
  print("Motion detected!")
  print(datetime.datetime.now())
  for i in range(10):
    print("LED on")
    gpio.output(test_led_pin, gpio.HIGH)
    time.sleep(.1)
    print("LED off")
    gpio.output(test_led_pin, gpio.LOW)
    time.sleep(.1)
  return None


def button_pressed(channel):
  """
  Run on button press.
  :param channel:
  :return:
  """
  print("Button pressed!")
  print(datetime.datetime.now())
  for i in range(2):
    print("LED on")
    gpio.output(test_led_pin, gpio.HIGH)
    time.sleep(.1)
    print("LED off")
    gpio.output(test_led_pin, gpio.LOW)
    time.sleep(.1)
  return None


# Add event detection on the PIR sensor pin
gpio.add_event_detect(
  test_pir_pin,
  gpio.RISING,
  callback=motion_detected
)

gpio.add_event_detect(
  test_button_pin,
  gpio.RISING,
  callback=button_pressed
)

try:
  print("PIR Sensor Test (Press CTRL+C to exit)")
  while True:
    time.sleep(1)  # Loop indefinitely

except KeyboardInterrupt:
  print("Quit")

finally:
  gpio.cleanup()  # Reset GPIO settings
