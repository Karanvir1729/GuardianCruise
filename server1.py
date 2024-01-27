import socket
import time

# Define the server's IP address and port number
SERVER_HOST = '100.65.1.28'  # Replace this with your server's IP address
SERVER_PORT = 65432          # Replace this with your server's port

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the server
    s.connect((SERVER_HOST, SERVER_PORT))
    print("Connected to the server.")

    # Send "1" to the server every 5 seconds
    while True:
        try:
            s.sendall(b'1')
            #print("Sent '1' to the server.")
            # Receive response from the server
            response = s.recv(1024)
            if response:
                print("Received response from the server:", response.decode())
            time.sleep(5)  # Sleep for 5 seconds
        except Exception as e:
            print(f"Error communicating with the server: {e}")
            break
