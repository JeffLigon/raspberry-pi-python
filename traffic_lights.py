""" Wiring Notes
Ground--220 Ohm resistor--Red LED--GPIO17
Ground--220 Ohm resistor--Yellow LED--GPIO27
Ground--220 Ohm resistor--Green LED--GPIO22
"""
from gpiozero import LED
from time import sleep

red_led = LED(17)
yellow_led = LED(27)
green_led = LED(22)
sleep_timer = 0.1

while True:
    red_led.on()
    sleep(sleep_timer)
    yellow_led.on()
    sleep(sleep_timer)
    green_led.on()
    sleep(sleep_timer)
    red_led.off()
    sleep(sleep_timer)
    yellow_led.off()
    sleep(sleep_timer)
    green_led.off()
    sleep(sleep_timer)
    
    
# print(red_led.is_lit)
#       
#while True:
#    red_led.on()
#    sleep(1)
#    red_led.off()
#    sleep(1)
    

