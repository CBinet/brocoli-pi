import RPi.GPIO as GPIO
import time
import datetime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)

x = 0
while x < 5
    GPIO.output(19,True)
    time.sleep(1)
    GPIO.output(19,False)
    x = x + 1

print ("Time : " + str(datetime.datetime.now().time()))

