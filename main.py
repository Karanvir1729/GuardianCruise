import cv2
import dlib
import numpy as np
import screeninfo
from pynput.keyboard import Key, Controller
from collections import deque

face_detector = dlib.get_frontal_face_detector()
landmark_predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')  

cap = cv2.VideoCapture(0)  
monitors = screeninfo.get_monitors()
monitor = monitors[0]

keyboard = Controller()
flag = True

distances = deque(maxlen=25)
bin = deque(maxlen=15)

def change():
    keyboard.press(Key.alt)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.release(Key.alt)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector(gray)
    
    for face in faces:
        landmarks = landmark_predictor(gray, face)
        
        left_eye = np.array([landmarks.part(36).x, landmarks.part(36).y])
        right_eye = np.array([landmarks.part(45).x, landmarks.part(45).y])
        
        euclidean_distance = np.linalg.norm(right_eye - left_eye)
        distances.append(euclidean_distance)
        avg_distance = sum(distances)/25
        cv2.putText(frame, f'Distance: {avg_distance:.2f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        

        if avg_distance < 65:
            bin.append(1)
        else:
            bin.append(0)

        screen = sum(bin)/len(bin)

             

        
            


        
    cv2.imshow("Frame", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
