# TryHackMe — Pre-Security Path
## Module 4: Networking Concepts, Core Protocols & Secure Communications

> **Platform:** TryHackMe  
> **Path:** Penetration Testing  
> **Status:** ✅ Completed

---

## 📌 Overview

This module covered networking concepts in depth — from the OSI and TCP/IP models to IP addressing, routing, and core protocols. It also covered securing communications with TLS, SSH, SFTP, and VPNs, along with hands-on use of tools like Telnet, ping, and traceroute.

---

## 1. The OSI Model

The **OSI (Open Systems Interconnection)** model is a 7-layer framework developed by the International Organization for Standardization (ISO) that defines how communication should occur in a computer network.

| Layer | Name | Key Function | Examples |
|---|---|---|---|
| 7 | **Application** | Network services directly to user applications | HTTP, FTP, SMTP, IMAP |
| 6 | **Presentation** | Data encoding, compression, and encryption | ASCII, Unicode, MIME, JPEG, PNG |
| 5 | **Session** | Establishes, maintains, and synchronizes sessions between applications | NFS, RPC |
| 4 | **Transport** | End-to-end communication; segmentation, error control, flow control | TCP, UDP |
| 3 | **Network** | Logical addressing and routing between different networks | IP, ICMP, IPSec |
| 2 | **Data Link** | Physical addressing (MAC); data transfer within the same network | Ethernet, Wi-Fi (MAC addresses) |
| 1 | **Physical** | Transmits raw binary data (0s and 1s) over physical media | Cables, fiber optics, radio signals |

### Layer Highlights

- **Physical Layer** — defines the medium (copper cables, optical fiber, wireless) to transmit signals as binary
- **Data Link Layer** — handles communication between devices on the **same** network using MAC addresses; every NIC has a unique MAC address set by the manufacturer
- **Network Layer** — connects **different** networks together; handles routing via routers (like tracing a route across cities/countries)
- **Transport Layer** — enables end-to-end communication between applications on different hosts using TCP or UDP
- **Session Layer** — creates and maintains sessions; handles synchronization to prevent race conditions; ensures data is transmitted in the correct order
- **Presentation Layer** — acts as a translator between different software systems; handles encoding (ASCII/Unicode) and formats like JPEG, GIF, PNG using MIME for email attachments
- **Application Layer** — the layer users interact with most; protocols like HTTP, FTP, SMTP, IMAP operate here

---

## 2. The TCP/IP Model

The **TCP/IP model** is a practical 4-layer model that underpins the modern Internet. Unlike the OSI model's 7 layers, it groups the top three OSI layers into one.

| TCP/IP Layer | Equivalent OSI Layers | Description |
|---|---|---|
| **Application** | Layers 5, 6, 7 (Session + Presentation + Application) | User-facing protocols (HTTP, FTP, SMTP) |
| **Transport** | Layer 4 | TCP/UDP; end-to-end communication |
| **Internet** | Layer 3 | IP addressing and routing |
| **Link** | Layer 2 | Physical MAC addressing; local network |

> **Key difference:** OSI has 7 layers; TCP/IP has 4 layers. The top three OSI layers (Application, Presentation, Session) are combined into a single Application layer in TCP/IP.

---

## 3. IP Addresses & Subnetting

An **IP address** is a unique identifier for a device on a network, made up of **4 octets** (32 bits for IPv4), each ranging from 0–255.

### IPv4 vs IPv6

| Version | Bits | Address Space | Notes |
|---|---|---|---|
| **IPv4** | 32 | ~4.29 billion addresses | Running out due to device explosion |
| **IPv6** | 128 | ~340+ trillion addresses | Solves IPv4 exhaustion |

### Private vs Public IP Addresses

| Type | Purpose |
|---|---|
| **Private** | Used within local networks; not routable on the Internet |
| **Public** | Assigned by ISP; used to communicate on the Internet |

### RFC 1918 — Private IP Ranges (Memorize these!)

| Range | CIDR |
|---|---|
| `10.0.0.0` – `10.255.255.255` | `10/8` |
| `172.16.0.0` – `172.31.255.255` | `172.16/12` |
| `192.168.0.0` – `192.168.255.255` | `192.168/16` |

> By looking at an IP address, you can tell if it's private or public based on these ranges.

### Subnetting

A subnet mask defines how an IP address is split between the **network** portion and the **host** portion.

**Example:** `192.168.66.89/24`
- `/24` means the leftmost **24 bits** are fixed (network)
- The remaining **8 bits** can vary (host addresses)

