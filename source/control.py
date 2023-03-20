import tkinter as tk
import RPi.GPIO as IO
from picamera2.encoders import H264Encoder
from picamera2 import Picamera2
import time
import cv2

#gpio pins set
pwmPin = 19
dirPin = 13
strPin = 26

#gpio setup for drive
IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(pwmPin,IO.OUT)
IO.setup(dirPin,IO.OUT)

pd = IO.PWM(pwmPin, 100)
pd.start(0)

speed = 0
steer = 0
steeer_center = 10.5

#gpio setup for steering
IO.setmode(IO.BCM)
IO.setup(strPin, IO.OUT)
ps = IO.PWM(strPin, 100)
ps.start(3)


# GUI setup
window = tk.Tk()
window.title("RC Car Controller")

# Functions for controlling the RC car
def forward(speed):
    speed += 2
    pd.changeDutyCycle(speed)
    return speed
def backward(speed):
    speed -= 2
    pd.changeDutyCycle(speed)
    return speed
def stop():
    speed = 0
    pd.changeDutyCycle(speed)
    return speed

def left(steeer):
    steeer += 0.5
    ps.changeDutyCycle(steeer)
def right(steeer):
    steeer -= 0.5
    ps.changeDutyCycle(steeer)
def str_center():
    ps.changeDutyCycle(steeer_center)



# GUI elements
btn_forward = tk.Button(window, text="Forward", command=forward)
btn_backward = tk.Button(window, text="Backward", command=backward)
btn_stop = tk.Button(window, text="Stop", command=stop)
btn_left = tk.Button(window, text="Left", command=left)
btn_right = tk.Button(window, text="Right", command=right)
btn_str_center = tk.Button(window, text="Center", command=str_center)

# Place the buttons on the window
btn_forward.grid(row=0, column=1)
btn_backward.grid(row=2, column=1)
btn_stop.grid(row=1, column=1)
btn_left.grid(row=1, column=0)
btn_right.grid(row=1, column=2)
btn_str_center.grid(row=1, column=3)


#show camera preview
picam2 = Picamera2()
picam2.preview_configuration.main.size = (1280,720)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()

while True:
    im= picam2.capture_array()
    cv2.imshow("Camera", im)
    if cv2.waitKey(1)==ord('q'):
        break
cv2.destroyAllWindows()


# Start the GUI
window.mainloop()
