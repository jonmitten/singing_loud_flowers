import RPi.GPIO as GPIO
import time

# Use BCM GPIO references
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin to use
button_pin = 18

# Set up the GPIO pin as an input with a pull-down resistor
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    print("Waiting for button press...")
    while True:
        # Check if the button is pressed
        if GPIO.input(button_pin) == GPIO.HIGH:
            print("Button pressed!")
            # Wait for a short period to avoid detecting multiple presses
            time.sleep(0.2)
        time.sleep(0.1)  # Small delay to debounce the button
except KeyboardInterrupt:
    # Clean up GPIO on CTRL+C exit
    print("Exiting...")
    GPIO.cleanup()
except Exception as e:
    # Clean up GPIO on other exceptions
    print(f"An error occurred: {e}")
    GPIO.cleanup()
finally:
    # Ensure GPIO is cleaned up on normal exit
    GPIO.cleanup()