import socket

# Start making a socket listen for connections & See if they want a connection or are sending a message because we already have a connection

# Socket variables

server_HOST = "127.0.0.1"
server_PORT = 30000
server_ADDRESS = ((server_HOST, server_PORT))

# Create socket
server_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_SOCKET.bind(server_ADDRESS)
server_SOCKET.listen()
client_SOCKET, address = server_SOCKET.accept()
print(f"Connected to {address}")

# Send a comfirmation back
client_SOCKET.send(b'Hello')

# Save the connection once you received a comfirmation of the comfirmation we send
