# Created by Charles
# April 11, 2017

# Imports
from flask import jsonify
import RPi.GPIO as GPIO

# Class to represent a GPIO
# output pin on the Rapsberry PI
class Output:

    def __init__(self, id, info):
        GPIO.setup(id, GPIO.OUT)
        self.id = id
	self.state = False
        self.info = info

    def toggle(self):
        self.state = not self.state
        GPIO.output(self.id,self.state)

    def toDict(self):
        return {'id' : self.id, 'info' : self.info, 'state' : self.state}

    def toJSON(self):
        return jsonify(self.toDict())
