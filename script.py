import RPi.GPIO as GPIO
import time
import datetime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)

print ("Time : " + str(datetime.datetime.now().time()))

x = 0
while x < 3:
    GPIO.output(19,True)
    time.sleep(1)
    GPIO.output(19,False)
    time.sleep(1)	
    x = x + 1


