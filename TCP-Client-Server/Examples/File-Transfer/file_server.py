
import socket
import struct
import json
import os

HOST = "0.0.0.0"
PORT = 5001

BUFFER_SIZE = 4096
SAVE_DIR = "received_files"


def receive_exact(sock, size):
    data = bytearray()

    while len(data) < size:
        packet = sock.recv(min(BUFFER_SIZE, size - len(data)))

        if not packet:
            raise ConnectionError("Connection lost during transfer.")

        data.extend(packet)

    return bytes(data)


def start_server():
    os.makedirs(SAVE_DIR, exist_ok=True)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((HOST, PORT))
    server.listen(5)

    print(f"Server listening on port {PORT}...")
    print("Waiting for client connection...\n")

    try:
        while True:
            conn, addr = server.accept()

            with conn:
                print(f"Connected to: {addr}")

                try:
                    # Receive header length
                    header_size = struct.unpack(
                        "!I", receive_exact(conn, 4)
                    )[0]

                    # Receive file information
                    header = json.loads(
                        receive_exact(conn, header_size).decode("utf-8")
                    )

                    filename = os.path.basename(header["filename"])
                    filesize = header["filesize"]

                    if not filename or filesize < 0:
                        raise ValueError("Invalid file information.")

                    filepath = os.path.join(SAVE_DIR, filename)

                    print(f"Receiving file: {filename}")
                    print(f"File size: {filesize} bytes")

                    received = 0

                    with open(filepath, "wb") as file:
                        while received < filesize:
                            chunk = conn.recv(
                                min(BUFFER_SIZE, filesize - received)
                            )

                            if not chunk:
                                raise ConnectionError(
                                    "File transfer interrupted."
                                )

                            file.write(chunk)
                            received += len(chunk)

                    conn.sendall(b"SUCCESS")

                    print("File received successfully!")
                    print(f"Saved at: {filepath}\n")

                except (ConnectionError, ValueError, KeyError,
                        json.JSONDecodeError, OSError) as error:

                    print(f"Transfer failed: {error}")

                    try:
                        conn.sendall(b"FAILED")
                    except OSError:
                        pass

    except KeyboardInterrupt:
        print("\nServer shutting down...")

    finally:
        server.close()


if __name__ == "__main__":
    start_server()
