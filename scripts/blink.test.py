import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led_test_pin = 18
GPIO.setup(led_test_pin, GPIO.OUT)

GPIO.setwarnings(False)


def blink(blinks=10, sleep_time=0.05):
  for i in range(blinks):
    print("LED on")
    GPIO.output(led_test_pin, GPIO.HIGH)
    time.sleep(sleep_time)
    print("LED off")
    GPIO.output(led_test_pin, GPIO.LOW)
    time.sleep(sleep_time)


GPIO.cleanup()