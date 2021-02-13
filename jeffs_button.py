from gpiozero import Button, LED
from time import time, sleep
from random import randint

red_led = LED(17)
yellow_led = LED(27)
green_led = LED(22)
btn = Button(4)

while True:
    btn.wait_for_press()
    red_led.toggle()
    sleep(0.3)
    yellow_led.toggle()
    sleep(0.3)
    green_led.toggle()
    btn.wait_for_release()
    sleep(3)
    red_led.off()
    yellow_led.off()
    green_led.off()