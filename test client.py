import socket
host = "100.65.1.28"
port = 6002
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the server
    s.connect((host, port))
    s.sendall("Jeff is currently asleep while driving".encode())