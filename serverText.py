import socket

# Define the host and port on which the server will listen
HOST = '100.65.3.233'  # Indicates that the server will accept connections from any network interface
PORT = 12001      # Port number (you can choose any available port)
import threading
# Create a socket object
def handle_client(conn, addr):
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            print('Connection closed by', addr)
            break
        print('Received:', data.decode())
        # Echo back the received data to the client
        conn.sendall(data)
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