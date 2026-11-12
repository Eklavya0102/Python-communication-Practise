
import socket

# Create UDP socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Host and port
host = '127.0.0.1'
port = 12345

# Bind socket
server.bind((host, port))

print("UDP Server is waiting for messages...")

# Receive message from client
message, address = server.recvfrom(1024)

print("Connected to:", address)
print("Client:", message.decode())

# Send response
server.sendto(
    "Hello Client! Message received.".encode(),
    address
)

# Close socket
server.close()
