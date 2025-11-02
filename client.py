import socket

HOST = "127.0.0.1"
PORT = 30000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        message = input("Message: ")
        s.sendall(bytes(message, 'utf-8'))
        data = s.recv(1024)
        print(f"received {data!r}")