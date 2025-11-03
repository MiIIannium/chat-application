import socket
import threading

# Start making a socket listen for connections & See if they want a connection or are sending a message because we already have a connection

# Socket variables

server_HOST = "127.0.0.1"
server_PORT = 30000
server_ADDRESS = ((server_HOST, server_PORT))

clients_LIST = []

# Client class
class Client():
    def __init__(self, socket, address):
        self.socket = socket
        self.address = address

    # Send a comfirmation back
    def Affirmation(self):
        self.socket.send(b'Affirmative')

    def Listening(self):
        while True:
            message = self.socket.recv(1024)

            if message is None:
                print("None")

            print(message)

            # Broadcast

# Create socket
server_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_SOCKET.bind(server_ADDRESS)
server_SOCKET.listen()

while True:
    client_SOCKET, address = server_SOCKET.accept()
    print(f"Connected to {address}")
    client_object = Client(client_SOCKET, address)
    clients_LIST.append(client_object)
    print("1")
    client_thread = threading.Thread(target=client_object.Affirmation)
    client_thread.start()
    client_listening_thread = threading.Thread(target=client_object.Listening)
    client_listening_thread.start()

# Save the connection once you received a comfirmation of the comfirmation we send
