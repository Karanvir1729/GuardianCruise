import socket

def start_client():
    # Create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client.connect(('100.65.6.83', 5555))

    while True:
        # Send a message to the server
        message = input("Enter your message: ")
        client.send(message.encode('utf-8'))

        # Receive the response from the server
        response = client.recv(1024).decode('utf-8')
        print(f"Server response: {response}")

if __name__ == "__main__":
    start_client()
