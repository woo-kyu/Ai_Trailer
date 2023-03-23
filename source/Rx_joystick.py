import socket
import time
import struct
import numpy as np
import cv2

HOST_IP = '192.168.0.13'
PORT = 8000

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST_IP, PORT)
sock.connect(server_address)

while True:
    cmd = 12
    cmd = struct.pack('B', cmd)
    sock.sendall(cmd)

    data_bytes = sock.recv(1)
    data = struct.unpack('B', data_bytes)
    print(data[0])

    time.sleep(0.1)

