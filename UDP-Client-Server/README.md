# UDP Client-Server Communication Using Python

\<p align="center">   \<img src="[https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white](https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white)" alt="Python">   \<img src="[https://img.shields.io/badge/Protocol-UDP-orange](https://img.shields.io/badge/Protocol-UDP-orange)" alt="UDP">   \<img src="[https://img.shields.io/badge/Socket-Programming-purple](https://img.shields.io/badge/Socket-Programming-purple)" alt="Socket Programming"> \</p>

## 1. Introduction

This project demonstrates UDP (User Datagram Protocol) client-server communication using Python socket programming.

UDP is a connectionless transport layer protocol that allows devices to exchange data over a network without establishing a connection before transmission.

Unlike TCP, UDP does not guarantee reliable data delivery, packet ordering, or retransmission of lost packets. However, it provides lower communication overhead, making it suitable for real-time applications.

This project demonstrates how a UDP server receives messages from a client and sends a response using Python's built-in `socket` module.

The project also includes a UDP chat application with separate server and client programs.

## 2. Detailed Overview of UDP

### What is UDP?

**UDP (User Datagram Protocol)** is a connectionless transport layer protocol that enables applications to transmit data in the form of independent datagrams over an IP network.

It allows data to be sent without establishing a connection between the sender and receiver.

UDP is commonly used in applications where speed and low latency are important.

UDP operates at the Transport Layer (Layer 4) of the OSI model.

### Key Characteristics of UDP

1. **Connectionless:** UDP does not establish a connection before transmitting data.
2. **Best-Effort Delivery:** UDP does not guarantee that transmitted datagrams will reach their destination.
3. **No Built-in Acknowledgement:** UDP does not provide built-in acknowledgements for received datagrams.
4. **No Automatic Retransmission:** Lost datagrams are not automatically retransmitted by UDP.
5. **No Ordering Guarantee:** Datagrams may arrive in a different order than they were sent.
6. **Low Overhead:** UDP has a fixed header size of only 8 bytes.
7. **Low Latency:** It avoids connection establishment and built-in retransmission overhead.
8. **Checksum:** UDP uses checksums for error detection. IPv4 UDP checksums can be optional, while IPv6 normally requires them.
9. **Datagram-Based Communication:** UDP sends and receives individual data packets rather than a continuous byte stream.
10. **No Built-in Flow Control:** UDP does not automatically control the transmission rate based on receiver capacity.
11. **No Built-in Congestion Control:** UDP itself does not provide congestion control mechanisms.

## 3. How UDP Works

UDP communication generally involves the following steps.

### A. Socket Creation

Both the client and server create UDP sockets using Python's `socket` module.

### B. Server Binding

The server binds its socket to a specific IP address and port number so that it can receive incoming datagrams.

### C. Data Transmission

1. The client prepares a message.
2. The client sends the message to the server's IP address and port.
3. The network delivers the UDP datagram on a best-effort basis.
4. The server receives the datagram using `recvfrom()`.
5. The server processes the received message.
6. The server sends a response using `sendto()`.

### D. Communication Termination

UDP does not require a connection termination handshake. Each application can close its socket when communication is complete.

## 4. UDP Client-Server Architecture

### UDP Server

A UDP server waits for incoming datagrams from clients.

Its responsibilities include:

- Creating a UDP socket.
- Binding the socket to an IP address and port.
- Waiting for incoming messages.
- Receiving datagrams from clients.
- Processing received messages.
- Sending responses to clients.
- Closing the socket.

### UDP Client

A UDP client sends datagrams to a UDP server.

Its responsibilities include:

- Creating a UDP socket.
- Specifying the server IP address and port.
- Sending messages using `sendto()`.
- Receiving responses using `recvfrom()`.
- Closing the socket.

Unlike TCP, UDP does not require the client to establish a connection before sending data.

## 5. Python Socket Programming

Python provides a built-in `socket` module for implementing network communication.

### UDP Socket Creation

```python
import socket

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)
```

- `AF_INET`: Specifies IPv4 addressing.
- `SOCK_DGRAM`: Specifies a UDP datagram socket.

### Important UDP Socket Functions

| Function     | Description                                   |
| ------------ | --------------------------------------------- |
| `socket()`   | Creates a UDP socket                          |
| `bind()`     | Assigns an IP address and port to the server  |
| `sendto()`   | Sends data to a specified IP address and port |
| `recvfrom()` | Receives data and the sender's address        |
| `close()`    | Closes the socket                             |

### Socket Parameters

- **IP Address:** Identifies a device on a network.
- **Port Number:** Identifies a specific application or service.
- **127.0.0.1:** The IPv4 loopback address, also known as localhost.

## 6. UDP Header Format

UDP uses a fixed-size header of 8 bytes.

It consists of four fields:

