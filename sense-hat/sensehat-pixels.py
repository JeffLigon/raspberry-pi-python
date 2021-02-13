from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

sense.set_rotation(90)
sense.clear()

red = (255,0,0)
green = (0,255,0)
blue = (0,255,255)
white = (255,255,255)
off = (0,0,0)
random_color = (randint(0,255),randint(0,255),randint(0,255))
number = 1

print(random_color)

# sense.set_pixel(0,0,blue)
# sense.set_pixel(0,7,red)
# sense.set_pixel(7,0,green)
# sense.set_pixel(7,7,white)
while True:
    random_color = (randint(0,255),randint(0,255),randint(0,255))
    print(random_color)
    for i in range(0,8):
        sense.set_pixel(i,0,random_color)
        sleep(0.1)
    random_color = (randint(0,255),randint(0,255),randint(0,255))
    print(random_color)
    for i in range(0,8):
        sense.set_pixel(7,i,random_color)
        sleep(0.1)
    random_color = (randint(0,255),randint(0,255),randint(0,255))
    print(random_color)
    for i in range(7,0,-1):
        sense.set_pixel(i,7,random_color)
        sleep(0.1)
    random_color = (randint(0,255),randint(0,255),randint(0,255))
    print(random_color)
    for i in range(7,0,-1):
        sense.set_pixel(0,i,random_color)
        sleep(0.1)
    sense.show_letter(str(number))
    number = number + 1
    sleep(0.3)
    sense.clear()
