import socket

# Define the server's IP address and port number
def socket_init(message):
    SERVER_HOST = '100.65.3.233'  # If the server is running on the same machine, use 'localhost' or '127.0.0.1'
    SERVER_PORT = 12001         # Make sure it matches the server's port

    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the server
        s.connect((SERVER_HOST, SERVER_PORT))
        print("Connected to the server.")
        s.sendall(message.encode())
        # Receive the response from theh server
        data = s.recv(1024)
        print('Received from server:', data.decode())

def send_socket( s):
        # Prompt the user to input a message
        #message = input("Enter your message: ")
        # Send the message to the server
        pass