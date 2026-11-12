
import socket

# Create TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Host and port
host = '127.0.0.1'
port = 12345

# Bind socket
server.bind((host, port))

# Start listening
server.listen(1)
print("Server is waiting for connection...")

# Accept client connection
conn, addr = server.accept()
print("Connected to:", addr)

# Receive message
message = conn.recv(1024).decode()
print("Client:", message)

# Send response
conn.send("Hello Client! Message received.".encode())

# Close connection
conn.close()
server.close()
