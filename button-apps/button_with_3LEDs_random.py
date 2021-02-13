from gpiozero import LED, Button 
from signal import pause
from random import randint
from time import time, sleep

red = LED(17)
yellow = LED(27)
green = LED(22)
lights = [red,yellow,green]
button = Button(26)

while True:
    button.wait_for_press()
    lights[randint(0,2)].on()
    button.wait_for_release()
    red.off()
    green.off()
    yellow.off()
    
#while True:
#    random_light = [17,27,22]
#    random_led = LED(random_light[randint(0,2)])
#yellow_led = LED(27)
#green_led = LED(22) 
    
#light = [LED(17), LED(27), LED(22)]
#print(light[randint(0,2)])

#def button_on():
#    random_led.on
#def button_off():
#    random_led.off

#button.when_pressed = yellow_led.on

#    button.when_pressed = random_led.on
#    button.when_released = random_led.off
#    pause()
#button.when_pressed = button_on
#button.when_released = button_off
