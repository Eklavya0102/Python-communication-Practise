import socket

# Create TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server host and port
host = '127.0.0.1'
port = 12345

# Connect to server
client.connect((host, port))

# Send message
client.send("Hello Server!".encode())

# Receive response
response = client.recv(1024).decode()
print("Server:", response)

# Close connection
client.close()
