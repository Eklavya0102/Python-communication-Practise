# Python Network Programming – TCP & UDP Client-Server Communication


<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Protocol-TCP-green" alt="TCP">
  <img src="https://img.shields.io/badge/Protocol-UDP-orange" alt="UDP">
  <img src="https://img.shields.io/badge/Domain-Computer%20Networks-purple" alt="Computer Networks">
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="MIT License">
</p>


## 1. Introduction

**Python Communication Practise** is an educational repository containing practical implementations of TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) client-server communication using Python socket programming.

This project helps students and beginners understand computer networking, transport layer protocols, socket programming, and client-server architecture through practical implementation.

It demonstrates how two applications communicate over a network, exchange messages, and use different transport protocols.

The repository includes:

- Basic TCP client-server communication.
- TCP chat application using separate server and client programs.
- Basic UDP client-server communication.
- UDP chat application using separate server and client programs.
- TCP vs UDP comparison.
- Python socket programming documentation.

## 2. Project Objectives

- Understand the fundamentals of computer networking.
- Learn TCP and UDP transport layer protocols.
- Understand client-server architecture.
- Implement socket programming using Python.
- Understand connection-oriented and connectionless communication.
- Work with IP addresses and port numbers.
- Exchange messages between client and server applications.
- Explore interactive chat communication.

## 3. Project Overview

### A. TCP Client-Server Communication

TCP is a connection-oriented transport layer protocol that provides reliable and ordered data transmission.

The TCP implementation demonstrates:

- Creating TCP client and server sockets.
- Binding the server to an IP address and port.
- Listening for incoming connections.
- Accepting client connections.
- Sending and receiving messages.
- Closing the connection.

**TCP Chat Application**

The TCP chat example contains separate server and client programs. It demonstrates interactive message exchange between the two applications.

### B. UDP Client-Server Communication

UDP is a connectionless transport layer protocol that allows applications to exchange data without establishing a connection beforehand.

The UDP implementation demonstrates:

- Creating UDP client and server sockets.
- Binding the server to an IP address and port.
- Sending datagrams using `sendto()`.
- Receiving datagrams using `recvfrom()`.
- Identifying the sender's address.
- Sending responses to clients.

**UDP Chat Application**

The UDP chat example also contains separate server and client programs. It demonstrates message exchange using UDP datagrams.

## 4. Understanding TCP and UDP

| Basis               | TCP                           | UDP                    |
| ------------------- | ----------------------------- | ---------------------- |
| Full Form           | Transmission Control Protocol | User Datagram Protocol |
| Connection          | Connection-oriented           | Connectionless         |
| Reliability         | Reliable delivery             | Best-effort delivery   |
| Data Transmission   | Byte stream                   | Datagrams              |
| Acknowledgement     | Built-in                      | Not built-in           |
| Retransmission      | Supported                     | Not built-in           |
| Data Ordering       | Maintained                    | Not guaranteed         |
| Header Size         | 20–60 bytes                   | 8 bytes                |
| Handshake           | Three-way handshake           | No handshake           |
| Common Applications | Web, email, file transfer     | Gaming, streaming, DNS |

### When to Use TCP?

TCP is suitable when reliable and ordered data delivery is important, such as file transfers, web communication, and email.

### When to Use UDP?

UDP is suitable when low latency and low communication overhead are important, such as online gaming, voice calls, and real-time streaming.

For a detailed explanation, refer to [TCP vs UDP](docs/TCP_vs_UDP.md).

## 5. TCP and UDP Communication Flow

### TCP Communication

```text
       CLIENT                         SERVER
          |                              |
          | -------- SYN --------------> |
          | <------ SYN-ACK ------------ |
          | -------- ACK --------------> |
          |                              |
          | -------- DATA -------------> |
          | <------ RESPONSE ----------- |
          |                              |
          |       CONNECTION CLOSED     |
```

TCP establishes a connection using a three-way handshake before data transmission.

