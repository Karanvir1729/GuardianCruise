import cv2
import dlib
import numpy as np

# Load the pre-trained face detector from dlib
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  # You need to download this file

# Load the video capture
cap = cv2.VideoCapture(0)  # Use 0 for default camera, or provide the video file path

# Variables to keep track of the blink state
blink_count = 0
blink_threshold = 2  # Adjust this threshold based on your requirements
eyes_closed = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = detector(gray)
    
    for face in faces:
        # Get the facial landmarks
        landmarks = predictor(gray, face)

        # Extract eye region coordinates as integers
        left_eye_coords = np.array([(int(landmarks.part(i).x), int(landmarks.part(i).y)) for i in range(36, 42)], dtype=np.int32)
        right_eye_coords = np.array([(int(landmarks.part(i).x), int(landmarks.part(i).y)) for i in range(42, 48)], dtype=np.int32)

        # Draw the eyes on the frame
        cv2.polylines(frame, [left_eye_coords], isClosed=True, color=(255, 0, 0), thickness=1)
        cv2.polylines(frame, [right_eye_coords], isClosed=True, color=(255, 0, 0), thickness=1)

        # Calculate the eye aspect ratio to determine if the eyes are closed
        left_eye_aspect_ratio = (abs(left_eye_coords[1][1] - left_eye_coords[5][1]) +
                                abs(left_eye_coords[2][1] - left_eye_coords[4][1])) / \
                               (2 * abs(left_eye_coords[0][0] - left_eye_coords[3][0]))

        right_eye_aspect_ratio = (abs(right_eye_coords[1][1] - right_eye_coords[5][1]) +
                                 abs(right_eye_coords[2][1] - right_eye_coords[4][1])) / \
                                (2 * abs(right_eye_coords[0][0] - right_eye_coords[3][0]))

        # Average eye aspect ratio
        avg_eye_aspect_ratio = (left_eye_aspect_ratio + right_eye_aspect_ratio) / 2

        # Check if the eyes are closed
        if avg_eye_aspect_ratio < 0.2:
            blink_count += 1
        else:
            blink_count = 0

        # Determine if a blink has occurred based on the threshold
        if blink_count >= blink_threshold:
            eyes_closed = True
            print("Blink detected!")

    # Display the frame
    cv2.imshow("Blink Detection", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
