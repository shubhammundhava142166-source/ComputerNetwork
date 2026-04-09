import socket

HOST = '127.0.0.1'  # Server IP
PORT = 8080         # Server Port

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect((HOST, PORT))
print(f"Connected to {HOST}:{PORT}")

while True:
    message = input("Client: ")
    client_socket.send(message.encode())

    if message.lower() == "exit":
        print("Closing connection")
        break

    data = client_socket.recv(1024).decode()

    if not data:
        print("Server disconnected")
        break

    print("Server:", data)

    if data.lower() == "exit":
        print("Server closed connection")
        break

client_socket.close()