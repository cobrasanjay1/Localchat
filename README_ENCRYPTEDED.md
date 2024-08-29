# Encrypted UDP Chat Application
This is an enhanced version of a simple UDP-based chat application written in Python, now featuring encryption for secure communication between a server and one or more clients over a local network. The encryption is implemented using the cryptography library's Fernet symmetric encryption.

## Features
Server: Listens for incoming encrypted messages from clients and optionally sends an encrypted response back.
Client: Sends encrypted messages to the server and receives encrypted responses.
Multi-threaded: The server runs in a separate thread, allowing clients to start and communicate independently.
Encryption: All communication between the server and clients is encrypted using Fernet symmetric encryption.

## How It Works
A unique encryption key is generated at runtime, which is used to encrypt and decrypt all messages.
The server retrieves the local IP address and starts listening on port 12345.
The client connects to the server using its IP address and sends encrypted messages.
The server receives the encrypted messages, decrypts them, and can respond with an encrypted message.
Communication continues until the user interrupts (e.g., using Ctrl+C).

## Requirements
Python 3.x
cryptography library (install using pip install cryptography)

## Usage

### Running the Server and the CLient
To start the server, run the following command. The server will automatically start in a separate thread and the client will prompt you to enter the IP address of the server.

``` bash
Copy code
python3 Chat.py
```
Once the client is running, you can start typing messages to send to the server.

### Code Overview
get_local_ip(): Retrieves the local IP address of the machine.
start_server(): Starts a UDP server that listens for incoming encrypted messages and responds with encrypted messages.
start_client(server_ip): Starts a UDP client that connects to the server using the provided IP address and handles encryption and decryption of messages.
main(): Starts the server in a separate thread and then prompts the user to start the client.

### Customization
Port Number: The default port number is 12345. You can change this by modifying the server_address and server_port variables in the code.
Buffer Size: The default buffer size for messages is 1024 bytes. This can be adjusted as needed.
Encryption Key: The encryption key is generated at runtime using Fernet.generate_key(). If you want to use a fixed key for encryption/decryption, you can set it manually by modifying the key variable.
Security Considerations
Key Management: The encryption key is generated at runtime and is not persisted, meaning it will be different each time you run the application. For a real-world application, securely store and manage the encryption key.
Symmetric Encryption: Since Fernet uses symmetric encryption, the same key is used for both encryption and decryption. Ensure that the key is kept secure and only shared between trusted parties.

### Contributing
Feel free to fork this repository and submit pull requests. Any improvements or bug fixes are welcome!
