import socket
import sys
import threading

# Socket variables
client_HOST = "127.0.0.1"
client_PORT = int(sys.argv[1])
client_ADDRESS = ((client_HOST, client_PORT))

server_HOST = "127.0.0.1"
server_PORT = 30000
server_ADDRESS = ((server_HOST, server_PORT))

def Receive_Messages(sock):
    while True:
        encoded_data = sock.recv(1024)
        
        decoded_data = encoded_data.decode("utf-8")
        sys.stdout.write(f"\r{decoded_data}\nYou: ")
        sys.stdout.flush()

def Send_Messages(sock):
    try:
        while True:
            message = input("You: ")
            sock.sendall(message.encode("UTF-8"))
    except KeyboardInterrupt:
        print("Canceled")
    except:
        print("Unknown Error?")
    

# Create socket
client_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_SOCKET.bind(client_ADDRESS)

# Send a connection request
client_SOCKET.connect(server_ADDRESS)
threading.Thread(target=Receive_Messages, args=(client_SOCKET,)).start()

Send_Messages(client_SOCKET)

client_SOCKET.close()


# Send a message