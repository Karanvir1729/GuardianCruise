import socket

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('100.65.3.233', 12345)  # Change this to your desired IP address and port
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print(f"Server listening on {server_address}")

while True:
    # Wait for a connection
    print("Waiting for a connection...")
    client_socket, client_address = server_socket.accept()
    print(f"Connection established from {client_address}")

    try:
        # Receive data in chunks
        data = b''
        while True:
            chunk = client_socket.recv(1024)
            if not chunk:
                break
            data += chunk

        # Decode the received data and print it
        received_data = data.decode()
        print(f"Received data: {received_data}")

    finally:
        # Clean up the connection
        client_socket.close()