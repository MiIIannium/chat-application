import socket
import sys
import threading


# Utility Functions

def find_available_port(start=30000, end=40000):
    """
    Find the first available TCP port within the given range.

    Args:
        start (int): Starting port number to check.
        end (int): Ending port number to check.

    Returns:
        int: The first available port number, or None if none are found.
    """
    for port in range(start, end):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("127.0.0.1", port))
                return port
            except OSError:
                continue
    return None


def send_message(sock, message):
    """
    Send a UTF-8 encoded message through the given socket.
    """
    sock.sendall(message.encode("utf-8"))


def receive_messages(sock):
    """
    Continuously listen for incoming messages from the server and print them.
    """
    try:
        while True:
            data = sock.recv(1024)
            if not data:
                print("Server closed the connection.")
                sock.close()
                break

            message = data.decode("utf-8")
            sys.stdout.write(f"\r{message}\n")
            sys.stdout.flush()

    except Exception as e:
        print(f"Error receiving messages: {e}")
        sock.close()



# Client Setup

def get_client_port():
    """
    Ask the user for a port, validate it, or generate one if needed.
    """
    user_input = input("Port: ").strip()

    if not user_input:
        print("No port entered, generating one automatically...")
        return find_available_port()

    try:
        port = int(user_input)
        # Check if port is available
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("127.0.0.1", port))
        return port
    except (ValueError, OSError):
        print("Invalid or unavailable port. Generating one automatically...")
        return find_available_port()



# Main Client Logic

def main():
    client_host = "127.0.0.1"
    client_port = get_client_port()
    server_host = "127.0.0.1"
    server_port = 30000

    client_address = (client_host, client_port)
    server_address = (server_host, server_port)

    print(f"Using client port: {client_port}")

    # Create and bind the client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.bind(client_address)

    try:
        # Connect to the server
        client_socket.connect(server_address)

        # Receive initial confirmation message
        initial_response = client_socket.recv(1024).decode("utf-8")
        print(initial_response)

        # Start a thread to handle incoming messages
        threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

        # Handle user input and sending messages
        while True:
            message = input()
            if message.startswith("!"):
                print("Command detected (not yet implemented).")
            else:
                send_message(client_socket, message)

    except KeyboardInterrupt:
        print("\nConnection closed by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client_socket.close()


if __name__ == "__main__":
    main()
