# import GPIO library
import RPi.GPIO as GPIO

# set GPIO numbering mode and define input and output pins
GPIO.setmode(GPIO.BOARD)
#GPIO.setup(12, GPIO.IN)
#GPIO.setup(16, GPIO.IN)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
x =input("choose :")
try:
    while True:
        if x:
            GPIO.output(11, GPIO.HIGH)
        else:
            GPIO.output(11, GPIO.LOW)
        #if GPIO.input(16):
         #  GPIO.output(15, True)
        #else:
          #  GPIO.output(15, False)

finally:
    # cleanup the GPIO pins before ending
    GPIO.cleanup()