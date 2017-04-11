# Created by Charles
# April 11, 2017

# Imports
from flask import Flask
from flask import jsonify,make_response
from Output import Output
import RPi.GPIO as GPIO

# GPIO setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Flask setup
app = Flask(__name__)

# Here is where you instanciate the pins you want to use :
# Example: 
#    Output(1, "Red Light") 
# This will setup the GPIO output pin 1 and will put up "Red Light" as the info-label.
outputs = [Output(17, "Red Light"),Output(18, "Green Light"),Output(19, "Yellow Light")]

# -- API Routes -- 
@app.route('/outputs')
def getOutputs():
    rtrn = []
    for output in outputs:
        rtrn.append(output.toJSON())
        print (output.toJSON())
    
    return make_response(jsonify({'results' : rtrn}), 200)

@app.route('/outputs/<id>')
def getOutput(id):
    output = findOutput(id)
    if output:
        return make_response(output.toJSON(), 200)
    else:
        return make_response("NOT_FOUND : This output ID is not binded.", 400)

@app.route('/outputs/<id>/toggle')
def toggle(id):
    output = findOutput(id)
    if output:
        output.toggle()
        return make_response(output.toJSON(), 200)
    else:
        return make_response("NOT_FOUND : This output ID is not binded.", 400)

# -- Helper functions --

def findOutput(id):
    for output in outputs:
	if id == str(output.id):
	    return output

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