### Useful Commands

```bash
# Windows
ipconfig

# Linux
ifconfig
ip address show   # or: ip a s
```

---

## 4. Routing & Routing Protocols

**Routing** is the process of finding the best path for data packets to travel from source to destination across networks. Routers operate at **Layer 3** and forward packets based on IP addresses.

### Common Routing Protocols

| Protocol | Full Name | Description |
|---|---|---|
| **OSPF** | Open Shortest Path First | Shares network topology info and calculates the most efficient path |
| **EIGRP** | Enhanced Interior Gateway Routing Protocol | Combines aspects of multiple routing algorithms; shares reachable networks and cost |
| **BGP** | Border Gateway Protocol | Used on the Internet between ISPs; exchanges routing info between large networks |
| **RIP** | Routing Information Protocol | Simple protocol for small networks; uses hop count to determine best route |

---

## 5. UDP & TCP

Both protocols operate at the **Transport Layer (Layer 4)** and allow communication with specific processes on a target host using **port numbers**.

### TCP (Transmission Control Protocol)

- **Connection-oriented** — establishes a connection before sending data
- **Reliable** — ensures packets arrive in the correct order
- Each data segment is automatically numbered; receiver sends acknowledgements
- Lost packets are retransmitted

### UDP (User Datagram Protocol)

- **Connectionless** — sends data without establishing a connection first
- **Unreliable** — does not guarantee packet order or delivery
- Faster than TCP due to no overhead

### Three-Way Handshake (TCP)

| Step | Flag | Description |
|---|---|---|
| 1 | **SYN** | Client sends synchronization request with a random sequence number |
| 2 | **SYN/ACK** | Server responds with its own sequence number and acknowledges client's |
| 3 | **ACK** | Client acknowledges the server's SYN/ACK; connection established |

> Valid port numbers range from **1 to 65535** (uses 2 bytes); port 0 is reserved.

---

## 6. Encapsulation

Encapsulation is the process of each OSI layer adding its own header (and sometimes trailer) to the data as it moves down the stack.

| Layer | Unit | What's Added |
|---|---|---|
| Application | Data | Application data |
| Transport | Segment / Datagram | TCP/UDP header |
| Network | Packet | IP header |
| Data Link | Frame | MAC header + trailer |
| Physical | Bits | Raw binary signal |

> Each layer wraps the data from the layer above — like putting a letter inside an envelope, then a box, then a shipping label.

---

## 7. Telnet

**Telnet** is a protocol used for remote terminal connections that allows you to connect to and communicate with remote systems via the command line.

- Originally designed for remote administration
- Can connect to **any TCP port** — useful for testing services

### Common Test Servers

| Server | Default Port | Function |
|---|---|---|
| Echo Server | 7 | Echoes back everything you send |
| Daytime Server | 13 | Returns the current date and time |
| Web Server | 80 | Serves web pages (HTTP) |

```bash
telnet <IP address> <port>
```

---

## 8. DHCP (Dynamic Host Configuration Protocol)

**DHCP** automatically assigns IP addresses and network configuration to devices joining a network.

### The DORA Process

| Step | Name | Description |
|---|---|---|
| 1 | **Discover** | Device broadcasts asking if any DHCP server exists |
| 2 | **Offer** | DHCP server replies with an available IP, gateway, and DNS info |
| 3 | **Request** | Device confirms it wants the offered configuration |
| 4 | **Acknowledge** | Server confirms; device can now use the assigned IP |

---

## 9. ARP (Address Resolution Protocol)

**ARP** links IP addresses to MAC addresses so data can be delivered at the Ethernet level.

- IP address = address on the network
- MAC address = address of the actual network interface card
- ARP bridges Layer 3 (IP) and Layer 2 (MAC)

**How it works:**
1. Device broadcasts "Who has this IP? What is your MAC?"
2. Device with matching IP replies with its MAC address
3. Mapping is stored in the ARP cache for future use

---

## 10. ICMP (Internet Control Message Protocol)

**ICMP** is used for network diagnostics and troubleshooting.

| Tool | Command | Function |
|---|---|---|
| **Ping** | `ping <IP/URL>` | Tests connectivity; measures Round Trip Time (RTT) |
| **Traceroute** | `traceroute <IP/URL>` | Shows each hop (router) a packet passes through from source to destination |

---

## 11. NAT (Network Address Translation)

**NAT** translates private IP addresses to a public IP address so devices on a local network can communicate with the Internet.

