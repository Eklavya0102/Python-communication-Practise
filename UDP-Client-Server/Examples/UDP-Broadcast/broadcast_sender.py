
import socket

BROADCAST_IP = "255.255.255.255"
PORT = 5002


def start_sender():
    sender = socket.socket(
        socket.AF_INET,
        socket.SOCK_DGRAM
    )

    # Enable UDP broadcasting
    sender.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_BROADCAST,
        1
    )

    print("=" * 50)
    print("           UDP BROADCAST SENDER")
    print("=" * 50)
    print(f"Broadcast IP : {BROADCAST_IP}")
    print(f"Port         : {PORT}")
    print("Type 'exit' to stop broadcasting.\n")

    try:
        while True:
            message = input("Enter message: ")

            if message.lower() == "exit":
                print("Broadcast sender stopped.")
                break

            if not message.strip():
                print("Message cannot be empty!\n")
                continue

            sender.sendto(
                message.encode("utf-8"),
                (BROADCAST_IP, PORT)
            )

            print("Message broadcast successfully!\n")

    except KeyboardInterrupt:
        print("\nSender stopped.")

    finally:
        sender.close()


if __name__ == "__main__":
    start_sender()
