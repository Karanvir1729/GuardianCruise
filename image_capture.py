import cv2
import os
import time

cap = cv2.VideoCapture(0)

DELAY = 2

for i in range(10000):
    ret, frame = cap.read()
    cv2.imwrite(f"captured_image{i}.jpg", frame)
    if i > 10:
        os.remove(f"captured_image{i - 10}.jpg")
    time.sleep(DELAY)

cap.release()
cv2.destroyAllWindows()
