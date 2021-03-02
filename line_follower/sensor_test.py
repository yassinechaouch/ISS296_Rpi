import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library

GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering

sensor = 10
GPIO.setup(sensor, GPIO.IN)  # Set pin 8 to be an output pin and set initial value to low (off)

while True:
    if GPIO.input(sensor):
        print("white surface")
    else:
        print("black surface")


