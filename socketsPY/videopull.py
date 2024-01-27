import cv2
import socket
import pickle
import struct

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 5555))
server_socket.listen(0)

connection, addr = server_socket.accept()

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    data = pickle.dumps(frame)
    message_size = struct.pack("L", len(data))
    connection.sendall(message_size + data)

camera.release()
