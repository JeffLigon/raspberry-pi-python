from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
sense.set_rotation(r=90)

while True:
    r1 = randint(0,255)
    g1 = randint(0,255)
    b1 = randint(0,255)
    sense.show_letter("O", (r1,g1,b1))
    sleep(0.5)

    r2 = randint(0,255)
    g2 = randint(0,255)
    b2 = randint(0,255)
    sense.show_letter("M", (r2,g2,b2))
    sleep(0.5)

    r3 = randint(0,255)
    g3 = randint(0,255)
    b3 = randint(0,255)
    sense.show_letter("G", (r3,g3,b3))
    sleep(0.5)

    r4 = randint(0,255)
    g4 = randint(0,255)
    b4 = randint(0,255)
    sense.show_letter("!", (r4,g4,b4))
    sleep(0.5)
     
    sense.clear()
