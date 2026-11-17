# TCP vs UDP – Understanding Transport Layer Protocols

## 1. Introduction

TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) are two major transport layer protocols used in computer networking.

Both protocols enable communication between devices over a network. However, they differ in how they transmit data, handle errors, and maintain communication.

- **TCP:** A connection-oriented protocol that provides reliable and ordered data delivery.
- **UDP:** A connectionless protocol that provides faster communication without guaranteeing delivery or order.

## 2. What is TCP?

TCP stands for **Transmission Control Protocol**.

It is a connection-oriented communication protocol that establishes a connection between a client and a server before exchanging data.

TCP ensures that:
- Data reaches the destination reliably.
- Data packets are delivered in the correct order.
- Lost packets are retransmitted.
- Duplicate data is detected.
- Errors are detected using checksums.

### How TCP Works

1. The client sends a connection request to the server.
2. The server responds to the request.
3. The client acknowledges the response.
4. A connection is established.
5. Data is exchanged reliably.
6. The connection is closed after communication.

### TCP Three-Way Handshake

TCP establishes a connection using a three-way handshake:

| Step | Process | Description |
|---|---|---|
| 1 | SYN | Client requests a connection. |
| 2 | SYN-ACK | Server acknowledges the request. |
| 3 | ACK | Client confirms the connection. |

After these three steps, communication can begin.

### Advantages of TCP

- Reliable data transmission.
- Guaranteed in-order delivery.
- Error detection and recovery.
- Flow control and congestion control.
- Suitable for transferring important data.

### Disadvantages of TCP

- More overhead than UDP.
- Connection establishment takes time.
- Generally higher latency.
- Requires more protocol state and resources.

### Applications of TCP

- Web browsing (HTTP/HTTPS).
- Email communication.
- File transfer.
- Remote access (SSH).
- Database communication.

## 3. What is UDP?

UDP stands for **User Datagram Protocol**.

It is a connectionless communication protocol that sends data without establishing a connection between the client and server.

UDP does not guarantee that packets will reach their destination or arrive in the correct order.

### How UDP Works

1. The client prepares a data packet.
2. The client sends the packet to the server.
3. The server receives the packet if it reaches the destination.
4. The server can respond without establishing a connection.

Unlike TCP, UDP does not perform a connection handshake or automatically retransmit lost packets.

### Advantages of UDP

- Faster communication with low overhead.
- No connection establishment required.
- Suitable for real-time applications.
- Supports broadcast and multicast.

### Disadvantages of UDP

- No guaranteed packet delivery.
- No guaranteed packet ordering.
- No built-in retransmission.
- Applications must implement reliability if required.

### Applications of UDP

- Online gaming.
- Live video streaming.
- Voice and video calls.
- DNS queries.
- Real-time communication.

## 4. TCP vs UDP – Comparison

| Feature | TCP | UDP |
|---|---|---|
| Full Form | Transmission Control Protocol | User Datagram Protocol |
| Connection | Connection-oriented | Connectionless |
| Reliability | Reliable | Best-effort |
| Data Delivery | Ordered | No ordering guarantee |
| Speed | Generally higher overhead | Generally lower overhead |
| Error Detection | Yes | Yes, using checksum |
| Retransmission | Supported | Not built-in |
| Handshake | Three-way handshake | No handshake |
| Flow Control | Yes | No |
| Congestion Control | Yes | No built-in mechanism |
| Header Size | 20–60 bytes | 8 bytes |
| Data Format | Byte stream | Datagrams |
| Broadcasting | Not supported | Supported |
| Typical Usage | File transfer, web, email | Gaming, streaming, DNS |

## 5. Visual Representation

### TCP Communication

TCP provides reliable communication through acknowledgements and retransmission.

```text
CLIENT                         SERVER
  |                               |
  | -------- SYN ---------------> |
  | <------ SYN-ACK ------------- |
  | -------- ACK ---------------> |
  |                               |
  | -------- DATA --------------> |
  | <-------- ACK --------------- |
  |                               |
  | -------- DATA --------------> |
  | <-------- ACK --------------- |
  |                               |
  |          Connection           |
  |             Closed            |
```

### UDP Communication

UDP sends datagrams without establishing a connection or requiring acknowledgements.

```text
CLIENT                         SERVER
  |                               |
  | -------- DATA --------------> |
  | -------- DATA --------------> |
  | -------- DATA --------------> |
  |                               |
  |       No delivery guarantee   |
  |       No automatic retry      |
```

## 6. TCP and UDP in Python

Python provides the built-in `socket` module to implement network communication using TCP and UDP.

### TCP Socket

TCP uses `SOCK_STREAM`.

```python
import socket

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
```

### UDP Socket

UDP uses `SOCK_DGRAM`.

```python
import socket

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)
```

### Difference in Socket Methods

| TCP Method | Purpose |
|---|---|
| `bind()` | Assigns an IP address and port. |
| `listen()` | Waits for incoming connections. |
| `accept()` | Accepts a client connection. |
| `connect()` | Connects the client to the server. |
| `send()` | Sends data. |
| `recv()` | Receives data. |

| UDP Method | Purpose |
|---|---|
| `bind()` | Assigns an IP address and port. |
| `sendto()` | Sends data to a destination address. |
| `recvfrom()` | Receives data and sender address. |

## 7. When Should You Use TCP or UDP?

### Choose TCP when:
- Data accuracy is important.
- Every message must be delivered.
- Data must arrive in order.
- You are transferring files or accessing websites.

### Choose UDP when:
- Low latency is important.
- Occasional packet loss is acceptable.
- Real-time communication is required.
- You are developing online games or live streaming applications.

**Note:** UDP can also be used for reliable communication when an application implements its own reliability mechanisms.

## 8. Conclusion

TCP and UDP are essential transport layer protocols used in computer networking.

TCP focuses on reliable and ordered data delivery, whereas UDP focuses on low-overhead communication without guaranteeing delivery.

The choice between TCP and UDP depends on the application's requirements, especially reliability, latency, and communication overhead.

## 9. References

- [Python Socket Programming Documentation](https://docs.python.org/3/library/socket.html)
- [RFC 9293 – Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293)
- [RFC 768 – User Datagram Protocol](https://www.rfc-editor.org/rfc/rfc768)

---

**Part of Python Communication Practise**

Learn. Code. Understand. Connect.