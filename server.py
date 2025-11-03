import socket
import threading

# Start making a socket listen for connections & See if they want a connection or are sending a message because we already have a connection

# Socket variables

server_HOST = "127.0.0.1"
server_PORT = 30000
server_ADDRESS = ((server_HOST, server_PORT))

clients_LIST = []

# Create socket
server_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_SOCKET.bind(server_ADDRESS)
server_SOCKET.listen()

# Client class
class Client():
    def __init__(self, socket, address):
        self.socket = socket
        self.address = address
        clients_LIST.append(self)

# Send a comfirmation back
def Connection_Comfirmation(sock_object):
    message = "Server: Connected to " + str(server_ADDRESS)
    sock_object.socket.send(message.encode("utf-8"))

def Broadcast(sender_sock_object, message):
    for client in clients_LIST:
        if client != sender_sock_object:
            client.socket.send(bytes(message, "utf-8"))

def Receiving_Messages(sock_object):
        try:
            while True:
                encoded_data = sock_object.socket.recv(1024)
                decoded_data = encoded_data.decode("utf-8")

                if encoded_data is None:
                    print("None")
                    break

                message = str(sock_object.address) + ": " + decoded_data
                print(message)

                # Broadcast
                Broadcast(sock_object, message)
        finally:
            clients_LIST.remove(sock_object)
            print("Disconnected")
            

def connection_accepting():
    try:
        while True:
            client_SOCKET, address = server_SOCKET.accept()
            print(f"Connected to {address}")

            client_object = Client(client_SOCKET, address)

            Connection_Comfirmation(client_object)  # Sends a message back to the client telling them they are successfully connected

            client_listening_thread = threading.Thread(target=Receiving_Messages, args=(client_object,))  # The thread that listens for messages from the client
            client_listening_thread.start()
    except:
        print("Unknown Error?")

    server_SOCKET.close()

connection_accepting()


# Save the connection once you received a comfirmation of the comfirmation we send
