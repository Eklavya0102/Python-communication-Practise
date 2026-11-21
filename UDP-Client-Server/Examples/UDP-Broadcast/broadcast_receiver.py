
import socket

HOST = "0.0.0.0"
PORT = 5002
BUFFER_SIZE = 4096


def start_receiver():
    receiver = socket.socket(
        socket.AF_INET,
        socket.SOCK_DGRAM
    )

    receiver.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1
    )

    receiver.bind((HOST, PORT))

    print("=" * 50)
    print("          UDP BROADCAST RECEIVER")
    print("=" * 50)
    print(f"Listening on port: {PORT}")
    print("Waiting for broadcast messages...")
    print("Press Ctrl+C to stop.\n")

    try:
        while True:
            data, address = receiver.recvfrom(BUFFER_SIZE)

            message = data.decode("utf-8", errors="replace")

            print(f"Sender IP   : {address[0]}")
            print(f"Sender Port : {address[1]}")
            print(f"Message     : {message}")
            print("-" * 50)

    except KeyboardInterrupt:
        print("\nReceiver stopped.")

    finally:
        receiver.close()


if __name__ == "__main__":
    start_receiver()
