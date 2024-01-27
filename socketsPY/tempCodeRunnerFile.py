import socket
import threading

def handle_client(client_socket):
    while True:
        # Receive data from the client
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break

        # Print the received message
        print(f"Received message: {data}")

        # Send a response back to the client
        response = input("Enter your response: ")
        client_socket.send(response.encode('utf-8'))

    # Close the client socket when the loop exits
    client_socket.close()

def start_server():
    # Create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server.bind(('100.65.6.83', 12345))

    # Listen for incoming connections (max 5 connections in the queue)
    server.listen(5)
    print("Server listening on port 12345...")

    while True:
        # Accept a connection from a client
        client, addr = server.accept()
        print(f"Accepted connection from {addr}")

        # Start a new thread to handle the client
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
