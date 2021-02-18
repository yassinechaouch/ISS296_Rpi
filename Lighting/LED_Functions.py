from gpiozero import LED
from time import sleep

red_led = LED(17) #GPIO17
blue_led = LED(18) #GPIO18

while True:
    red_led.on()
    sleep(1)
    red_led.off()
    blue_led.on()
    sleep(1)
    blue_led.off()


    '''red = LED(17)
    
    red.blink()
    
    pause()'''
