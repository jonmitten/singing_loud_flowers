"""
Deploy to Pi Zeros with:
ansible-playbook -i inventory.ini test_python_gpio.yml
"""
import RPi.GPIO as GPIO
import time

led_test_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led_test_pin,GPIO.OUT)

for i in range(10):
  print("LED on")
  GPIO.output(led_test_pin,GPIO.HIGH)
  time.sleep(.1)
  print("LED off")
  GPIO.output(led_test_pin,GPIO.LOW)
  time.sleep(.1)