### UDP Communication

```text
       CLIENT                         SERVER
          |                              |
          | -------- DATA -------------> |
          |                              |
          | <------ RESPONSE ----------- |
          |                              |
          |       COMMUNICATION ENDS    |
```

UDP sends datagrams without requiring a connection handshake.

*These diagrams illustrate simplified communication flows.*

## 6. Python Socket Programming

Python provides the built-in `socket` module for network communication.

### TCP Socket

```python
import socket

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
```

- `AF_INET` specifies IPv4 addressing.
- `SOCK_STREAM` specifies TCP communication.

### UDP Socket

```python
import socket

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)
```

- `AF_INET` specifies IPv4 addressing.
- `SOCK_DGRAM` specifies UDP communication.

### Important Socket Functions

| Function               | Protocol | Purpose                                |
| ---------------------- | -------- | -------------------------------------- |
| `socket()`             | Both     | Creates a socket                       |
| `bind()`               | Both     | Assigns an IP address and port         |
| `listen()`             | TCP      | Waits for incoming connections         |
| `accept()`             | TCP      | Accepts a client connection            |
| `connect()`            | TCP      | Establishes a connection               |
| `send()` / `sendall()` | TCP      | Sends data                             |
| `recv()`               | TCP      | Receives data                          |
| `sendto()`             | UDP      | Sends a datagram                       |
| `recvfrom()`           | UDP      | Receives a datagram and sender address |
| `close()`              | Both     | Closes a socket                        |

For more details, refer to [Python Socket Programming](docs/socket_programming.md).

## 7. Repository Structure

```text
Python-communication-Practise/
│
├── TCP-Client-Server/
│   ├── server.py
│   ├── client.py
│   ├── README.md
│   │
│   └── Examples/
│       ├── chat_server.py
│       └── chat_client.py
│
├── UDP-Client-Server/
│   ├── server.py
│   ├── client.py
│   ├── README.md
│   │
│   └── Examples/
│       ├── chat_server.py
│       └── chat_client.py
│
├── docs/
│   ├── TCP_vs_UDP.md
│   └── socket_programming.md
│
├── requirements.txt
├── LICENSE
└── README.md
```

### Directory Description

| File / Folder                 | Description                      |
| ----------------------------- | -------------------------------- |
| `TCP-Client-Server/`          | TCP client-server implementation |
| `TCP-Client-Server/server.py` | TCP server program               |
| `TCP-Client-Server/client.py` | TCP client program               |
| `TCP-Client-Server/Examples/` | TCP chat application             |
| `chat_server.py`              | TCP chat server                  |
| `chat_client.py`              | TCP chat client                  |
| `UDP-Client-Server/`          | UDP client-server implementation |
| `UDP-Client-Server/server.py` | UDP server program               |
| `UDP-Client-Server/client.py` | UDP client program               |
| `UDP-Client-Server/Examples/` | UDP chat application             |
| `chat_server.py`              | UDP chat server                  |
| `chat_client.py`              | UDP chat client                  |
| `docs/`                       | Networking documentation         |
| `requirements.txt`            | Project dependencies             |
| `LICENSE`                     | MIT License                      |

## 8. Requirements

- Python 3.x.
- A code editor or terminal.
- Basic knowledge of Python and computer networks.
- Two terminal windows for client-server communication.

**Dependencies:** The implementations use Python's built-in `socket` module. No external networking packages are required for the described programs.

