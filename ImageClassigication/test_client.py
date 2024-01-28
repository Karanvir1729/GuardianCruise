import cv2
import socket
import pickle
import struct

# Set up the socket connection
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = '100.65.6.83'  # Change this to your server's IP address
port = 5560  # Change this to your server's port
client_socket.connect((host_ip, port))

# Start capturing video from the webcam
video = cv2.VideoCapture(0)

while True:
    # Read frames from the camera
    ret, frame = video.read()

    # Serialize the frame using pickle
    data = pickle.dumps(frame)

    # Send the length of the serialized frame
    message_size = struct.pack("L", len(data))

    # Send the length of the data first
    client_socket.sendall(message_size)

    # Then send the data
    if len(data) > 0:  # Check if data is not empty
        client_socket.sendall(data)

    # If you want to display the stream locally, uncomment the following lines
    cv2.imshow('TRANSMITTING VIDEO', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close everything
video.release()
cv2.destroyAllWindows()
client_socket.close()