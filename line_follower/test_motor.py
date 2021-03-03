# import GPIO library
import RPi.GPIO as GPIO
from time import sleep

# set GPIO numbering mode and define input and output pins
GPIO.setmode(GPIO.BOARD)

motor_f=8
motor_b=10
GPIO.setup(motor_f, GPIO.OUT)
GPIO.setup(motor_b, GPIO.OUT)

#p=GPIO.PWM(8,1000)
#p.start(100)

try:
    while True:
        GPIO.output(motor_b, GPIO.HIGH)
        GPIO.output(motor_f, GPIO.LOW)
        sleep(5)
        GPIO.output (motor_b, GPIO.LOW)
        GPIO.output (motor_f, GPIO.HIGH)
        sleep(5)

        #if GPIO.input(16):
         #  GPIO.output(15, True)
        #else:
          #  GPIO.output(15, False)

finally:
    # cleanup the GPIO pins before ending
    GPIO.cleanup()
