# TCP Client-Server Communication Using Python

## 1. Introduction

This project demonstrates the implementation of **TCP (Transmission Control Protocol) Client-Server Communication** using Python socket programming.

TCP is one of the fundamental protocols of the Internet Protocol (IP) suite. It enables reliable communication between two devices over a network by establishing a connection before exchanging data.

This project demonstrates how a TCP server listens for incoming connections, how a client establishes a connection with the server, and how messages are exchanged between them.

The implementation uses Python's built-in `socket` module to establish communication between a client and a server.

---

## 2. Detailed Overview of TCP

### What is TCP?

**TCP (Transmission Control Protocol)** is a connection-oriented transport layer protocol that provides reliable, ordered, and error-checked delivery of data between devices communicating over a network.

It ensures that data sent from one device reaches the destination correctly and in the same order in which it was transmitted.

TCP operates at the **Transport Layer (Layer 4)** of the OSI model.

### Key Characteristics of TCP

1. **Connection-Oriented:** TCP establishes a connection between the sender and receiver before transmitting data.

2. **Reliable Data Transmission:** TCP ensures that transmitted data reaches the destination. Lost segments can be retransmitted.

3. **Ordered Delivery:** Data is delivered to the receiving application in the correct sequence.

4. **Error Detection:** TCP uses checksums to detect errors in transmitted segments.

5. **Acknowledgement:** The receiver sends acknowledgements (ACKs) to confirm successful receipt of data.

6. **Flow Control:** TCP uses a sliding window mechanism to prevent the sender from overwhelming the receiver.

7. **Congestion Control:** TCP adjusts its transmission rate to help prevent network congestion.

8. **Full-Duplex Communication:** Both devices can send and receive data simultaneously.

9. **Byte Stream Protocol:** TCP treats transmitted information as a continuous stream of bytes rather than separate messages.

### TCP in the OSI Model

| OSI Layer | Function |
|---|---|
| Application Layer | Provides network services to applications |
| Presentation Layer | Data formatting and encryption |
| Session Layer | Manages communication sessions |
| Transport Layer | TCP – Reliable data transmission |
| Network Layer | IP addressing and routing |
| Data Link Layer | Frame transmission |
| Physical Layer | Transmission of raw bits |

---

## 3. How TCP Works

TCP communication generally involves three major stages:

### A. Three-Way Handshake

Before exchanging data, TCP establishes a connection using a three-way handshake.

**Step 1: SYN (Synchronize)**

The client sends a SYN packet to the server requesting a connection.

**Step 2: SYN-ACK (Synchronize-Acknowledgement)**

The server responds with a SYN-ACK packet to acknowledge the request.

**Step 3: ACK (Acknowledgement)**

The client sends an ACK packet to confirm the connection.

After these three steps, the TCP connection is established.

### B. Data Transmission

Once the connection is established:

1. The sender divides data into TCP segments.
2. Segments are transmitted through the network.
3. The receiver checks the received data.
4. Acknowledgements are sent to confirm receipt.
5. Missing segments can be retransmitted.
6. Data is reassembled and delivered in order.

### C. Connection Termination

TCP generally uses a four-step process to terminate a connection:

1. **FIN:** One device requests connection termination.
2. **ACK:** The other device acknowledges the request.
3. **FIN:** The other device sends its own termination request.
4. **ACK:** The first device acknowledges it.

The connection is then closed.

---

## 4. TCP Client-Server Architecture

TCP follows a client-server communication model.

### TCP Server

A TCP server is a program that waits for incoming connection requests from clients.

Its responsibilities include:
- Creating a TCP socket.
- Binding the socket to an IP address and port.
- Listening for incoming connections.
- Accepting client connections.
- Receiving and processing client data.
- Sending responses to clients.
- Closing the connection when communication is complete.

### TCP Client

A TCP client is a program that initiates a connection with a TCP server.

Its responsibilities include:
- Creating a TCP socket.
- Specifying the server IP address and port.
- Establishing a connection with the server.
- Sending data to the server.
- Receiving responses.
- Closing the connection.

