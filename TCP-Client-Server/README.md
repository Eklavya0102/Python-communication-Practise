# TCP Client-Server Communication Using Python

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Protocol-TCP-green" alt="TCP">
  <img src="https://img.shields.io/badge/Socket-Programming-purple" alt="Socket Programming">
</p>

## 1. Introduction

This project demonstrates TCP (Transmission Control Protocol) client-server communication using Python socket programming.

TCP is a connection-oriented transport layer protocol that provides reliable and ordered data transmission between devices.

This implementation demonstrates how a TCP server listens for incoming connections, how a client establishes a connection with the server, and how messages are exchanged between them.

The project also includes a TCP chat application with separate server and client programs.

## 2. Detailed Overview of TCP

### What is TCP?

**TCP (Transmission Control Protocol)** is a connection-oriented transport layer protocol that provides reliable, ordered, and error-checked delivery of data between devices communicating over a network.

TCP operates at the Transport Layer (Layer 4) of the OSI model.

### Key Characteristics of TCP

1. **Connection-Oriented:** Establishes a connection before data transmission.
2. **Reliable Data Transmission:** Lost segments can be retransmitted.
3. **Ordered Delivery:** Data is delivered to the receiving application in sequence.
4. **Error Detection:** Uses checksums to detect errors.
5. **Acknowledgement:** Uses acknowledgements to confirm receipt of data.
6. **Flow Control:** Helps prevent the sender from overwhelming the receiver.
7. **Congestion Control:** Adjusts transmission to help manage network congestion.
8. **Full-Duplex Communication:** Both devices can send and receive data.
9. **Byte Stream:** Treats transmitted information as a continuous stream of bytes.

## 3. How TCP Works

TCP communication generally involves three major stages.

### A. Three-Way Handshake

Before exchanging data, TCP establishes a connection using a three-way handshake.

1. **SYN:** The client sends a connection request to the server.
2. **SYN-ACK:** The server acknowledges the request.
3. **ACK:** The client confirms the connection.

After these three steps, the TCP connection is established.

### B. Data Transmission

Once the connection is established:

1. The sender transmits data.
2. TCP divides the data into segments as required.
3. The receiver acknowledges received data.
4. Missing segments can be retransmitted.
5. Data is delivered to the receiving application in order.

### C. Connection Termination

TCP normally uses a FIN and ACK exchange from both sides to close a connection gracefully.

## 4. TCP Client-Server Architecture

### TCP Server

A TCP server waits for incoming connection requests from clients.

Its responsibilities include:

- Creating a TCP socket.
- Binding the socket to an IP address and port.
- Listening for incoming connections.
- Accepting a client connection.
- Receiving client data.
- Sending a response.
- Closing the connection.

### TCP Client

A TCP client initiates a connection with a TCP server.

Its responsibilities include:

- Creating a TCP socket.
- Specifying the server IP address and port.
- Establishing a connection.
- Sending data to the server.
- Receiving the server's response.
- Closing the socket.

## 5. Python Socket Programming

Python provides a built-in `socket` module for network communication.

### TCP Socket Creation

```python
import socket

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
```

- `AF_INET`: Specifies IPv4 addressing.
- `SOCK_STREAM`: Specifies TCP communication.

### Important TCP Socket Functions

| Function | Description |
|---|---|
| `socket()` | Creates a socket object |
| `bind()` | Assigns an IP address and port |
| `listen()` | Places the server in listening mode |
| `accept()` | Accepts an incoming client connection |
| `connect()` | Establishes a connection with the server |
| `send()` | Sends data |
| `sendall()` | Sends all supplied data |
| `recv()` | Receives data |
| `close()` | Closes the socket |

### IP Address and Port

- **IP Address:** Identifies a device on a network.
- **Port Number:** Identifies a specific application or service.
- **127.0.0.1:** The IPv4 loopback address, also known as localhost.

## 6. Project Structure

```text
TCP-Client-Server/
│
├── server.py
├── client.py
├── README.md
│
└── Examples/
    ├── chat_server.py
    └── chat_client.py
```

### Files Description

