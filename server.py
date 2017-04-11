import RPi.GPIO as GPIO
from flask import Flask
import Ouput

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)

app = Flask(__name__)

output19 = new Ouput(19)
print (output19.getId())
@app.route('/:id/status')
def index():
    return 'Hello world'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
