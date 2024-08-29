# UDP Chat Application

This is a simple UDP-based chat application written in Python. It allows for communication between a server and one or more clients over a local network.

## Features

- **Server**: Listens for incoming messages from clients and optionally sends a response back.
- **Client**: Sends messages to the server and receives responses.
- **Multi-threaded**: The server runs in a separate thread, allowing clients to start and communicate independently.

## How It Works

1. The server retrieves the local IP address and starts listening on port `12345`.
2. The client connects to the server using its IP address and sends messages.
3. The server receives messages and can respond back to the client.
4. Communication continues until the user interrupts (e.g., using `Ctrl+C`).

## Requirements

- Python 3.x

## Usage

### Running the Server and the CLient
To start the server, run the following command. The server will automatically start in a separate thread and the client will prompt you to enter the IP address of the server.

``` bash
python3 Chat.py
```
Once the client is running, you can start typing messages to send to the server.

### Code Overview
get_local_ip(): Retrieves the local IP address of the machine.
start_server(): Starts a UDP server that listens for incoming messages.
start_client(server_ip): Starts a UDP client that connects to the server using the provided IP address.
main(): Starts the server in a separate thread and then prompts the user to start the client.

### Customization
Port Number: The default port number is 12345. You can change this by modifying the server_address and server_port variables in the code.
Buffer Size: The default buffer size for messages is 1024 bytes. This can be adjusted as needed.

### Contributing
Feel free to fork this repository and submit pull requests. Any improvements or bug fixes are welcome!
