import socket
import threading
import time

def get_local_ip():
    """Retrieve the local IP address of the machine."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as temp_sock:
            temp_sock.connect(('8.8.8.8', 80))  # Google DNS server
            local_ip = temp_sock.getsockname()[0]
        return local_ip
    except Exception as e:
        print(f"Error retrieving local IP address: {e}")
        return '127.0.0.1'  # Fallback to localhost

def start_server():
    local_ip = get_local_ip()  # Get the local IP address
    server_address = (local_ip, 12345)  # Bind to the local IP address and port
    buffer_size = 1024  # Size of the buffer to receive messages

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(server_address)
    print(f"Server listening on {server_address}")

    try:
        while True:
            # Receive message
            message, client_address = sock.recvfrom(buffer_size)
            print(f"Received message from {client_address}: {message.decode('utf-8')}")

            # Optionally send a response back to the client
            response = "Message received"
            sock.sendto(response.encode('utf-8'), client_address)
    except KeyboardInterrupt:
        print("Server shutting down.")
    finally:
        sock.close()

def start_client(server_ip):
    buffer_size = 1024  # Size of the buffer to receive messages
    server_port = 12345  # Hardcoded port number for the client

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        while True:
            # Send message
            message = input("Enter message: ")
            sock.sendto(message.encode('utf-8'), (server_ip, server_port))

            # Receive response
            response, _ = sock.recvfrom(buffer_size)
            print(f"Server response: {response.decode('utf-8')}")
    except KeyboardInterrupt:
        print("Client shutting down.")
    finally:
        sock.close()

def main():
    # Start the server first
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()

    # Give the server a moment to start
    time.sleep(2)

    # Get the receiver's IP address from the user
    receiver_ip = input("Enter the receiver's IP address: ")

    # Start client functionality
    print("Client started. Type messages to send.")
    start_client(receiver_ip)

if __name__ == "__main__":
    main()

