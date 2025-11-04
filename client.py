import socket
import sys
import threading

def Receive_Messages(sock):
    try:
        while True:
            encoded_data = sock.recv(1024)
            
            if not encoded_data:
                print("Server closed the connection")
                sock.close()
                break
                
            decoded_data = encoded_data.decode("utf-8")
            sys.stdout.write(f"\r{decoded_data}\n")
            sys.stdout.flush()
    except:
        print("Exception")

def Send_Messages(sock, message):
    sock.sendall(message.encode("UTF-8"))
    
def generate_port():
    print("Generating Port")
    for port in range(30000, 40000):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("127.0.0.1", port))
                return port
            except:
                continue  # Port is available
    return None  # No available ports found

# Socket variables
# Client Socket
client_HOST = "127.0.0.1"
client_PORT = input("Port: ")

if client_PORT == "":
    client_PORT = generate_port()
else:
    try:
        int(client_PORT)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind("127.0.0.1", client_PORT)
    except:
        print("Invalid port/input")
        client_PORT = generate_port()

print(client_PORT)
client_ADDRESS = ((client_HOST, client_PORT))

# Server socket
server_HOST = "127.0.0.1"
server_PORT = 30000
server_ADDRESS = ((server_HOST, server_PORT))

# Create socket
client_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_SOCKET.bind(client_ADDRESS)

# Send a connection request
client_SOCKET.connect(server_ADDRESS)

# Comfirmation message send by server
encoded_data = client_SOCKET.recv(1024)
decoded_data = encoded_data.decode("utf-8")
print(decoded_data)

receive_messages_thread = threading.Thread(target=Receive_Messages, args=(client_SOCKET,))
receive_messages_thread.start()

try:
    while True:
        message = input()
        if message.startswith("!"):
            print("Command")
        else:
            Send_Messages(client_SOCKET, message)
except KeyboardInterrupt:
    pass
except:
    pass

print("Connection Closed")
client_SOCKET.close()