| File | Description |
|---|---|
| `server.py` | Creates the TCP server and handles client communication |
| `client.py` | Connects to the TCP server and exchanges messages |
| `Examples/chat_server.py` | Server-side program for the TCP chat application |
| `Examples/chat_client.py` | Client-side program for the TCP chat application |
| `README.md` | Documentation and execution instructions |

## 7. Requirements

- Python 3.x installed.
- A code editor or terminal.
- Basic knowledge of Python.
- Two terminal windows for client-server communication.

No external Python libraries are required for the described implementation.

## 8. Installation and Execution

### Step 1: Clone the Repository

```bash
git clone https://github.com/Eklavya0102/Python-communication-Practise.git
```

### Step 2: Navigate to the Repository

```bash
cd Python-communication-Practise
```

### Step 3: Start the TCP Server

Open the first terminal:

```bash
python TCP-Client-Server/server.py
```

### Step 4: Start the TCP Client

Open a second terminal:

```bash
python TCP-Client-Server/client.py
```

The client will connect to the server and exchange messages.

## 9. TCP Chat Application

The `Examples` folder contains a TCP chat application with two separate programs:

- `chat_server.py` – Handles the server side of the chat.
- `chat_client.py` – Handles the client side of the chat.

The application demonstrates interactive communication between a TCP client and server.

### How to Run the TCP Chat Application

**Terminal 1 – Start the Chat Server**

```bash
python TCP-Client-Server/Examples/chat_server.py
```

**Terminal 2 – Start the Chat Client**

```bash
python TCP-Client-Server/Examples/chat_client.py
```

Start the server before running the client.

*The exact chat interaction and termination command depend on the implementation in the example files.*

## 10. Expected Output

The following is an illustrative example of basic TCP client-server communication. Actual messages depend on the code.

**Server Terminal**

```text
Server is waiting for connection...
Connected to: ('127.0.0.1', 54321)
Client: Hello Server!
```

**Client Terminal**

```text
Server: Hello Client! Message received.
```

*Note: The client's temporary port number may differ between executions.*

## 11. Applications of TCP

TCP is widely used where reliable data transmission is important.

- **Web Browsing:** HTTP and HTTPS communication.
- **Email Services:** SMTP, IMAP, and POP3.
- **File Transfer:** Reliable file transfer.
- **Remote Access:** SSH and remote terminal connections.
- **Database Communication:** Communication between applications and database servers.
- **Messaging Applications:** Reliable message exchange.

## 12. Advantages of TCP

- Reliable communication between devices.
- Ensures ordered data delivery.
- Provides error detection and retransmission.
- Supports full-duplex communication.
- Provides flow and congestion control.
- Suitable for applications requiring accurate data transfer.

## 13. Limitations of TCP

- Connection establishment introduces overhead.
- Generally has more protocol overhead than UDP.
- Retransmissions can increase communication delays.
- Maintaining connections consumes network and system resources.
- Not ideal for applications that prioritize extremely low latency over reliable delivery.

## 14. Learning Objectives

Through this project, the following concepts are explored:

- Understanding TCP and its characteristics.
- Learning client-server architecture.
- Understanding socket programming in Python.
- Implementing TCP communication.
- Working with IP addresses and port numbers.
- Understanding connection establishment and termination.
- Sending and receiving data over a network.
- Exploring TCP-based chat communication.

## 15. Conclusion

This project provides practical experience with TCP-based communication using Python.

By implementing a TCP client, server, and chat application, it demonstrates how two applications establish a connection, exchange messages reliably, and terminate communication.

It serves as a foundation for understanding computer networking and developing more advanced network-based applications.

## 16. References

- [Python Socket Programming Documentation](https://docs.python.org/3/library/socket.html)
- [Python Threading Documentation](https://docs.python.org/3/library/threading.html)
- [RFC 9293 – Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293)

---

**Technology:** Python | Socket Programming | TCP/IP

**Category:** Computer Networks Practical / Networking Fundamentals

**Purpose:** Educational implementation of TCP client-server communication.

[Back to Main Repository](../README.md) | [UDP Implementation](../UDP-Client-Server/README.md)