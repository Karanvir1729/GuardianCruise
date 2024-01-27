import socket

# Define the server's IP address and port number
SERVER_HOST = '100.65.3.233'  # Replace this with your server's IP address
SERVER_PORT = 12000            # Replace this with your server's port
BUFFER_SIZE = 4096

# Define the path to the JPG file you want to send
FILE_PATH = 'download (2).jpg'  # Replace this with the path to your JPG file

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the server
    s.connect((SERVER_HOST, SERVER_PORT))
    print("Connected to the server.")

    # Read the JPG file
    with open(FILE_PATH, 'rb') as file:
        # Read the file's contents
        file_data = file.read()

    # Send the file size to the server
    s.sendall(len(file_data).to_bytes(4, byteorder='big'))

    # Send the file data to the server
    bytes_sent = 0
    while bytes_sent < len(file_data):
        bytes_to_send = min(BUFFER_SIZE, len(file_data) - bytes_sent)
        s.sendall(file_data[bytes_sent:bytes_sent + bytes_to_send])
        bytes_sent += bytes_to_send

print("File sent successfully.")