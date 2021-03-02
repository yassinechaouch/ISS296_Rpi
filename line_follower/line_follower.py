import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


GPIO.setup(2,GPIO.IN) #GPIO 2 -> Left IR out
GPIO.setup(3,GPIO.IN) #GPIO 3 -> Right IR out

GPIO.setup(4,GPIO.OUT) #GPIO 4 -> Motor 1 terminal A
GPIO.setup(14,GPIO.OUT) #GPIO 14 -> Motor 1 terminal B

GPIO.setup(17,GPIO.OUT) #GPIO 17 -> Motor Left terminal A
GPIO.setup(18,GPIO.OUT) #GPIO 18 -> Motor Left terminal B

while True:

    if GPIO.input(2)==True and GPIO.input(3)==True: #both while move forward
        GPIO.output(4,True) #1A+
        GPIO.output(14,False) #1B-

        GPIO.output(17,True) #2A+
        GPIO.output(18,False) #2B-

    elif GPIO.input(2)==False and GPIO.input(3)==True: #turn right
        GPIO.output(4,True) #1A+
        GPIO.output(14,True) #1B-

        GPIO.output(17,True) #2A+
        GPIO.output(18,False) #2B-

    elif GPIO.input(2)==True and GPIO.input(3)==False: #turn left
        GPIO.output(4,True) #1A+
        GPIO.output(14,False) #1B-

        GPIO.output(17,True) #2A+
        GPIO.output(18,True) #2B-

    else:  #stay still
        GPIO.output(4,True) #1A+
        GPIO.output(14,True) #1B-

        GPIO.output(17,True) #2A+
        GPIO.output(18,True) #2B-