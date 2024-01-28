import cv2
import dlib
import numpy as np
from collections import deque
import time
import sys

start_time = time.time()

# Load the pre-trained face detector from dlib
detector = dlib.get_frontal_face_detector()
predictor_path = sys.argv[1]  # Path to shape_predictor_68_face_landmarks.dat
predictor = dlib.shape_predictor(predictor_path)

# Load the video capture
cap = cv2.VideoCapture(0)  # Use 0 for default camera, or provide the video file path

# Variables for blink detection
blink_count = 0
blink_threshold = 2  # Adjust this threshold based on your requirements
eyes_closed = False

# Variables for face orientation detection
face_detector = dlib.get_frontal_face_detector()
keyboard = Controller()
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

    # Blink detection
    faces = detector(gray)
    for face in faces:
        landmarks = predictor(gray, face)

        # Draw lines around the eyes
        left_eye_coords = np.array([(landmarks.part(i).x, landmarks.part(i).y) for i in range(36, 42)], dtype=np.int32)
        right_eye_coords = np.array([(landmarks.part(i).x, landmarks.part(i).y) for i in range(42, 48)], dtype=np.int32)
        cv2.polylines(frame, [left_eye_coords], isClosed=True, color=(0, 255, 0), thickness=2)
        cv2.polylines(frame, [right_eye_coords], isClosed=True, color=(0, 255, 0), thickness=2)

        # Draw lines around the face
        face_coords = np.array([(landmarks.part(i).x, landmarks.part(i).y) for i in range(0, 68)], dtype=np.int32)
        cv2.polylines(frame, [face_coords], isClosed=True, color=(0, 255, 0), thickness=2)

        left_eye_aspect_ratio = (abs(left_eye_coords[1][1] - left_eye_coords[5][1]) +
                                abs(left_eye_coords[2][1] - left_eye_coords[4][1])) / \
                               (2 * abs(left_eye_coords[0][0] - left_eye_coords[3][0]))

        right_eye_aspect_ratio = (abs(right_eye_coords[1][1] - right_eye_coords[5][1]) +
                                 abs(right_eye_coords[2][1] - right_eye_coords[4][1])) / \
                                (2 * abs(right_eye_coords[0][0] - right_eye_coords[3][0]))

        avg_eye_aspect_ratio = (left_eye_aspect_ratio + right_eye_aspect_ratio) / 2

        if avg_eye_aspect_ratio < 0.2:
            blink_count += 1
            tim = time.time() - start_time
            # print(f"blink rate: {blink_count/tim}")

        if blink_count >= blink_threshold:
            eyes_closed = True

    # Face orientation detection
    faces = face_detector(gray)
    for face in faces:
        # Your existing face orientation detection logic

    # Output the processed frame to stdout
        _, img_encoded = cv2.imencode('.jpg', frame)
        img_bytes = img_encoded.tobytes()
        sys.stdout.buffer.write(img_bytes)
        sys.stdout.flush()
