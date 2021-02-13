from gpiozero import LED
from time import sleep

red_led = LED(17)

while True:
    red_led.blink(0.3,0.3,3)
    sleep(3)
    red_led.blink(1,1,3)
    sleep(3)
    red_led.blink(0.3,0.3,3)
    sleep(5)
    print(red_led.is_lit)
#       
#while True:
#    red_led.on()
#    sleep(1)
#    red_led.off()
#    sleep(1)
    
