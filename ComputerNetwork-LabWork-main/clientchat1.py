import socket

# Server details
serverAddressPort = ("127.0.0.1", 20001)
bufferSize = 1024

# Create UDP socket
UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        # Take input from user
        message = input("Client: ")

        # Send message
        UDPClientSocket.sendto(message.encode(), serverAddressPort)

        # Exit condition
        if message.lower() == "exit":
            print("Closing client...")
            break

        # Receive response
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        response = msgFromServer[0].decode()

        print("Server:", response)

except Exception as e:
    print("Error:", e)

finally:
    UDPClientSocket.close()