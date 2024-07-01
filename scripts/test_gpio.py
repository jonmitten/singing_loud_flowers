import RPi.GPIO as gpio
import time

# Set the gpio mode
gpio.setmode(gpio.BCM)

# List of all gpio pins on Raspberry Pi (excluding power and ground)
all_pins = [4, 5, 6, 12, 13, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]

# Callback function to handle events
def event_callback(channel):
    print(f"Event detected on pin: {channel}")

# Set up each pin with event detection
for pin in all_pins:
    gpio.setup(pin, gpio.IN, pull_up_down=gpio.PUD_DOWN)
    gpio.add_event_detect(pin, gpio.BOTH, callback=event_callback)

try:
    # Keep the script running to detect events
    print("Monitoring pins for events. Press Ctrl+C to exit.")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Exiting program")

# Clean up gpio settings
gpio.cleanup()