| Field            |    Size | Description                                |
| ---------------- | ------: | ------------------------------------------ |
| Source Port      | 16 bits | Identifies the sender's application port   |
| Destination Port | 16 bits | Identifies the receiver's application port |
| Length           | 16 bits | Specifies the UDP header and data length   |
| Checksum         | 16 bits | Used for error detection                   |

**Total UDP Header Size: 64 bits (8 bytes).**

## 7. Project Structure

```text
UDP-Client-Server/
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

| File                      | Description                                                         |
| ------------------------- | ------------------------------------------------------------------- |
| `server.py`               | Creates a UDP server, receives client messages, and sends responses |
| `client.py`               | Sends messages to the UDP server and receives responses             |
| `Examples/chat_server.py` | Server-side program for the UDP chat application                    |
| `Examples/chat_client.py` | Client-side program for the UDP chat application                    |
| `README.md`               | Documentation and execution instructions                            |

## 8. Requirements

- Python 3.x installed.
- Basic knowledge of Python.
- A code editor or terminal.
- Two terminal windows for client-server communication.

No external Python libraries are required for the described implementation.

## 9. Installation and Execution

### Step 1: Clone the Repository

```bash
git clone https://github.com/Eklavya0102/Python-communication-Practise.git
```

### Step 2: Navigate to the Repository

```bash
cd Python-communication-Practise
```

### Step 3: Start the UDP Server

Open the first terminal:

```bash
python UDP-Client-Server/server.py
```

The server will start waiting for incoming UDP messages.

### Step 4: Start the UDP Client

Open a second terminal:

```bash
python UDP-Client-Server/client.py
```

The client will send a message to the server and receive its response.

## 10. UDP Chat Application

The `Examples` folder contains a UDP chat application with two separate programs:

- `chat_server.py` – Handles the server side of the chat.
- `chat_client.py` – Handles the client side of the chat.

The application demonstrates message exchange using UDP datagrams.

### How to Run the UDP Chat Application

**Terminal 1 – Start the Chat Server**

```bash
python UDP-Client-Server/Examples/chat_server.py
```

**Terminal 2 – Start the Chat Client**

```bash
python UDP-Client-Server/Examples/chat_client.py
```

Start the server before running the client.

*The exact chat interaction and termination command depend on the implementation in the example files.*

## 11. Expected Output

The following is an illustrative example of basic UDP client-server communication. Actual messages depend on the code.

**Server Terminal**

```text
UDP Server is waiting for messages...
Message received from: ('127.0.0.1', 54321)
Client: Hello Server!
```

**Client Terminal**

```text
Server: Hello Client! Message received.
```

*Note: The client's temporary port number may differ between executions. UDP does not establish a connection; the sender's address is returned with the received datagram.*

## 12. Applications of UDP

UDP is widely used in applications that require fast communication and low latency.

- **Online Gaming:** Enables fast exchange of game-state updates.
- **Video Streaming:** Supports real-time media delivery.
- **Voice and Video Calls:** Used in real-time communication systems.
- **DNS:** Uses UDP for many domain name lookup queries.
- **DHCP:** Uses UDP for automatic IP address configuration.
- **Live Broadcasting:** Supports real-time audio and video transmission.

## 13. Advantages of UDP

- Low communication overhead.
- No connection establishment required.
- Smaller header size compared to TCP.
- Suitable for real-time applications.
- Supports broadcast and multicast communication.
- Preserves individual datagram boundaries.

## 14. Limitations of UDP

- Does not guarantee data delivery.
- No automatic retransmission of lost packets.
- Does not guarantee packet ordering.
- No built-in flow control.
- No built-in congestion control.
- Applications may need to implement their own reliability mechanisms.

## 15. Learning Objectives

Through this project, the following concepts are explored:

- Understanding UDP and its characteristics.
- Learning connectionless communication.
- Understanding client-server architecture.
- Implementing UDP socket programming in Python.
- Working with IP addresses and port numbers.
- Sending and receiving datagrams.
- Understanding the difference between TCP and UDP.
- Exploring UDP-based chat communication.

## 16. Conclusion

This project provides a practical understanding of UDP-based communication using Python.

By implementing a UDP client, server, and chat application, it demonstrates how two applications exchange data without establishing a connection beforehand.

It serves as a foundation for understanding connectionless communication and developing network-based applications that require low latency and minimal communication overhead.

## 17. References

- [Python Socket Programming Documentation](https://docs.python.org/3/library/socket.html)
- [RFC 768 – User Datagram Protocol](https://www.rfc-editor.org/rfc/rfc768)

---

**Technology:** Python | Socket Programming | UDP/IP

**Category:** Computer Networks Practical / Networking Fundamentals

**Purpose:** Educational implementation of UDP client-server communication.

[Back to Main Repository](../README.md) | [TCP Implementation](../TCP-Client-Server/README.md)
