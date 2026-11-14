# Python Network Programming – TCP & UDP Client-Server Communication

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![TCP](https://img.shields.io/badge/Protocol-TCP-green)
![UDP](https://img.shields.io/badge/Protocol-UDP-orange)
![Networking](https://img.shields.io/badge/Domain-Computer%20Networks-purple)
![Status](https://img.shields.io/badge/Status-Learning%20%26%20Practice-success)

## 1. Introduction

This repository contains practical implementations of **TCP (Transmission Control Protocol)** and **UDP (User Datagram Protocol)** client-server communication using Python socket programming.

The project is developed to understand the fundamentals of computer networking, transport layer protocols, and client-server architecture.

It demonstrates how two applications communicate over a network using different transport protocols, exchange messages, and handle data transmission.

The repository includes basic TCP and UDP communication programs along with a TCP Chat Application that demonstrates continuous two-way communication using multithreading.

Both protocols are implemented using Python's built-in `socket` module without requiring any external networking libraries.

---

## 2. Project Overview

The repository is divided into two main sections:

### A. TCP Client-Server Communication

TCP is a connection-oriented transport layer protocol that provides reliable, ordered, and error-checked data transmission.

In this implementation:

- The server creates a TCP socket and waits for client connections.
- The client establishes a connection with the server.
- The client sends a message to the server.
- The server receives the message and sends a response.
- Both sides close the connection after communication.

**Additional Implementation – TCP Chat Application:**

- Enables continuous two-way communication between client and server.
- Supports multiple messages during a single connection.
- Uses Python multithreading to handle sending and receiving simultaneously.
- Allows users to terminate the chat using the `exit` command.

### B. UDP Client-Server Communication

UDP is a connectionless transport layer protocol that allows applications to exchange data without establishing a connection beforehand.

In this implementation:

- The server creates a UDP socket and binds it to an IP address and port.
- The client sends a datagram directly to the server.
- The server receives the message and identifies the sender.
- The server sends a response to the client.
- Both sides close their sockets after communication.

---

## 3. Understanding TCP

### What is TCP?

**TCP (Transmission Control Protocol)** is a connection-oriented transport layer protocol that ensures reliable and ordered delivery of data between devices over a network.

It establishes a connection before transmitting data and uses acknowledgements, sequence numbers, retransmissions, flow control, and congestion control to support reliable communication.

TCP operates at the **Transport Layer (Layer 4)** of the OSI model.

### Characteristics of TCP

- Connection-oriented communication.
- Reliable data transmission.
- Ordered data delivery.
- Error detection using checksums.
- Acknowledgement mechanism.
- Retransmission of lost segments.
- Flow control using a sliding window.
- Congestion control.
- Full-duplex communication.
- Byte-stream-based transmission.

### TCP Three-Way Handshake

TCP establishes a connection using three steps:

1. **SYN:** Client requests a connection.
2. **SYN-ACK:** Server acknowledges the request.
3. **ACK:** Client confirms the connection.

After these steps, data transmission begins.

### TCP Applications

- Web browsing (HTTP/HTTPS).
- Email communication.
- File transfer.
- Remote access (SSH).
- Database communication.
- Chat applications.

---

## 4. Understanding UDP

### What is UDP?

**UDP (User Datagram Protocol)** is a connectionless transport layer protocol that allows applications to transmit data in the form of independent datagrams without establishing a connection beforehand.

It provides low communication overhead and is commonly used in applications where speed and low latency are important.

UDP operates at the **Transport Layer (Layer 4)** of the OSI model.

### Characteristics of UDP

- Connectionless communication.
- No connection establishment.
- No built-in acknowledgement mechanism.
- No automatic retransmission.
- No guarantee of packet ordering.
- Low protocol overhead.
- Fast communication.
- Datagram-based transmission.
- Checksum-based error detection.
- No built-in flow control.
- No built-in congestion control.

### UDP Communication Process

1. Client creates a UDP socket.
2. Client specifies the server's IP address and port.
3. Client sends a datagram using `sendto()`.
4. Server receives the datagram using `recvfrom()`.
5. Server processes the message.
6. Server sends a response using `sendto()`.

Unlike TCP, UDP does not require a three-way handshake.

### UDP Applications

- Online gaming.
- Live video streaming.
- Voice and video calls.
- DNS queries.
- DHCP.
- Real-time broadcasting.

---

## 5. Difference Between TCP and UDP

TCP and UDP are two major transport layer protocols used for communication over IP networks. Both serve the purpose of transferring data between applications, but they differ in their communication methods, reliability, speed, and applications.

| Basis | TCP | UDP |
|---|---|---|
| Full Form | Transmission Control Protocol | User Datagram Protocol |
| Connection | Connection-oriented | Connectionless |
| Reliability | Reliable | Best-effort delivery |
| Speed | Generally slower | Generally faster |
| Data Transmission | Byte stream | Datagrams |
| Acknowledgement | Supported | Not built-in |
| Error Detection | Checksum | Checksum |
| Retransmission | Supported | Not built-in |
| Data Ordering | Maintains ordered delivery | No ordering guarantee |
| Flow Control | Available | Not built-in |
| Congestion Control | Available | Not built-in |
| Header Size | Minimum 20 bytes | 8 bytes |
| Handshake | Three-way handshake | No handshake |
| Communication | Full-duplex | Supports bidirectional datagram exchange |
| Broadcasting | Not supported directly | Supported |
| Applications | Web, email, file transfer | Gaming, streaming, DNS |

### Which One Should We Use?

**Use TCP when:**

- Data must reach the destination reliably.
- Data must arrive in the correct order.
- Accuracy is more important than low latency.
- File transfer or web communication is required.
- Continuous messaging is needed.

**Use UDP when:**

- Low latency is important.
- Occasional packet loss can be tolerated.
- Real-time communication is required.
- Fast transmission is preferred over built-in delivery guarantees.

**Note:** UDP applications can implement their own reliability mechanisms when required. TCP's reliability features also introduce additional communication overhead.

---

## 6. TCP vs UDP – Communication Flow

### TCP Communication

```text
       CLIENT                     SERVER
          |                          |
          | -------- SYN ----------> |
          | <------ SYN-ACK -------- |
          | -------- ACK ----------> |
          |                          |
          | ------ DATA -----------> |
          | <----- ACK ------------- |
          | <----- RESPONSE -------- |
          |                          |
          | ------ FIN ------------> |
          | <----- ACK ------------- |
          |                          |
          |     CONNECTION CLOSED   |
```

### UDP Communication

```text
       CLIENT                     SERVER
          |                          |
          |                          |
          | ------ DATA -----------> |
          |                          |
          | <----- RESPONSE -------- |
          |                          |
          |                          |
          |     COMMUNICATION ENDS   |
```

*These diagrams illustrate simplified communication flows. TCP connection termination generally uses a four-step FIN/ACK exchange.*

---

## 7. Python Socket Programming

Python provides a built-in `socket` module that allows applications to communicate over a network.

A socket acts as an endpoint for sending and receiving data.

### TCP Socket Creation

```python
socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

- `AF_INET`: Specifies IPv4 addressing.
- `SOCK_STREAM`: Specifies TCP communication.

### UDP Socket Creation

```python
socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
```

- `AF_INET`: Specifies IPv4 addressing.
- `SOCK_DGRAM`: Specifies UDP communication.

### Important Socket Functions

| Function | Protocol | Purpose |
|---|---|---|
| `socket()` | Both | Creates a socket |
| `bind()` | Both | Assigns IP and port |
| `listen()` | TCP | Waits for connections |
| `accept()` | TCP | Accepts a client connection |
| `connect()` | TCP | Establishes a connection |
| `send()` | TCP | Sends data |
| `sendall()` | TCP | Sends all supplied data |
| `recv()` | TCP | Receives data |
| `sendto()` | UDP | Sends a datagram |
| `recvfrom()` | UDP | Receives a datagram and sender address |
| `close()` | Both | Closes a socket |

### Additional Python Concept: Multithreading

The TCP Chat Application uses Python's built-in `threading` module.

Multithreading allows multiple tasks to execute concurrently within a program.

In the chat application:

- One thread handles incoming messages.
- The main thread handles outgoing messages.
- Both operations work independently, allowing continuous two-way communication.

Example:

```python
import threading

thread = threading.Thread(target=receive_messages)
thread.start()
```

---

## 8. Project Structure

```text
Python-Network-Programming/
│
├── TCP-Client-Server/
│   ├── client.py
│   ├── server.py
│   ├── chat_client.py
│   └── chat_server.py
│
├── UDP-Client-Server/
│   ├── client.py
│   └── server.py
│
└── README.md
```

### Directory Description

| File / Folder | Description |
|---|---|
| `TCP/` | Contains TCP communication programs |
| `TCP/client.py` | Basic TCP client |
| `TCP/server.py` | Basic TCP server |
| `TCP/chat_client.py` | TCP chat client using multithreading |
| `TCP/chat_server.py` | TCP chat server using multithreading |
| `UDP/` | Contains UDP communication programs |
| `UDP/client.py` | Basic UDP client |
| `UDP/server.py` | Basic UDP server |
| `README.md` | Main project documentation |

---

## 9. Requirements

- Python 3.x.
- Basic knowledge of Python programming.
- Basic understanding of computer networks.
- Code editor or terminal.

**Dependencies:** No external Python packages are required. The project uses Python's built-in `socket` and `threading` modules.

---

## 10. How to Run the Project

### Step 1: Clone the Repository

```bash
git clone <repository-url>
```

### Step 2: Navigate to the Repository

```bash
cd Python-Network-Programming
```

### A. Running TCP Client-Server

**Terminal 1 – Start TCP Server**

```bash
python TCP/server.py
```

**Terminal 2 – Start TCP Client**

```bash
python TCP/client.py
```

### B. Running TCP Chat Application

**Terminal 1 – Start TCP Chat Server**

```bash
python TCP/chat_server.py
```

**Terminal 2 – Start TCP Chat Client**

```bash
python TCP/chat_client.py
```

Once connected, both sides can send and receive messages continuously.

Type `exit` to end the chat. For a clean shutdown of this basic implementation, type `exit` on both sides.

### C. Running UDP Client-Server

**Terminal 1 – Start UDP Server**

```bash
python UDP/server.py
```

**Terminal 2 – Start UDP Client**

```bash
python UDP/client.py
```

**Important:** Always start the server before executing the client. Open two separate terminals for each communication experiment.

---

## 11. Expected Output

### A. TCP Communication

**Server Output**

```text
Server is waiting for connection...
Connected to: ('127.0.0.1', 54321)
Client: Hello Server!
```

**Client Output**

```text
Server: Hello Client! Message received.
```

### B. TCP Chat Application

**Server Output**

```text
Chat Server is waiting for connection...
Client connected: ('127.0.0.1', 54321)

Client: Hello Server!
You: Hello Client!
Client: How are you?
You: I am fine!
Client ended the chat.
```

**Client Output**

```text
Connected to Chat Server!
Type 'exit' to end the chat.

You: Hello Server!
Server: Hello Client!
You: How are you?
Server: I am fine!
You: exit
Chat Client closed.
```

### C. UDP Communication

**Server Output**

```text
UDP Server is waiting for messages...
Connected to: ('127.0.0.1', 54321)
Client: Hello Server!
```

**Client Output**

```text
Server: Hello Client! Message received.
```

*Note: The temporary client port number may vary between executions.*

---

## 12. Common Concepts Used

### IP Address

An IP address is a logical address used to identify a device on a network.

### Port Number

A port number identifies a particular application or service running on a device.

### Localhost

`127.0.0.1` is the IPv4 loopback address, also known as localhost. It allows communication between applications running on the same computer.

### Client

A client is an application that initiates communication with another application.

### Server

A server is an application that waits for incoming requests and provides responses.

### Socket

A socket is an endpoint used for communication between two applications over a network.

### Threading

Threading allows multiple tasks to execute concurrently within a program. It is used in the TCP Chat Application to handle sending and receiving operations independently.

---

## 13. Advantages and Limitations

### TCP

**Advantages**

- Reliable data transmission.
- Maintains data order.
- Supports retransmission.
- Provides flow and congestion control.
- Suitable for accurate data transfer.

**Limitations**

- Connection establishment overhead.
- More protocol overhead than UDP.
- Retransmissions may increase latency.
- Connection management consumes resources.

### UDP

**Advantages**

- Low communication overhead.
- No connection establishment required.
- Suitable for real-time applications.
- Supports broadcasting and multicasting.
- Preserves individual datagram boundaries.

**Limitations**

- No guaranteed delivery.
- No automatic retransmission.
- No guaranteed packet ordering.
- No built-in flow or congestion control.

---

## 14. Learning Objectives

The primary objectives of this project are:

1. To understand the fundamentals of computer networking.
2. To learn the TCP and UDP transport layer protocols.
3. To understand client-server architecture.
4. To implement socket programming using Python.
5. To understand connection-oriented and connectionless communication.
6. To work with IP addresses and port numbers.
7. To understand the differences between TCP and UDP.
8. To implement continuous two-way communication.
9. To understand multithreading in Python.
10. To gain practical experience in sending and receiving network data.

---

## 15. Conclusion

This project provides practical experience with two fundamental transport layer protocols: TCP and UDP.

By implementing basic client-server communication, continuous TCP chat functionality, and UDP messaging using Python, it demonstrates the differences between connection-oriented and connectionless communication.

TCP provides reliable and ordered data delivery, whereas UDP provides lightweight communication with lower overhead.

The TCP Chat Application further demonstrates how multithreading enables simultaneous sending and receiving of messages.

Understanding these concepts helps build a strong foundation in computer networking, socket programming, and network application development.

---

## 16. Future Improvements

The project can be extended with the following features:

- Multiple-client TCP server implementation.
- Group chat application.
- UDP continuous messaging.
- TCP file transfer.
- DNS lookup program.
- HTTP client-server communication.
- Network port scanning.
- Client-server communication between different computers.
- Error handling and connection timeout mechanisms.

---

## 17. References

- [Python Socket Programming Documentation](https://docs.python.org/3/library/socket.html)
- [Python Threading Documentation](https://docs.python.org/3/library/threading.html)
- [RFC 9293 – Transmission Control Protocol (TCP)](https://www.rfc-editor.org/rfc/rfc9293)
- [RFC 768 – User Datagram Protocol (UDP)](https://www.rfc-editor.org/rfc/rfc768)

---

**Technology:** Python 3 | Socket Programming | TCP | UDP | Multithreading

**Category:** Computer Networks / Network Programming

**Purpose:** Educational project for learning and practicing TCP and UDP client-server communication.

**Author:** Eklavya Chaudhary