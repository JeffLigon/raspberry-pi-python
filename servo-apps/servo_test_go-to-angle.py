# Import libraries
import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pin 16 as an output, and set servo1 as pin 16 as PWM
GPIO.setup(16,GPIO.OUT)
servo1 = GPIO.PWM(16,50) # Note 16 is pin, 50 = 50Hz pulse

#start PWM running, but with value of 0 (pulse off)
servo1.start(0)

#Loop to allow user to enter angle to move to.
try:
    while True:
        angle = float(input('Enter the angle between 0 & 180: '))
        servo1.ChangeDutyCycle(2+(angle/18))
        time.sleep(0.5)
        servo1.ChangeDutyCycle(0)

#Clean-up at the end
finally:
    servo1.stop()
    GPIO.cleanup()
    print ("Goodbye")


    
    
    