- Home devices have **private IPs** (not routable on Internet)
- Router has a **public IP** assigned by ISP
- NAT maps outgoing private IPs to the public IP and tracks return traffic
- Also helps reduce **IPv4 address exhaustion**

---

## 12. DNS (Domain Name System)

**DNS** translates human-readable domain names into IP addresses so users don't have to remember numeric addresses.

### DNS Record Types

| Record | Full Name | Purpose |
|---|---|---|
| **A** | Address Record | Maps a hostname to an IPv4 address |
| **AAAA** | Quad-A Record | Maps a hostname to an IPv6 address |
| **CNAME** | Canonical Name | Maps one domain name to another (e.g. redirect `pixel.com` → `google.com`) |
| **MX** | Mail Exchange | Specifies the mail server responsible for handling emails for a domain |

### WHOIS

```bash
whois <domain>    # e.g. whois google.com
```

Returns: registered domain ID, registrar name, registrar URL, registration date, contact email, and more.

---

## 13. HTTP & HTTPS

**HTTP (HyperText Transfer Protocol)** and **HTTPS (HTTP Secure)** are used for accessing web pages.

### HTTP Methods

| Method | Purpose |
|---|---|
| **GET** | Retrieve data from the server |
| **POST** | Send data to the server |
| **PUT** | Update existing data on the server |
| **DELETE** | Delete data on the server |

### Connecting to a Web Server

**HTTP (plain):**
1. TCP three-way handshake
2. Communicate using HTTP (e.g. `GET / HTTP/1.1`)

**HTTPS (secure):**
1. TCP three-way handshake
2. Establish TLS session
3. Communicate using HTTP over TLS

---

## 14. FTP (File Transfer Protocol)

**FTP** is designed specifically for transferring files (unlike HTTP which retrieves web pages).

| Command | Purpose |
|---|---|
| `USER` | Provide username |
| `PASS` | Provide password |
| `RETR` | Retrieve (download) a file |
| `STOR` | Store (upload) a file |

---

## 15. SMTP (Simple Mail Transfer Protocol)

**SMTP** handles the **sending** of emails — how a mail client talks to a mail server and how mail servers talk to each other.

| Command | Purpose |
|---|---|
| `HELO` | Initiates an SMTP session |
| `MAIL FROM` | Specifies the sender's email address |
| `RCPT TO` | Specifies the recipient's email address |
| `DATA` | Begins the email body input |

---

## 16. POP3 & IMAP (Receiving Email)

**POP3 (Post Office Protocol v3)** — downloads emails from the server to the client.

Common commands: `USER`, `PASS`, `STAT`, `LIST`, `RETR`, `DELE`, `QUIT`

**IMAP (Internet Message Access Protocol)** — keeps emails synced on the server, accessible from multiple devices.

---

## 17. SSL & TLS

**TLS (Transport Layer Security)** is a cryptographic protocol that secures communication between a client and a server over an insecure network.

- **SSL** (Secure Sockets Layer) was the predecessor; SSL 2.0 released in 1995
- **TLS** was developed by IETF in 1999 as an upgrade to SSL 3.0
- TLS 1.3 (2018) brought significant security improvements
- Operates at the **Transport Layer** of the OSI model
- Ensures **confidentiality** (no one can read data) and **integrity** (no one can modify data)

### How TLS Certificates Work

1. Server admin creates a **Certificate Signing Request (CSR)**
2. Submits it to a **Certificate Authority (CA)**
3. CA verifies and issues a **digital certificate**
4. The signed certificate is installed on the server to prove its identity
5. Clients verify the certificate using the CA's root certificate installed on their system

### Adding TLS to Existing Protocols

| Plaintext Protocol | Secure (TLS) Version |
|---|---|
| HTTP | HTTPS |
| SMTP | SMTPS |
| POP3 | POP3S |
| IMAP | IMAPS |
| FTP | FTPS |

---

## 18. SSH (Secure Shell)

**SSH** is a cryptographic network protocol used for secure remote access to systems over an unsecured network. There are two versions — **SSH-1** and **SSH-2**, with SSH-2 being the modern standard. Most implementations are based on the **OpenSSH** library.

### Key Benefits of OpenSSH

| Benefit | Description |
|---|---|
| **Secure Authentication** | Verifies identity of users and hosts before granting access |
| **Confidentiality** | Encrypts all data in transit so no one can read it |
| **Integrity** | Ensures data has not been altered during transmission |
| **Tunneling** | Allows other protocols to be securely tunneled through SSH |
| **X11 Forwarding** | Enables graphical applications on a remote machine to be displayed locally |

