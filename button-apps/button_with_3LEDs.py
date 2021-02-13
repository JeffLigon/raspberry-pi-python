from gpiozero import LED, Button 
from signal import pause

red_led = LED(17)
yellow_led = LED(27)
green_led = LED(22) 
button = Button(26) 
button.when_pressed = red_led.on 
button.when_released = red_led.off 
pause()