import cv2
import matplotlib.pyplot as plt
import numpy as np
import multiprocessing
import tensorflow as tf
import keras as k

def show(img):
    cv2.imshow("Results Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def grayscale(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

def gaussian_blur(frame, kernel_size = 5):
    return cv2.GaussianBlur(frame, (kernel_size, kernel_size), 0)

def canny(frame, threshold1, threshold2):
    return cv2.Canny(frame, threshold1, threshold2)

def sliding_windows(frame):
    none = None

def Lenet():
    model = Sequential()
    model.add(Conv2D(filters = 6, kernel_size = (5,5), strides = (1,1), activation = "relu", input_shape = (32,32,1)),)

def show_matplotlib(img):
    plt.imshow(img)
    plt.show()