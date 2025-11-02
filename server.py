import socket
import time

HOST = "127.0.0.1"
PORT = 30000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    connection, address = s.accept()

    with connection:
        print(f"{address} connected")
        while True:
            print("Top")
            data = connection.recv(1024)
            if not data:
                print("No data")
            else:
                print(f"Data: {data}")
                connection.sendall(data)