import socket
import threading

# Function to receive and display messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            print("Connection closed.")
            client_socket.close()
            break

# Create a socket to connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 8080))  # Replace with the server's IP address

# Start a thread to receive messages from the server
receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

# Main loop to send messages to the server
while True:
    message = input()
    client_socket.send(message.encode())
