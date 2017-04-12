# Created by Charles
# April 11, 2017

# Imports
import requests
import json
from flask import Flask
from flask import jsonify,make_response,request
from modules.GPIOControls.Output import Output
from modules.GPIOControls.Group import Group
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
# Here is where you instanciate the groups you want to use :
# Example: 
#    Group(10, [Output(17, "Fan 1"),Output(18, "Fan 2")], "Fans controller") 
#
# This will create a group with output 17 and 18 with the label "Fans controller"
groups = [Group(0, outputs, "Basic 3 LED group")]

# -- API Routes -- 

# Returns all of the outputs
# @return JSON of the outputs list
@app.route('/outputs')
def getOutputs():
    rtrn = []
    for output in outputs:
        rtrn.append(output.toDict())
    
    return make_response(jsonify({'results' : rtrn}), 200)

# Returns the output at location <id>
# @params id : Id to to match with
# @return JSON of the selected output
@app.route('/outputs/<id>')
def getOutput(id):
    output = findOutput(id)
    if output:
        return make_response(output.toJSON(), 200)
    else:
        return make_response("NOT_FOUND : This output ID is not binded.", 400)

# Toggle the voltage on the output at location <id>
# @params id : Id to to match with
# @return JSON of the selected output
@app.route('/outputs/<id>/toggle')
def toggleOutput(id):
    output = findOutput(id)
    if output:
        output.toggle()
        return make_response(output.toJSON(), 200)
    else:
        return make_response("NOT_FOUND : This output ID is not binded.", 400)


# Returns all of the groups
# @return JSON of the groups list
@app.route('/groups')
def getGroups():
    rtrn = []
    for group in groups:
        rtrn.append(group.toDict())
    
    return make_response(jsonify({'results' : rtrn}), 200)

# Returns the group <id>
# @params id : Id to to match with
# @return JSON of the selected group
@app.route('/groups/<id>')
def getGroup(id):
    group = findGroup(id)
    if group:
        return make_response(group.toJSON(), 200)
    else:
        return make_response("NOT_FOUND : This group ID is not binded.", 400)

# Toggle the voltage on the outputs of group <id>
# @params id : Id to to match with
# @return JSON of the selected group
@app.route('/groups/<id>/toggle')
def toggleGroup(id):
    group = findGroup(id)
    if group:
        group.toggle()
        return make_response(group.toJSON(), 200)
    else:
        return make_response("NOT_FOUND : This group ID is not binded.", 400)

@app.route('/weather')
def getWeather():
    city = request.args.get('city');
    if city:
        r = requests.get('https://api.apixu.com/v1/current.json?key=c0efcc5afb314c0182a35001171204&q=' + city);
        return make_response(json.dumps(r.json(), indent=4), 200)
    else :
        return make_response("INVALID QUERY : Missing the city parameter.", 400)

# -- Helper functions --

# Returns the output with 'id'
# @params id : Id to match with
# @return Selected output
def findOutput(id):
    for output in outputs:
	if id == str(output.id):
	    return output

# Returns the group  'id'
# @params id : Id to match with
# @return Selected group
def findGroup(id):
    for group in groups:
	if id == str(group.id):
	    return group

# -- Main --

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