```bash
ssh username@hostname
```

---

## 19. SFTP (SSH File Transfer Protocol)

**SFTP** is a secure file transfer protocol that is part of the **SSH protocol suite**. It provides the same functionality as FTP but over an encrypted connection.

- Runs on **port 22** (same as SSH)
- Must be enabled in the OpenSSH server configuration

```bash
sftp username@hostname
```

| Command | Purpose |
|---|---|
| `get <filename>` | Download a file from the remote machine |
| `put <filename>` | Upload a file to the remote machine |

> **SFTP vs FTP:** FTP sends data in plaintext — credentials and files can be intercepted. SFTP encrypts everything, making it the secure alternative.

---

## 20. VPN (Virtual Private Network)

### Why VPNs Were Built

The original TCP/IP protocol was designed to deliver packets reliably — not securely. Key gaps:

- **No confidentiality** — data could be read by anyone on the network
- **No integrity protection** — data could be altered in transit without detection

VPNs were developed as a cost-effective solution to these gaps.

### What a VPN Does

- Creates an **encrypted tunnel** between the user's device and a VPN server
- **Masks the user's real IP address** — destination sees the VPN server's IP
- Makes it appear as if the user is browsing from the **VPN server's location**

### Common Use Cases

| Use Case | Description |
|---|---|
| **Corporate Security** | Gives remote employees secure access to internal networks |
| **Privacy** | Hides browsing activity from ISPs and third parties |
| **Geo-restriction bypass** | Access region-locked content by connecting to a server in that country |
| **Public Wi-Fi Protection** | Encrypts traffic on untrusted networks |

### How It Works

```
User Device → [Encrypted Tunnel] → VPN Server → Internet
                                        ↑
                              Destination sees this IP
                              (not the user's real IP)
```

**Requirements:** Internet connectivity + VPN server + VPN client

---

## 🛠️ Tools Reference

| Tool | Purpose |
|---|---|
| `ping` | Test connectivity and measure RTT using ICMP |
| `traceroute` | Trace the path packets take across routers |
| `telnet` | Connect to remote systems or test TCP ports |
| `whois` | Look up domain registration information |
| `ipconfig` / `ifconfig` / `ip a s` | View IP address and network configuration |
| `ssh username@hostname` | Secure remote login |
| `sftp username@hostname` | Secure file transfer |
| Nmap | Network scanning and port discovery |
| tcpdump | Packet capture and analysis |

---

## 📡 Protocol Ports Reference

### Standard Protocols

| Protocol | Transport | Default Port |
|---|---|---|
| TELNET | TCP | 23 |
| DNS | UDP or TCP | 53 |
| HTTP | TCP | 80 |
| HTTPS | TCP | 443 |
| FTP | TCP | 21 |
| SMTP | TCP | 25 |
| POP3 | TCP | 110 |
| IMAP | TCP | 143 |
| SSH / SFTP | TCP | 22 |

### Secure (TLS) Versions

| Protocol | Default Port |
|---|---|
| HTTPS | 443 |
| SMTPS | 465 and 587 |
| POP3S | 995 |
| IMAPS | 993 |

---

## 📚 Key Concepts Learned

- OSI Model — all 7 layers, their functions and examples
- TCP/IP Model — 4 layers and how they map to OSI
- IPv4 vs IPv6 and why IPv6 is needed
- Private IP ranges (RFC 1918) — memorized
- Subnetting and subnet mask notation (e.g. `/24`)
- Routing and routing protocols (OSPF, EIGRP, BGP, RIP)
- TCP vs UDP — reliability, speed, and use cases
- TCP three-way handshake (SYN, SYN/ACK, ACK)
- Encapsulation across OSI layers
- Telnet for testing TCP services
- DHCP DORA process
- ARP — linking IP to MAC addresses
- ICMP — ping and traceroute
- NAT — private to public IP translation
- DNS record types (A, AAAA, CNAME, MX) and WHOIS
- HTTP methods (GET, POST, PUT, DELETE) and ports
- FTP for file transfer; SMTP for sending email; POP3/IMAP for receiving
- SSL/TLS — how it works and certificate authorities
- Securing protocols with TLS (HTTPS, SMTPS, POP3S, IMAPS)
- SSH — secure remote access; OpenSSH and its 5 key benefits
- SFTP — secure file transfer over SSH on port 22
- VPN — encrypted tunnels, IP masking, use cases, and requirements

---

*Notes from hands-on learning on TryHackMe. All labs performed in a legal, controlled environment.*
