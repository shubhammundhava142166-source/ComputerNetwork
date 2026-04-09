import socket

# Server details
localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

# Create UDP socket
UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind socket
UDPServerSocket.bind((localIP, localPort))

print("UDP server is up and listening...")

while True:
    # Receive data from client
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    
    message = bytesAddressPair[0].decode()
    address = bytesAddressPair[1]

    print(f"Message from Client: {message}")
    print(f"Client Address: {address}")

    # Response message
    response = "Hello UDP Client"

    # Send response back
    UDPServerSocket.sendto(response.encode(), address)