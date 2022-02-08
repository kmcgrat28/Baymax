import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
p = GPIO.PWM(17, 50)
speed = 7.5
p.start(7.5)

try:
    while True:
        p.ChangeDutyCycle(speed)  # turn towards 90 degree
        time.sleep(10) # sleep 1 second
        p.ChangeDutyCycle(speed - 5)  # turn towards 0 degree
        time.sleep(10) # sleep 1 second
#        p.ChangeDutyCycle(speed + 5) # turn towards 180 degree
#        time.sleep(1) # sleep 1 second 
        p.stop()
        print("done")
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
