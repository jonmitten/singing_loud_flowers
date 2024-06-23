import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# List of all GPIO pins on Raspberry Pi
all_pins = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]

# Function to check if a pin is in use
def is_pin_in_use(pin):
    try:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        time.sleep(0.1)
        if GPIO.input(pin):
            return True
        else:
            return False
    except RuntimeError:
        return True
    except Warning:
        # Handling physical pull up resistor warning
        return True

# Check each pin and notify if in use
in_use_pins = []
for pin in all_pins:
    if is_pin_in_use(pin):
        in_use_pins.append(pin)

# Clean up GPIO settings
GPIO.cleanup()

# Print the result
if in_use_pins:
    print("The following pins are in use: ", in_use_pins)
else:
    print("No pins are in use.")
