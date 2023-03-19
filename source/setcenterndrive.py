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
    time.sleep(75)
    for x in range (speed, 0, -5):
        p.ChangeDutyCycle(x)
        time.sleep(0.1)
    time.sleep(0.5)

def steering():
    IO.setmode(IO.BCM)
    IO.setup(strPin, IO.OUT)
    p = IO.PWM(strPin, 100)
    p.start(3)

    #constant parameters
    center = 10.5


    # servo Degree 7~21, steering deg 7-10.5-15
    try:
        while True:
            p.ChangeDutyCycle(center)  # center
            

    except KeybordInterrupt:
        p.stop()
    IO.cleanup()


p1 = mp.Process(target=drive)
p2 = mp.Process(target=steering)

p2.start()
p1.start()