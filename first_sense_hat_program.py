from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(r=90)

while True:
    sense.show_message("Hello my name is Jeff Ligon and this is fun!!", text_colour=(0,255,0), back_colour=(100,100,100), scroll_speed=0.05)