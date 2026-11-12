
import socket

# Create UDP socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server host and port
host = '127.0.0.1'
port = 12345

# Send message to server
client.sendto("Hello Server!".encode(), (host, port))

# Receive response
response, address = client.recvfrom(1024)

print("Server:", response.decode())

# Close socket
client.close()
