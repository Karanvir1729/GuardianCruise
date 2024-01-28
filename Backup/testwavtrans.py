import socket

# Define the server's IP address and port number
def socket_init():
    SERVER_HOST = '100.65.6.83'  # If the server is running on the same machine, use 'localhost' or '127.0.0.1'
    SERVER_PORT = 5570        # Make sure it matches the server's port

    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the server
        s.connect((SERVER_HOST, SERVER_PORT))
        print("Connected to the server.")
        s.sendfile(open(r"C:\Users\dolev\Desktop\Programs\Nostalgic Ride\Backup\Kustavyya.wav", "rb"))
        # Receive the response from theh server
        #data = s.recv(1024)
        #print('Received from server:', data.decode())

def send_socket(s):
        # Prompt the user to input a message
        #message = input("Enter your message: ")
        # Send the message to the server
        pass
socket_init()