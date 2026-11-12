# Python Network Programming – TCP & UDP Client-Server Communication

## 1. Introduction

This repository contains practical implementations of **TCP (Transmission Control Protocol)** and **UDP (User Datagram Protocol)** client-server communication using Python socket programming.

The project is developed to understand the fundamentals of computer networking, transport layer protocols, and client-server architecture.

It demonstrates how two applications communicate over a network using different transport protocols, exchange messages, and handle data transmission.

Both TCP and UDP are implemented using Python's built-in `socket` module without requiring any external libraries.

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

---

## 4. Understanding UDP

### What is UDP?

**UDP (User Datagram Protocol)** is a connectionless transport layer protocol that allows applications to transmit data in the form of independent datagrams without establishing a connection beforehand.

It provides low communication overhead and is commonly used in applications where speed and low latency are important.

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
| Communication | Full-duplex | Supports request and response communication |
| Broadcasting | Not supported directly | Supported |
| Applications | Web, email, file transfer | Gaming, streaming, DNS |

### Which One Should We Use?

**Use TCP when:**
- Data must reach the destination reliably.
- Data must arrive in the correct order.
- Accuracy is more important than low latency.
- File transfer or web communication is required.

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
| `recv()` | TCP | Receives data |
| `sendto()` | UDP | Sends a datagram |
| `recvfrom()` | UDP | Receives a datagram and sender address |
| `close()` | Both | Closes a socket |

---

## 8. Project Structure

```text
Python-Network-Programming/
│
├── TCP/
│   ├── client.py
│   └── server.py
│
├── UDP/
│   ├── client.py
│   └── server.py
│
└── README.md
```

### Directory Description

| File / Folder | Description |
|---|---|
| `TCP/` | Contains TCP client-server implementation |
| `TCP/client.py` | Connects to the TCP server and sends a message |
| `TCP/server.py` | Accepts TCP connections and responds to clients |
| `UDP/` | Contains UDP client-server implementation |
| `UDP/client.py` | Sends UDP datagrams and receives responses |
| `UDP/server.py` | Receives UDP datagrams and sends responses |
| `README.md` | Main project documentation |

---

## 9. Requirements

- Python 3.x
- Basic knowledge of Python programming.
- Basic understanding of computer networks.
- Code editor or terminal.

**Dependencies:** No external Python packages are required. The project uses Python's built-in `socket` module.

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

### B. Running UDP Client-Server

**Terminal 1 – Start UDP Server**

```bash
python UDP/server.py
```

**Terminal 2 – Start UDP Client**

```bash
python UDP/client.py
```

**Important:** Always start the server before executing the client.

---

## 11. Expected Output

### TCP Communication

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

### UDP Communication

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

An IP address is a unique logical address used to identify a device on a network.

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
8. To gain practical experience in sending and receiving network data.

---

## 15. Conclusion

This project provides practical experience with two fundamental transport layer protocols: TCP and UDP.

By implementing both client-server models using Python, it demonstrates the differences between connection-oriented and connectionless communication.

TCP provides reliable and ordered data delivery, whereas UDP provides lightweight communication with lower overhead.

Understanding both protocols helps build a strong foundation in computer networking, socket programming, and network application development.

---

## 16. Future Improvements

The project can be extended with the following features:

- Multiple-client TCP server implementation.
- Continuous two-way communication.
- UDP communication with multiple messages.
- File transfer using TCP.
- Simple chat application.
- Client-server communication between different computers.
- Error handling and connection timeout mechanisms.

---

## 17. References

- [Python Socket Programming Documentation](https://docs.python.org/3/library/socket.html)
- [RFC 9293 – Transmission Control Protocol (TCP)](https://www.rfc-editor.org/rfc/rfc9293)
- [RFC 768 – User Datagram Protocol (UDP)](https://www.rfc-editor.org/rfc/rfc768)

---

**Technology:** Python 3 | Socket Programming | TCP | UDP

**Category:** Computer Networks / Network Programming

**Purpose:** Educational project for learning and practicing TCP and UDP client-server communication.

**Author:** Eklavya Chaudhary