## 9. Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/Eklavya0102/Python-communication-Practise.git
```

### Step 2: Navigate to the Repository

```bash
cd Python-communication-Practise
```

### Step 3: Check Python Installation

```bash
python --version
```

## 10. How to Run the Project

For each implementation, open two terminal windows. Start the server first, then run the client.

### A. TCP Client-Server Communication

**Terminal 1 – TCP Server**

```bash
python TCP-Client-Server/server.py
```

**Terminal 2 – TCP Client**

```bash
python TCP-Client-Server/client.py
```

### B. TCP Chat Application

**Terminal 1 – TCP Chat Server**

```bash
python TCP-Client-Server/Examples/chat_server.py
```

**Terminal 2 – TCP Chat Client**

```bash
python TCP-Client-Server/Examples/chat_client.py
```

### C. UDP Client-Server Communication

**Terminal 1 – UDP Server**

```bash
python UDP-Client-Server/server.py
```

**Terminal 2 – UDP Client**

```bash
python UDP-Client-Server/client.py
```

### D. UDP Chat Application

**Terminal 1 – UDP Chat Server**

```bash
python UDP-Client-Server/Examples/chat_server.py
```

**Terminal 2 – UDP Chat Client**

```bash
python UDP-Client-Server/Examples/chat_client.py
```

**Important:** Start the server before the client. For local testing, use `127.0.0.1` as the server IP address if that matches the address configured in your programs.

## 11. Common Networking Concepts

| Concept     | Description                                    |
| ----------- | ---------------------------------------------- |
| IP Address  | Identifies a device on a network               |
| Port Number | Identifies an application or service           |
| Localhost   | `127.0.0.1`, the IPv4 loopback address         |
| Client      | Application that initiates communication       |
| Server      | Application that waits for incoming requests   |
| Socket      | Endpoint for network communication             |
| Datagram    | Independent unit of data transmitted using UDP |

## 12. Learning Outcomes

After completing this project, learners should be able to:

1. Understand the fundamentals of computer networking.
2. Explain TCP and UDP transport layer protocols.
3. Understand client-server architecture.
4. Implement socket programming using Python.
5. Differentiate connection-oriented and connectionless communication.
6. Work with IP addresses and port numbers.
7. Send and receive data over a network.
8. Understand basic chat application communication.

## 13. Future Improvements

Potential extensions include:

- Multiple-client TCP server.
- Group chat application.
- TCP file transfer.
- UDP-based real-time applications.
- DNS lookup program.
- HTTP client-server communication.
- Improved error handling and connection timeout mechanisms.

## 14. Documentation and Learning Resources

| Documentation                                    | Description                            |
| ------------------------------------------------ | -------------------------------------- |
| [TCP vs UDP](docs/TCP_vs_UDP.md)                 | Detailed comparison of TCP and UDP     |
| [Socket Programming](docs/socket_programming.md) | Python socket programming fundamentals |
| [TCP Client-Server](TCP-Client-Server/README.md) | TCP implementation and instructions    |
| [UDP Client-Server](UDP-Client-Server/README.md) | UDP implementation and instructions    |

## 15. References

- [Python Socket Programming Documentation](https://docs.python.org/3/library/socket.html)
- [Python Threading Documentation](https://docs.python.org/3/library/threading.html)
- [RFC 9293 – Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293)
- [RFC 768 – User Datagram Protocol](https://www.rfc-editor.org/rfc/rfc768)

## 16. Conclusion

This project provides practical experience with two fundamental transport layer protocols: TCP and UDP.

Through basic client-server programs and chat applications, it demonstrates how applications exchange information using connection-oriented and connectionless communication.

TCP focuses on reliable and ordered data delivery, whereas UDP provides lightweight communication with lower overhead.

The repository serves as a practical learning resource for students and beginners who want to develop a foundation in computer networking and Python network programming.

---

## Author

**Eklavya Chaudhary**

**Technology:** Python 3 | Socket Programming | TCP | UDP

**Category:** Computer Networks / Network Programming

**Purpose:** Educational project for learning and practising TCP and UDP client-server communication.

**Repository:** [Python Communication Practise](https://github.com/Eklavya0102/Python-communication-Practise)

**License:** MIT License

---

\<p align="center">   \<b>Learn. Code. Understand. Connect.\</b>   \<br>   If you find this repository helpful, consider giving it a ⭐ on GitHub! \</p>
