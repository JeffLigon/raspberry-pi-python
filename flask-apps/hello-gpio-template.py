# Wiring Notes
# button need to be wired like other GPIO project in book
# Project: Simple Soundboard
# https://learning.oreilly.com/library/view/Getting+Started+With+Raspberry+Pi,+3rd+Edition/9781680452457/ch07.html#FIG0802
# one side - 5V
# same side other pin - pin 26 and resistor connected to ground
from flask import Flask, render_template
import datetime
import RPi.GPIO as GPIO
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

@app.route("/")
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'HELLO PINS!',
      'time': timeString
      }
   return render_template('main.html', **templateData)

@app.route("/readPin/<pin>") 
def readPin(pin):
   try: 
      GPIO.setup(int(pin), GPIO.IN) 
      if GPIO.input(int(pin)) == True: 
         response = "Pin number " + pin + " is high!"
      else: 
         response = "Pin number " + pin + " is low!"
   except: 
      response = "There was an error reading pin " + pin + "."

   templateData = {
      'title' : 'Status of Pin' + pin,
      'response' : response
      }

   return render_template('pin.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)