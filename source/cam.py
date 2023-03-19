# import cv2
# from picamera2 import Picamera2
# from time import sleep

#show camera preview
# picam2 = Picamera2()
# picam2.preview_configuration.main.size = (1280,720)
# picam2.preview_configuration.main.format = "RGB888"
# picam2.preview_configuration.align()
# picam2.configure("preview")
# picam2.start()
#
# while True:
#     im= picam2.capture_array()
#     cv2.imshow("Camera", im)
#     if cv2.waitKey(1)==ord('q'):
#         break
# cv2.destroyAllWindows()


#captureing video

from picamera2.encoders import H264Encoder
from picamera2 import Picamera2
import time
picam2 = Picamera2()
video_config = picam2.create_video_configuration()
picam2.configure(video_config)
encoder = H264Encoder(bitrate=10000000)
output = "test.h264"
picam2.start_recording(encoder, output)
time.sleep(5)
picam2.stop_recording()