---

## 5. Python Socket Programming

Python provides a built-in `socket` module for network communication.

A socket acts as an endpoint through which two devices exchange information.

### Important Socket Functions

| Function | Description |
|---|---|
| `socket.socket()` | Creates a socket object |
| `bind()` | Assigns an IP address and port to the server |
| `listen()` | Places the server in listening mode |
| `accept()` | Accepts an incoming client connection |
| `connect()` | Establishes a connection with the server |
| `send()` | Sends data through the socket |
| `recv()` | Receives data through the socket |
| `close()` | Closes the socket connection |

### Socket Parameters

```python
socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

- `AF_INET`: Specifies IPv4 addressing.
- `SOCK_STREAM`: Specifies a TCP stream socket.

### IP Address and Port

- **IP Address:** Identifies a device on a network.
- **Port Number:** Identifies a specific application or service on that device.
- **127.0.0.1:** Also known as localhost, refers to the same computer.
- **12345:** Port number used in this project.

---

## 6. Project Structure

```text
TCP-Client-Server/
│
├── server.py
├── client.py
└── README.md
```

### Files Description

- `server.py`: Creates a TCP server, listens for client connections, receives messages, and sends responses.
- `client.py`: Connects to the TCP server, sends a message, and receives the server's response.
- `README.md`: Contains project documentation and instructions.

---

## 7. How to Execute the Project

### Prerequisites

- Python 3.x installed.
- Basic knowledge of Python.
- A code editor or terminal.

No external Python libraries are required.

### Step 1: Clone the Repository

```bash
git clone <repository-url>
```

### Step 2: Navigate to the Project Directory

```bash
cd TCP-Client-Server
```

### Step 3: Start the Server

Open the first terminal and execute:

```bash
python server.py
```

The server will start listening for incoming connections.

### Step 4: Start the Client

Open a second terminal and execute:

```bash
python client.py
```

The client will connect to the server and exchange messages.

---

## 8. Expected Output

### Server Terminal

```text
Server is waiting for connection...
Connected to: ('127.0.0.1', 54321)
Client: Hello Server!
```

### Client Terminal

```text
Server: Hello Client! Message received.
```

*Note: The client's temporary port number may differ between executions.*

---

## 9. Applications of TCP

TCP is widely used in applications where reliable data transmission is essential.

Some common applications include:

- **Web Browsing:** HTTP and HTTPS communication.
- **Email Services:** SMTP, IMAP and POP3.
- **File Transfer:** FTP and other reliable file-transfer services.
- **Remote Access:** SSH and remote terminal connections.
- **Database Communication:** Reliable communication between applications and database servers.
- **Messaging Applications:** Reliable message delivery and communication.

---

## 10. Advantages of TCP

- Reliable communication between devices.
- Ensures ordered data delivery.
- Provides error detection and retransmission.
- Supports full-duplex communication.
- Provides flow and congestion control.
- Suitable for applications requiring accurate data transfer.

## 11. Limitations of TCP

- Connection establishment introduces additional overhead.
- Generally has more protocol overhead than UDP.
- Retransmissions can increase communication delays.
- Not ideal for applications that prioritize extremely low latency over reliable delivery.
- Maintaining connections consumes network and system resources.

---

## 12. Learning Objectives

Through this project, the following concepts are explored:

- Understanding TCP and its characteristics.
- Learning the client-server architecture.
- Understanding socket programming in Python.
- Implementing TCP communication.
- Working with IP addresses and port numbers.
- Understanding connection establishment and termination.
- Sending and receiving data over a network.

---

## 13. Conclusion

This project provides a basic practical understanding of TCP-based communication using Python.

By implementing a TCP client and server, it demonstrates how two applications establish a connection, exchange messages reliably, and terminate communication.

It serves as a foundation for understanding computer networking and developing more advanced network-based applications.

---

**Technology:** Python | Socket Programming | TCP/IP

**Category:** Computer Networks Practical / Networking Fundamentals

**Purpose:** Educational and practical implementation of TCP client-server communication.