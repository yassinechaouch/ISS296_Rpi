import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering


GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(9, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)


for i in range(10):
    if i%2:
         GPIO.output(8, GPIO.HIGH) # Turn on
         sleep(0.5) # Sleep for 1 second
         GPIO.output(8, GPIO.LOW) # Turn off
         GPIO.output(9, GPIO.HIGH)  # Turn on
         sleep(0.5)  # Sleep for 1 second
         GPIO.output(9, GPIO.LOW)  # Turn off
         GPIO.output(10, GPIO.HIGH)  # Turn on
         sleep(0.5)  # Sleep for 1 second
         GPIO.output(10, GPIO.LOW)  # Turn off
         GPIO.output(11, GPIO.HIGH)  # Turn on
         sleep(0.5)  # Sleep for 1 second
         GPIO.output(11, GPIO.LOW)  # Turn off

    else:
        GPIO.output(11, GPIO.HIGH)  # Turn on
        sleep(0.5)  # Sleep for 1 second
        GPIO.output(11, GPIO.LOW)  # Turn off
        GPIO.output(10, GPIO.HIGH)  # Turn on
        sleep(0.5)  # Sleep for 1 second
        GPIO.output(10, GPIO.LOW)  # Turn off
        GPIO.output(9, GPIO.HIGH)  # Turn on
        sleep(0.5)  # Sleep for 1 second
        GPIO.output(9, GPIO.LOW)  # Turn off
        GPIO.output(8, GPIO.HIGH)  # Turn on
        sleep(0.5)  # Sleep for 1 second
        GPIO.output(8, GPIO.LOW)  # Turn off
