import socket
import threading

# Create a socket to listen for incoming connections
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 8080))
server_socket.listen(5)

# List to store connected clients
clients = []

# Function to broadcast messages to all connected clients
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                # Remove the client if there's an error
                remove(client)

# Function to remove a client from the list
def remove(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)

# Function to handle client connections
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(f"Received: {message.decode()}")
                broadcast(message, client_socket)
            else:
                remove(client_socket)
        except:
            continue

# Accept and handle client connections
while True:
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)
    print(f"Connected: {client_address}")
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
