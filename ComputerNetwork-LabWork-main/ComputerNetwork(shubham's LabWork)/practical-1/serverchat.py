import socket

HOST = '0.0.0.0'   # Listen on all interfaces
PORT = 8080

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind and listen
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Server listening on {HOST}:{PORT}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connected to {client_address}")

    while True:
        data = client_socket.recv(1024).decode()

        if not data:
            print("Client disconnected")
            break

        print("Client:", data)

        # Exit condition
        if data.lower() == "exit":
            print("Closing connection with client")
            break

        response = input("Server: ")
        client_socket.send(response.encode())

        if response.lower() == "exit":
            break

    client_socket.close()