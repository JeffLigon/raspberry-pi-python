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
print ("Waiting for 2 seconds")
time.sleep(2)

#Let's move the servo!
print ("Duty Cycle 0")
servo1.ChangeDutyCycle(0)
time.sleep(2)
print ("Duty Cycle 2")
servo1.ChangeDutyCycle(2)
time.sleep(2)
print ("Duty Cycle 3")
servo1.ChangeDutyCycle(3)
time.sleep(2)
print ("Duty Cycle 12")
servo1.ChangeDutyCycle(12)
time.sleep(2)
print ("Duty Cycle 0")
servo1.ChangeDutyCycle(0)
time.sleep(2)
#Define duty cycle variable
#duty = 2

#Loop for duty values 2 to 12 (0 to 180 degrees)
#while duty <= 12:
#    servo1.ChangeDutyCycle(duty)
#    time.sleep(1)
#    duty = duty + 1


#Clean-up at the end
servo1.stop()
GPIO.cleanup()
print ("Goodbye")


    
    
    

