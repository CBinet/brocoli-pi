import RPi.GPIO as GPIO
from flask import Flask
from Output import Output

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)

app = Flask(__name__)

outputs = [Output(19)]

@app.route('/<id>/status')
def getStatus(id):
    for output in outputs:
	if id == output.getId():
	    return output.getCurrentState()
    return "NOT_FOUND : This output ID is not binded."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
