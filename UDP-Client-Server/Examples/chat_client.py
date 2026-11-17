
import socket
import threading

# Create UDP socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = '127.0.0.1'
port = 12345

server_address = (host, port)

print("Connected to UDP Chat Server!")
print("Type 'exit' to end the chat.\n")


# Receive messages
def receive_messages():
    while True:
        try:
            message, address = client.recvfrom(1024)

            message = message.decode()

            if message.lower() == "exit":
                print("\nServer ended the chat.")
                break

            print("\nServer:", message)

        except OSError:
            break


# Start receiving thread
thread = threading.Thread(target=receive_messages, daemon=True)
thread.start()

# Send messages
while True:
    try:
        message = input("You: ")

        client.sendto(message.encode(), server_address)

        if message.lower() == "exit":
            break

    except (OSError, EOFError):
        break

client.close()

print("UDP Chat Client closed.")
