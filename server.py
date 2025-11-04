import socket
import threading

# Server Configuration

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 30000
SERVER_ADDRESS = (SERVER_HOST, SERVER_PORT)

# Track all connected clients
connected_clients = []


# Client Class

class Client:
    """
    Represents a connected client.
    Holds the socket and address, and automatically adds itself to the client list.
    """
    def __init__(self, client_socket, address):
        self.socket = client_socket
        self.address = address
        connected_clients.append(self)

    def send(self, message: str):
        """
        Send a UTF-8 encoded message to this client.
        """
        try:
            self.socket.sendall(message.encode("utf-8"))
        except Exception as e:
            print(f"Error sending message to {self.address}: {e}")


# Server Utility Functions

def send_connection_confirmation(client: Client):
    """
    Send a confirmation message to a newly connected client.
    """
    confirmation = f"Server: Connected to {SERVER_ADDRESS}"
    client.send(confirmation)


def broadcast_message(sender: Client, message: str):
    """
    Send a message to all connected clients except the sender.
    """
    for client in connected_clients:
        if client != sender:
            try:
                client.send(message)
            except Exception as e:
                print(f"Error broadcasting to {client.address}: {e}")


def handle_client_messages(client: Client):
    """
    Continuously listen for messages from a specific client.
    Broadcast received messages to all other connected clients.
    """
    try:
        while True:
            data = client.socket.recv(1024)
            if not data:
                break  # Client disconnected

            message = data.decode("utf-8").strip()

            # Handle special commands
            if message == "!kill":
                print(f"{client.address} requested disconnect.")
                break

            formatted_message = f"{client.address}: {message}"
            print(formatted_message)

            # Broadcast to all other clients
            broadcast_message(client, formatted_message)

    except Exception as e:
        print(f"Error handling client {client.address}: {e}")

    finally:
        disconnect_client(client)


def disconnect_client(client: Client):
    """
    Cleanly disconnect a client, close its socket, and remove it from the list.
    """
    try:
        client.socket.shutdown(socket.SHUT_RDWR)
    except Exception:
        pass  # Socket may already be closed

    client.socket.close()

    if client in connected_clients:
        connected_clients.remove(client)

    print(f"Client {client.address} disconnected.")


# Server Main Loop

def start_server():
    """
    Start the TCP chat server and listen for incoming connections.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(SERVER_ADDRESS)
    server_socket.listen()

    print(f"Server started on {SERVER_HOST}:{SERVER_PORT}")
    print("Waiting for connections...")

    try:
        while True:
            client_socket, address = server_socket.accept()
            print(f"New connection from {address}")

            client = Client(client_socket, address)
            send_connection_confirmation(client)

            # Handle messages from the client in a new thread
            threading.Thread(
                target=handle_client_messages,
                args=(client,),
                daemon=True
            ).start()

    except KeyboardInterrupt:
        print("\nServer shutting down (KeyboardInterrupt).")
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        server_socket.close()
        print("Server socket closed.")


# Entry Point

if __name__ == "__main__":
    start_server()
