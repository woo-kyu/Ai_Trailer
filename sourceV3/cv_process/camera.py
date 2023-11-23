from cam_test import *

CAMERA_NUMBER = 0



cam = cv2.VideoCapture(CAMERA_NUMBER)

while True:
    ret, frame = cam.read()
    if not ret:
        break
    edged = canny(gaussian_blur(grayscale(frame), kernel_size=5), threshold1=100, threshold2=200)

    cv2.imshow("frame", edged)

    if cv2.waitKey(1) == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
