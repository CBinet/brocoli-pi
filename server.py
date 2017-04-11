import RPi.GPIO as GPIO
from flask import Flask
from Output import Output

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)

app = Flask(__name__)

output19 = Output(19)

@app.route('/status')
def getStatus():
    return output19.getStatus()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
