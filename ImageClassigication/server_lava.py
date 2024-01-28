import socket
import threading
import os
import LLaVA
import time
# Define the host and port on which the server will listen
HOST = '100.65.3.233'  # Indicates that the server will accept connections from any network interface
PORT = 12000      # Port number (you can choose any available port)
BUFFER_SIZE = 4096

# Function to handle each client connection



# Function to handle each client connection
def handle_client(conn, addr):
    print('Connected by', addr)
    # Receive the file size first
    file_size = int.from_bytes(conn.recv(4), byteorder='big')
    print(f"Receiving file of size: {file_size} bytes")

    # Receive and save the file
    received_data = bytearray()
    while len(received_data) < file_size:
        remaining_bytes = file_size - len(received_data)
        received_data += conn.recv(min(remaining_bytes, BUFFER_SIZE))

    # Get the filename
    filename = f"received_image_{addr[0]}.jpg"

    # Save the received file as a JPG
    with open(filename, 'wb') as f:
        f.write(received_data)

    print(f"File received and saved as: {filename}")
    output = LLaVA.getInfo(filename)
    print(output)
    while True:

        conn.sendall(output.encode())
        conn.close()


# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to the host and port
    s.bind((HOST, PORT))
    # Listen for incoming connections
    s.listen()
    print("Server is listening for connections...")

    # Accept connections and handle them using threads
    while True:
        # Accept a connection
        conn, addr = s.accept()
        # Start a new thread to handle the client
        threading.Thread(target=handle_client, args=(conn, addr)).start()