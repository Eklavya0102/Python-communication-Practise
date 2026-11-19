# TCP File Transfer Using Python

## 1. Introduction

This project demonstrates file transfer between a TCP client and server using Python socket programming.

The client sends a selected file to the server over a TCP connection. The server receives the file and saves it locally.

TCP ensures reliable, ordered and error-checked data delivery between the client and server.

## 2. Features

- TCP-based client-server communication.
- Transfer files between client and server.
- Supports text files, images, PDFs, documents and other binary files.
- Displays file transfer progress.
- Automatically creates a folder to store received files.
- Uses buffer-based file transmission.

## 3. Technologies Used

- Python 3
- Socket Programming
- TCP Protocol
- JSON
- OS and Struct Modules

## 4. Project Structure

```text
File-Transfer/
│
├── file_client.py
├── file_server.py
└── README.md
```

## 5. How to Run

### Step 1: Start the Server

Open a terminal inside the `File-Transfer` folder and execute:

```bash
python file_server.py
```

### Step 2: Start the Client

Open another terminal and execute:

```bash
python file_client.py
```

### Step 3: Enter File Path

Enter the path of the file you want to transfer.

Example:

```text
Enter the file path: sample.pdf
```

The client will connect to the server and begin transferring the file.

## 6. Output

### Server Output

```text
Server listening on port 5001...
Waiting for client connection...

Connected to: ('127.0.0.1', 54321)
Receiving file: sample.pdf
File size: 102400 bytes
File received successfully!
Saved at: received_files/sample.pdf
```

### Client Output

```text
Enter the file path: sample.pdf

Connecting to server 127.0.0.1:5001...
Connected successfully!
Sending file: sample.pdf

Progress: 100.00%
Waiting for server confirmation...
File transferred successfully!
```

## 7. How It Works

1. The server creates a TCP socket and waits for incoming connections.
2. The client connects to the server using its IP address and port number.
3. The client sends the filename and file size as metadata.
4. The client reads the file in chunks and sends the data through the TCP connection.
5. The server receives the data and writes it into a new file.
6. After successful reception, the server sends a confirmation message to the client.

## 8. Conclusion

This project demonstrates how TCP socket programming can be used to transfer files reliably between two computers. It provides a practical understanding of TCP connections, data transmission, buffering and client-server communication.