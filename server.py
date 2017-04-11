import RPi.GPIO as GPIO
from flask import Flask
from Output import Output
from flask import jsonify

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

app = Flask(__name__)

outputs = [Output(17, "Red Light"),Output(18, "Green Light"),Output(19, "Yellow Light")]

@app.route('/<id>')
def getOutput(id):
    output = findOutput(id)
    if output:
        return jsonify(id = output.id, info = output.info, state = output.state)
    else:
        return "NOT_FOUND : This output ID is not binded."


@app.route('/<id>/status')
def getStatus(id):
    output = findOutput(id)
    if output:
        return jsonify(result = output.getCurrentState())
    else:
        return "NOT_FOUND : This output ID is not binded."

@app.route('/<id>/info')
def getInfo(id):
    output = findOutput(id)
    if output:
        return jsonify(result = output.getInfo())
    else:
        return "NOT_FOUND : This output ID is not binded."

@app.route('/<id>/toggle')
def toggle(id):
    output = findOutput(id)
    if output:
        output.toggle()
        return jsonify(result = output.getCurrentState())
    else:
        return "NOT_FOUND : This output ID is not binded."

def findOutput(id):
    for output in outputs:
	if id == str(output.getId()):
	    return output

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
