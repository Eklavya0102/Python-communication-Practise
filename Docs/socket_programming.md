# Socket Programming in Python

## 1. Introduction

Socket programming is a method of enabling communication between two or more devices over a computer network.

It allows applications running on different computers, or on the same computer, to exchange data using network protocols such as TCP and UDP.

Python provides a built-in `socket` module that makes network communication simple and easy to implement.

Socket programming is commonly used in:
- Client-server applications.
- Chat applications.
- File transfer systems.
- Online multiplayer games.
- Web servers.
- Network monitoring tools.

## 2. What is a Socket?

A socket is an endpoint of communication between two devices or applications over a network.

It acts as an interface between an application and the network communication system.

A socket is generally identified using:

- **IP Address:** Identifies a device on a network.
- **Port Number:** Identifies a specific application or service.
- **Protocol:** Defines how communication takes place, such as TCP or UDP.

### Example

Consider a client communicating with a server:

```text
Client                          Server
IP: 192.168.1.10                IP: 192.168.1.20
Port: 50000                     Port: 12345
       |                            |
       | ------ Message ----------> |
       | <----- Response ---------- |
```

The client and server use their IP addresses and port numbers to communicate.

## 3. What is an IP Address?

An IP (Internet Protocol) address is a unique logical address used to identify a device on an IP network.

There are two main versions:

### IPv4

IPv4 uses a 32-bit address represented in four decimal numbers separated by dots.

Example:

```text
192.168.1.10
127.0.0.1
8.8.8.8
```

### IPv6

IPv6 uses a 128-bit address represented in hexadecimal notation.

Example:

```text
2001:db8::1
```

### Localhost

`127.0.0.1` is the IPv4 loopback address, commonly known as localhost.

It allows a computer to communicate with applications running on itself.

For local client-server practice, both programs can use:

```python
HOST = "127.0.0.1"
```

## 4. What is a Port Number?

A port number is a numerical identifier used to distinguish different applications or services running on the same device.

Port numbers range from 0 to 65535.

### Port Number Categories

| Range | Category | Description |
|---|---|---|
| 0–1023 | Well-known ports | Common standard services |
| 1024–49151 | Registered ports | Registered application services |
| 49152–65535 | Dynamic/private ports | Commonly used for temporary connections |

### Examples of Common Ports

| Port | Service |
|---|---|
| 20/21 | FTP |
| 22 | SSH |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 443 | HTTPS |
| 3306 | MySQL |
| 5432 | PostgreSQL |

For learning socket programming, we can use a custom port such as `12345`.

## 5. What is Client-Server Architecture?

Client-server architecture is a communication model in which one application requests services or information from another application.

It consists of two main components:

### Client

The client is an application that initiates communication by sending requests to a server.

Examples:
- Web browsers.
- Mobile applications.
- Desktop applications.

### Server

The server is an application that waits for incoming requests and provides responses to connected clients.

Examples:
- Web servers.
- Database servers.
- File servers.

### Client-Server Communication Flow

```text
       CLIENT                         SERVER
          |                              |
          | ------ Connection Request ->|
          |                              |
          | <----- Connection Response -|
          |                              |
          | -------- Send Data -------->|
          |                              |
          | <------- Receive Data ------|
          |                              |
          | -------- Disconnect ------->|
```

The exact communication process depends on whether TCP or UDP is used.

## 6. What is Socket Programming in Python?

Python provides the `socket` module for implementing network communication.

It supports both TCP and UDP communication.

To use it, import the module:

```python
import socket
```

### Creating a Socket

A socket is created using the `socket()` function.

Syntax:

```python
socket.socket(address_family, socket_type)
```

There are two important parameters:

**1. Address Family**

- `socket.AF_INET` – IPv4 addressing.
- `socket.AF_INET6` – IPv6 addressing.

**2. Socket Type**

- `socket.SOCK_STREAM` – TCP communication.
- `socket.SOCK_DGRAM` – UDP communication.

### TCP Socket Creation

```python
import socket

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
```

### UDP Socket Creation

```python
import socket

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)
```

## 7. Important Socket Methods

Python provides several methods to establish and manage network communication.

### Common Methods

| Method | Description |
|---|---|
| `socket()` | Creates a socket. |
| `bind()` | Assigns an IP address and port number. |
| `close()` | Closes the socket. |
| `getsockname()` | Returns the socket's own address. |
| `setsockopt()` | Sets socket options. |

### TCP-Specific Methods

