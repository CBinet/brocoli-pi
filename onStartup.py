import RPi.GPIO as GPIO
import time
import datetime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

print ("Time : " + str(datetime.datetime.now().time()))

x = 0
pin = 17
while x < 3:
    GPIO.output(pin,True)
    time.sleep(.1)
    GPIO.output(pin,False)
    time.sleep(.1)	
    x = x + 1
    pin = pin + 1


