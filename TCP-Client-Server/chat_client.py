
import socket
import threading

# Create TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 12345

# Connect to server
client.connect((host, port))

print("Connected to Chat Server!")
print("Type 'exit' to end the chat.\n")


# Receive messages
def receive_messages():
    buffer = b""

    while True:
        try:
            data = client.recv(1024)

            if not data:
                print("\nServer disconnected.")
                break

            buffer += data

            while b"\n" in buffer:
                message, buffer = buffer.split(b"\n", 1)
                message = message.decode()

                if message.lower() == "exit":
                    print("\nServer ended the chat.")
                    return

                print("\nServer:", message)

        except OSError:
            break


# Start receiving in a separate thread
thread = threading.Thread(target=receive_messages, daemon=True)
thread.start()

# Send messages
while True:
    try:
        message = input("You: ")

        client.sendall((message + "\n").encode())

        if message.lower() == "exit":
            break

    except (OSError, EOFError):
        break

# Close connection
client.close()

print("Chat Client closed.")