| Method | Description |
|---|---|
| `listen()` | Makes a TCP server wait for connections. |
| `accept()` | Accepts an incoming client connection. |
| `connect()` | Establishes a connection with a server. |
| `send()` | Sends data through a connected socket. |
| `recv()` | Receives data through a connected socket. |
| `sendall()` | Sends all supplied data or raises an error. |

### UDP-Specific Methods

| Method | Description |
|---|---|
| `sendto()` | Sends data to a specified address. |
| `recvfrom()` | Receives data and returns the sender's address. |

## 8. Understanding Data Transmission

Computers transmit data in bytes, so Python strings must be converted before sending them through sockets.

### Encoding

The `encode()` method converts a string into bytes.

```python
message = "Hello Server"
data = message.encode()
```

### Decoding

The `decode()` method converts received bytes back into a string.

```python
received_data = data.decode()
```

### Example

```python
message = "Hello World"

# Convert string into bytes
encoded_message = message.encode()

# Convert bytes into string
decoded_message = encoded_message.decode()

print(decoded_message)
```

Output:

```text
Hello World
```

## 9. TCP Client-Server Communication

TCP is a connection-oriented protocol that provides reliable and ordered data transmission.

### TCP Server Workflow

1. Create a TCP socket.
2. Bind the socket to an IP address and port.
3. Listen for incoming connections.
4. Accept a client connection.
5. Receive data from the client.
6. Send a response.
7. Close the connection.

### TCP Client Workflow

1. Create a TCP socket.
2. Connect to the server.
3. Send a message.
4. Receive the server's response.
5. Close the connection.

Refer to the [TCP Client-Server implementation](../TCP-Client-server/README.md).

## 10. UDP Client-Server Communication

UDP is a connectionless protocol that sends data without establishing a connection.

### UDP Server Workflow

1. Create a UDP socket.
2. Bind the socket to an IP address and port.
3. Wait for incoming datagrams.
4. Receive data using `recvfrom()`.
5. Send a response using `sendto()`.

### UDP Client Workflow

1. Create a UDP socket.
2. Prepare a message.
3. Send data using `sendto()`.
4. Receive a response using `recvfrom()`.

Refer to the [UDP Client-Server implementation](../UDP-Client-Server/README.md).

## 11. TCP vs UDP Socket Methods

| TCP | UDP |
|---|---|
| `SOCK_STREAM` | `SOCK_DGRAM` |
| `listen()` | Not required |
| `accept()` | Not required |
| `connect()` | Optional for UDP |
| `send()` / `sendall()` | `sendto()` |
| `recv()` | `recvfrom()` |
| `bind()` | `bind()` |

## 12. Common Socket Programming Errors

Understanding common errors helps in debugging network applications.

| Error | Possible Cause |
|---|---|
| `ConnectionRefusedError` | Server is not running or is not accepting connections. |
| `Address already in use` | The selected port is already occupied. |
| `TimeoutError` | Communication did not complete within the timeout. |
| `ConnectionResetError` | The remote connection was unexpectedly closed. |
| `OSError` | General operating system or network-related error. |

### Basic Error Handling

```python
import socket

try:
    client = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    client.connect(("127.0.0.1", 12345))

except ConnectionRefusedError:
    print("Unable to connect to the server.")

except OSError as error:
    print("Socket error:", error)

finally:
    if "client" in locals():
        client.close()
```

## 13. How to Run Socket Programs

### Requirements

- Python 3.x
- Code editor such as VS Code.
- Two terminal windows.

### Running TCP

**Terminal 1 – Start the server**

```bash
python server.py
```

**Terminal 2 – Start the client**

```bash
python client.py
```

### Running UDP

**Terminal 1 – Start the server**

```bash
python server.py
```

**Terminal 2 – Start the client**

```bash
python client.py
```

Make sure the server is running before starting the client.

For local practice, use `127.0.0.1` as the server address in both programs.

## 14. Learning Outcomes

After completing this documentation and the practical implementations, learners should be able to:

- Understand socket programming fundamentals.
- Identify IP addresses and port numbers.
- Explain client-server architecture.
- Create TCP and UDP sockets in Python.
- Understand important socket methods.
- Encode and decode network messages.
- Build basic client-server applications.
- Identify and handle common socket errors.

## 15. References

- [Python Socket Programming Documentation](https://docs.python.org/3/library/socket.html)
- [Python Socket HOWTO](https://docs.python.org/3/howto/sockets.html)
- [RFC 9293 – Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293)
- [RFC 768 – User Datagram Protocol](https://www.rfc-editor.org/rfc/rfc768)

---

**Part of Python Communication Practise**

Learn. Code. Understand. Connect.