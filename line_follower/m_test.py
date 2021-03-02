import RPi.GPIO as GPIO
from time import sleep 

def init():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(10, GPIO.OUT)
	GPIO.setup(12, GPIO.OUT)

def forward(t):
	init()
	GPIO.output(10,True)
	GPIO.output(12,False)
	sleep(t)
	GPIO.cleanup()

def backward(t):
	init()
	GPIO.output(10, False)
	GPIO.output(12, True)
	sleep(t)
	GPIO.cleanup()


print("forward")
forward(5)
print("backward")
backward(5)

