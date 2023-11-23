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

# #captureing images in raspberry pi
import time
import picamera

# 카메라 초기화
camera = picamera.PiCamera()

# 카메라 해상도 설정
camera.resolution = (1920, 1080)

# 촬영 시작
camera.start_preview()

# 촬영 시간 설정 (1분 10초)
capture_time = 70

# 촬영할 프레임 수 계산
frame_count = capture_time * 30

# 이미지 파일 이름 설정
filename = 'image{}.jpg'

# 프레임마다 사진 촬영
for i in range(frame_count):
    camera.capture(filename.format(i))
    time.sleep(1/30)  # 30fps로 촬영하기 위해 1/30초 딜레이

# 촬영 종료
camera.stop_preview()

# capture images for training data
# import cv2
# import time
# import os
#
# cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FPS, 30)
#
# # Create a folder to store the images
# folder_name = "images"
# if not os.path.exists(folder_name):
#     os.makedirs(folder_name)
#
# # Start capturing images
# start_time = time.time()
# frame_count = 0
# duration = 75 # in seconds
# while (time.time() - start_time) < duration:
#     ret, frame = cap.read()
#
#     if ret:
#         # Save the image to disk
#         file_name = os.path.join(folder_name, f"image_{frame_count}.jpg")
#         cv2.imwrite(file_name, frame)
#
#         # Increment the frame count
#         frame_count += 1
#
# cap.release()
#
# # Calculate and print the capture time
# capture_time = time.time() - start_time
# print(f"Captured {frame_count} images in {capture_time:.2f} seconds.")
