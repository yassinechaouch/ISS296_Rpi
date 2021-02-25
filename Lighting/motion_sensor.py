import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library
from time import sleep  # Import the sleep function from the time module

GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
led = 8
motion_sensor = 10

GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)  # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(motion_sensor, GPIO.IN)  # Set pin 8 to be an output pin and set initial value to low (off)

s = GPIO.input(motion_sensor)

while s:
    GPIO.output(led, GPIO.HIGH)  # Turn off
    s = GPIO.input(motion_sensor)
