import RPi.GPIO as GPIO
import time


# Setting up the Rpi
GPIO.setmode(GPIO.BCM)

button= 14

GPIO.setup(button,GPIO.IN)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setwarnings(False)

# Loop
while button:
    GPIO.output(10, True)
    GPIO.output(16, True)
    GPIO.output(18, True)
    print("\nLEDs are ON")
    time.sleep(1)
    GPIO.output(10, False)
    GPIO.output(16, False)
    GPIO.output(18, False)
    print("\nLEDs are OFF")
    time.sleep(1)

