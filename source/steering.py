import RPi.GPIO as GPIO
import time

pin = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
p = GPIO.PWM(pin, 100)
p.start(3)

# servo Degree 7~21, steering deg 7-10.5-15
try:
    while True:
        p.ChangeDutyCycle(10.5)  # center
        print('angle:1')
        time.sleep(1)
        p.ChangeDutyCycle(15)  # left
        print('angle:5')
        time.sleep(1)
        p.ChangeDutyCycle(10.5)
        print('angle:8')
        time.sleep(1)
        p.ChangeDutyCycle(7)
        print('angle:5')
        time.sleep(1)
except KeybordInterrupt:
    p.stop()
GPIO.cleanup()
