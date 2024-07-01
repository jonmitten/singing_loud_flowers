import RPi.GPIO as gpio
import time

# Use BCM gpio references
gpio.setmode(gpio.BCM)

# Define the gpio pin to use
button_pin = 15

# Set up the gpio pin as an input with a pull-down resistor
gpio.setup(button_pin, gpio.IN, pull_up_down=gpio.PUD_DOWN)

try:
    print("Waiting for button press...")
    while True:
        # Check if the button is pressed
        if gpio.input(button_pin) == gpio.HIGH:
            print("Button pressed!")
            # Wait for a short period to avoid detecting multiple presses
            time.sleep(0.2)
        time.sleep(0.1)  # Small delay to debounce the button
except KeyboardInterrupt:
    # Clean up gpio on CTRL+C exit
    print("Exiting...")
    gpio.cleanup()
except Exception as e:
    # Clean up gpio on other exceptions
    print(f"An error occurred: {e}")
    gpio.cleanup()
finally:
    # Ensure gpio is cleaned up on normal exit
    gpio.cleanup()