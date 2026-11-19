
import socket
import struct
import json
import os

HOST = "127.0.0.1"
PORT = 5001

BUFFER_SIZE = 4096


def send_file(filepath):
    if not os.path.isfile(filepath):
        print("Error: File not found!")
        return

    filename = os.path.basename(filepath)
    filesize = os.path.getsize(filepath)

    # Prepare file information
    header = json.dumps({
        "filename": filename,
        "filesize": filesize
    }).encode("utf-8")

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print(f"Connecting to server {HOST}:{PORT}...")
        client.connect((HOST, PORT))

        print("Connected successfully!")
        print(f"Sending file: {filename}")

        # Send header length and file information
        client.sendall(struct.pack("!I", len(header)))
        client.sendall(header)

        # Send file data
        sent = 0

        with open(filepath, "rb") as file:
            while True:
                data = file.read(BUFFER_SIZE)

                if not data:
                    break

                client.sendall(data)
                sent += len(data)

                percentage = (sent / filesize * 100) if filesize else 100
                print(f"\rProgress: {percentage:.2f}%", end="")

        print("\nWaiting for server confirmation...")

        response = client.recv(1024)

        if response == b"SUCCESS":
            print("File transferred successfully!")
        else:
            print("File transfer failed!")

        client.close()

    except (OSError, ConnectionError) as error:
        print(f"\nConnection error: {error}")


if __name__ == "__main__":
    filepath = input("Enter the file path: ").strip().strip('"')
    send_file(filepath)
