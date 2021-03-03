import RPi.GPIO as GPIO
import time


GPIO.cleanup()
# Setting up the Rpi
GPIO.setmode(GPIO.BOARD)

button= 10

GPIO.setup(button,GPIO.IN)
GPIO.setup(8,GPIO.OUT)
#GPIO.setup(16,GPIO.OUT)
#GPIO.setup(18,GPIO.OUT)
GPIO.setwarnings(False)

# Loop
while True:

    if GPIO.input(button):
        GPIO.output(8, True)
        print("\nLED ON")
    else: GPIO.output(8, False)
        

