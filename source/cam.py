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

# from picamera2.encoders import H264Encoder
# from picamera2 import Picamera2
# import time
# picam2 = Picamera2()
# video_config = picam2.create_video_configuration()
# picam2.configure(video_config)
# encoder = H264Encoder(bitrate=10000000)
# output = "test.h264"
# picam2.start_recording(encoder, output)
# time.sleep(5)
# picam2.stop_recording()


# capture images for training data
import cv2
import time
import os

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 30)

# Create a folder to store the images
folder_name = "images"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Start capturing images
start_time = time.time()
frame_count = 0
duration = 75 # in seconds
while (time.time() - start_time) < duration:
    ret, frame = cap.read()

    if ret:
        # Save the image to disk
        file_name = os.path.join(folder_name, f"image_{frame_count}.jpg")
        cv2.imwrite(file_name, frame)

        # Increment the frame count
        frame_count += 1

cap.release()

# Calculate and print the capture time
capture_time = time.time() - start_time
print(f"Captured {frame_count} images in {capture_time:.2f} seconds.")
