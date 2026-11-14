
import socket
import threading

# Create UDP socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = '127.0.0.1'
port = 12345

# Bind socket
server.bind((host, port))

print("UDP Chat Server is waiting for connection...")
print("Type 'exit' to end the chat.\n")

client_address = None
running = True


# Receive messages
def receive_messages():
    global client_address, running

    while running:
        try:
            message, address = server.recvfrom(1024)
            client_address = address

            message = message.decode()

            if message.lower() == "exit":
                print("\nClient ended the chat.")
                break

            print("\nClient:", message)

        except OSError:
            break


# Start receiving thread
thread = threading.Thread(target=receive_messages, daemon=True)
thread.start()

# Send messages
while True:
    try:
        message = input("You: ")

        if client_address is not None:
            server.sendto(message.encode(), client_address)

        if message.lower() == "exit":
            break

    except (OSError, EOFError):
        break

running = False
server.close()

print("UDP Chat Server closed.")
