import RPi.GPIO as IO
import time
import multiprocessing as mp

#Gpio pins for drive
pwmPin = 19
dirPin = 13
strPin = 26

speed = 10


def drive():
    IO.setwarnings(False)
    IO.setmode(IO.BCM)
    IO.setup(pwmPin,IO.OUT)
    IO.setup(dirPin,IO.OUT)

    p = IO.PWM(pwmPin, 100)
    p.start(0)

    #forward
    IO.output(dirPin, True)
    for x in range (speed):
        p.ChangeDutyCycle(x)
        time.sleep(0.1)
    time.sleep(1)
    for x in range (speed, 0, -1):
        p.ChangeDutyCycle(x)
        time.sleep(0.1)
    time.sleep(0.5)

    #backward
    IO.output(dirPin, False)
    for x in range (speed):
        p.ChangeDutyCycle(x)
        time.sleep(0.1)
    time.sleep(0.5)
    for x in range (speed, 0, -1):
        p.ChangeDutyCycle(x)
        time.sleep(0.1)

def steering():
    IO.setmode(IO.BCM)
    IO.setup(strPin, IO.OUT)
    p = IO.PWM(strPin, 100)
    p.start(3)

    #constant parameters
    center = 10.5
    left = 15
    right = 7

    # servo Degree 7~21, steering deg 7-10.5-15
    try:
        while True:
            p.ChangeDutyCycle(center)  # center
            print('angle:1')
            time.sleep(1)
            p.ChangeDutyCycle(left)  # left
            print('angle:5')
            time.sleep(1)
            p.ChangeDutyCycle(center)
            print('angle:8')
            time.sleep(1)
            p.ChangeDutyCycle(right)
            print('angle:5')
            time.sleep(1)

    except KeybordInterrupt:
        p.stop()
    IO.cleanup()

p1 = mp.Process(target=drive)
p2 = mp.Process(target=steering)

p1.start()
p2.start()

#kyu