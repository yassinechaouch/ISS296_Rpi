# import GPIO library
import RPi.GPIO as GPIO

# set GPIO numbering mode and define input and output pins
GPIO.setmode(GPIO.BOARD)
#GPIO.setup(12, GPIO.IN)
#GPIO.setup(16, GPIO.IN)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
p=GPIO.PWM(8,1000)
p.start(100)

try:
    while True:
   	 GPIO.output(10, GPIO.HIGH)

        #if GPIO.input(16):
         #  GPIO.output(15, True)
        #else:
          #  GPIO.output(15, False)

finally:
    # cleanup the GPIO pins before ending
    GPIO.cleanup()
