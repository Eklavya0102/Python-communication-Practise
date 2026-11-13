
import socket
import threading

# Create TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 12345

# Bind and listen
server.bind((host, port))
server.listen(1)

print("Chat Server is waiting for connection...")

# Accept client
conn, addr = server.accept()
print("Client connected:", addr)
print("Type 'exit' to end the chat.\n")


# Receive messages
def receive_messages():
    buffer = b""

    while True:
        try:
            data = conn.recv(1024)

            if not data:
                print("\nClient disconnected.")
                break

            buffer += data

            while b"\n" in buffer:
                message, buffer = buffer.split(b"\n", 1)
                message = message.decode()

                if message.lower() == "exit":
                    print("\nClient ended the chat.")
                    return

                print("\nClient:", message)

        except OSError:
            break


# Start receiving in a separate thread
thread = threading.Thread(target=receive_messages, daemon=True)
thread.start()

# Send messages
while True:
    try:
        message = input("You: ")

        conn.sendall((message + "\n").encode())

        if message.lower() == "exit":
            break

    except (OSError, EOFError):
        break

# Close connection
conn.close()
server.close()

print("Chat Server closed.")
