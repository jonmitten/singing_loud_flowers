"""
Deploy to Pi Zeros with:
ansible-playbook -i inventory.ini test_python_gpio.yml
"""
import RPi.GPIO as gpio
import time

led_test_pin = 18

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(led_test_pin, gpio.OUT)

for i in range(10):
  print("LED on")
  gpio.output(led_test_pin, gpio.HIGH)
  time.sleep(.1)
  print("LED off")
  gpio.output(led_test_pin, gpio.LOW)
  time.sleep(.1)
gpio.cleanup()