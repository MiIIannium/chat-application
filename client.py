import socket
import sys
print(sys.argv[1])
# Socket variables
client_HOST = "127.0.0.1"
client_PORT = int(sys.argv[1])
client_ADDRESS = ((client_HOST, client_PORT))

server_HOST = "127.0.0.1"
server_PORT = 30000
server_ADDRESS = ((server_HOST, server_PORT))

# Create socket
client_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_SOCKET.bind(client_ADDRESS)

# Send a connection request
client_SOCKET.connect(server_ADDRESS)

while True:
    message = input("Message: ")
    client_SOCKET.send(bytes(message, "UTF-8"))

client_SOCKET.close()


# Send a message