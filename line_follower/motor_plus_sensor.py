import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library

GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering

sensor = 12
motor_f=8
motor_b=10
GPIO.setup(motor_f, GPIO.OUT)
GPIO.setup(motor_b, GPIO.OUT)
GPIO.setup(sensor, GPIO.IN)  # Set pin 8 to be an output pin and set initial value to low (off)

while True:
    if GPIO.input(sensor):
        GPIO.output(motor_b, GPIO.HIGH)
        GPIO.output(motor_f, GPIO.LOW)
    else:
        GPIO.output (motor_b, GPIO.LOW)
        GPIO.output (motor_f, GPIO.HIGH)

