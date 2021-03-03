import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

rightsensor=22
leftsensor=24
leftmotorforward=8
leftmotorbackward=10
rightmotorforward=16
rightmotorbackward=18



GPIO.setup(leftsensor,GPIO.IN) #GPIO 2 -> Left IR out
GPIO.setup(rightsensor,GPIO.IN) #GPIO 3 -> Right IR out

GPIO.setup(rightmotorforward,GPIO.OUT) #GPIO 4 -> Motor right terminal A
GPIO.setup(rightmotorbackward,GPIO.OUT) #GPIO 14 -> Motor right terminal B

GPIO.setup(leftmotorforward,GPIO.OUT) #GPIO 17 -> Motor Left terminal A
GPIO.setup(leftmotorbackward,GPIO.OUT) #GPIO 18 -> Motor Left terminal B

while True:

    if GPIO.input(rightsensor)==True and GPIO.input(leftsensor)==True: #both while move forward
        GPIO.output(rightmotorforward,True) #1A+
        GPIO.output(leftmotorbackward,False) #1B-

        GPIO.output(leftmotorforward,True) #2A+
        GPIO.output(rightmotorbackward,False) #2B-

    elif GPIO.input(rightsensor)==False and GPIO.input(leftsensor)==True: #turn right
        GPIO.output(rightmotorforward,True) #1A+
        GPIO.output(leftmotorbackward,True) #1B-

        GPIO.output(leftmotorforward,False) #2A+
        GPIO.output(rightmotorbackward,False) #2B-

    elif GPIO.input(rightsensor)==True and GPIO.input(leftsensor)==False: #turn left
        GPIO.output(rightmotorforward,False) #1A+
        GPIO.output(leftmotorbackward,False) #1B-

        GPIO.output(leftmotorforward,True) #2A+
        GPIO.output(rightmotorbackward,True) #2B-

    else:  #stay still
        GPIO.output(rightmotorforward,False) #1A+
        GPIO.output(leftmotorbackward,False) #1B-

        GPIO.output(leftmotorforward,False) #2A+
        GPIO.output(rightmotorbackward,False) #2B-