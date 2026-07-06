NOTE:This notes are structured using AI
# TryHackMe — Pre-Security Path
## Module 2: Network Fundamentals

> **Platform:** TryHackMe  
> **Path:** Penetration Testing  
> **Status:** ✅ Completed

---

## 📌 Overview

This module covered the foundations of computer networking — from what a network is, to how data travels across the internet, to the devices and protocols that make it all work.

---

## 1. What is a Network?

A **network** is simply devices connected together to share resources and communicate. Networks come in all shapes and sizes.

### The Internet
The Internet is one giant network made up of many smaller private networks joined together.

- **Private Networks** — small internal networks (e.g. home, office)
- **Public Networks** — the infrastructure connecting private networks together (i.e. the Internet)

### Brief History
- **ARPANET** — the first documented network, funded by the US Department of Defense
- **WWW (World Wide Web)** — invented by **Tim Berners-Lee in 1989**, enabling the modern Internet

---

## 2. IP Addresses

An **IP (Internet Protocol) address** is a set of numbers divided into **four octets** used to identify a device on a network for a period of time. IP addresses can change between devices but cannot be active on more than one device simultaneously within the same network.

### Public vs Private IP
| Type | Description |
|---|---|
| **Private IP** | Used to identify devices within a local network |
| **Public IP** | Assigned by your ISP; shared by all devices on the same router |

> Two devices on the same router share the same public IP but have different private IPs. All outgoing traffic is identified by the public IP.

### IPv4 vs IPv6
| Version | Address Space | Notes |
|---|---|---|
| **IPv4** | 2³² ≈ 4.29 billion addresses | Current standard; running out of addresses |
| **IPv6** | 2¹²⁸ ≈ 340+ trillion addresses | New standard; solves shortage, more efficient |

> Cisco estimated over 50 billion connected devices by 2021 — far exceeding IPv4's capacity, making IPv6 essential.

---

## 3. MAC Addresses

Every device has a **Network Interface Card (NIC)** with a permanently assigned **MAC (Media Access Control) address** set at the factory.

- Format: **12-character hexadecimal**, separated by colons (e.g. `a4:c3:f0:85:ac:2d`)
- First 6 characters → **manufacturer identifier**
- Last 6 characters → **unique device identifier**

### MAC Spoofing
MAC addresses can be **spoofed** — a device pretends to be another by faking its MAC address.

**Real-world implications:**
- Bypassing MAC-based firewall rules
- Gaining unauthorized access to paid/restricted Wi-Fi networks by copying an authorized device's MAC address
- This is why connecting to public Wi-Fi carries security risks

---

## 4. Ping & ICMP

**Ping** is a fundamental networking tool that uses **ICMP (Internet Control Message Protocol)** to test connectivity and measure **latency** between devices.

**Command:**
```bash
ping <IP address>
# or
ping <website URL>
```

- Sends ICMP packets to the target and measures response time
- Results show average round-trip time across all packets sent
- Useful for diagnosing connectivity issues

---

## 5. LAN Topologies

Networks can be physically arranged in different topologies, each with trade-offs:

| Topology | Description | Advantages | Disadvantages |
|---|---|---|---|
| **Star** | All devices connect to a central switch/hub | Reliable; easy to add devices | Expensive; central point of failure |
| **Bus** | All devices share a single backbone cable | Simple; cheap | Slow under heavy traffic; hard to troubleshoot |
| **Ring** | Devices connected in a loop | Easy to troubleshoot | Single break disrupts the network |

### Switch vs Hub
- **Hub** — broadcasts data to all devices on the network
- **Switch** — intelligently sends data only to the intended device (more efficient and secure)

### Router
- Connects multiple networks together
- Determines the best path for data to travel
- Operates at **Layer 3** of the OSI model

---

## 6. Subnetting

**Subnetting** is the process of dividing a network into smaller sub-networks (subnets).

### Why Subnet?
Subnetting provides:
- ✅ **Efficiency** — reduces unnecessary traffic
- ✅ **Security** — departments (e.g. Accounting, HR, Finance) are isolated from each other
- ✅ **Scalability** — easier to manage large networks

### Key Concepts
| Term | Description |
|---|---|
| **Network Address** | Identifies the subnet itself |
| **Host Address** | Identifies individual devices within the subnet |
| **Default Gateway** | The router address that traffic is sent to when leaving the subnet |
| **Subnet Mask** | Defines how an IP address is split between network and host portions |

IP addresses are divided into **four octets**, and the subnet mask determines which part identifies the network vs the device.

---

## 7. ARP (Address Resolution Protocol)

**ARP** allows devices to map **IP addresses to MAC addresses** on a local network.

### How it Works
1. **ARP Request** — device broadcasts "Who has this IP address? What is your MAC?"
2. **ARP Reply** — the device with that IP responds with its MAC address
3. The requesting device stores this mapping in its **ARP cache** for future use

> ARP bridges the gap between Layer 2 (MAC) and Layer 3 (IP) addressing.

---

## 8. DHCP (Dynamic Host Configuration Protocol)

**DHCP** automatically assigns IP addresses to devices joining a network (instead of manual configuration).

### 4-Step DHCP Process
| Step | Name | Description |
|---|---|---|
| 1 | **DHCP Discover** | Device broadcasts asking if any DHCP server exists |
| 2 | **DHCP Offer** | Server replies with an available IP address |
| 3 | **DHCP Request** | Device confirms it wants the offered IP |
| 4 | **DHCP ACK** | Server acknowledges; device can now use the IP |

---

## 9. The OSI Model

The **OSI (Open Systems Interconnection)** model is a 7-layer framework describing how data is transmitted across a network.

| Layer | Name | Key Function |
|---|---|---|
| 7 | **Application** | User-facing protocols; how users interact with network services |
| 6 | **Presentation** | Data translation/formatting so different software can communicate |
| 5 | **Session** | Creates and maintains connections between devices |
| 4 | **Transport** | Data transfer using TCP or UDP; handles error checking |
| 3 | **Network** | Routing and reassembly of data; optimal path selection |
| 2 | **Data Link** | Physical MAC addressing; adds MAC address to packets |
| 1 | **Physical** | Raw binary data transmission over hardware |

---

## 10. Packets & Frames

Data is broken into small chunks for transmission:

| Term | Layer | Contains |
|---|---|---|
| **Packet** | Layer 3 | IP addresses + payload |
| **Frame** | Layer 2 | Encapsulates packet + MAC addresses |

### Packet Headers
- **Time to Live (TTL)** — prevents packets looping forever
- **Checksum** — error checking
- **Source Address** — sender's IP
- **Destination Address** — recipient's IP

---

## 11. TCP/IP & The Three-Way Handshake

**TCP (Transmission Control Protocol)** ensures reliable data delivery.

### TCP Headers
Source Port, Destination Port, Source IP, Destination IP, Sequence Number, Acknowledgment Number, Checksum, Data, Flags

### Three-Way Handshake
| Step | Flag | Description |
|---|---|---|
| 1 | **SYN** | Client initiates connection |
| 2 | **SYN/ACK** | Server acknowledges and responds |
| 3 | **ACK** | Client confirms; connection established |
| — | **Data** | Data transmission begins |
| — | **FIN** | Graceful connection close |
| — | **RST** | Abrupt connection reset |

### TCP vs UDP
| Feature | TCP | UDP |
|---|---|---|
| Reliability | ✅ Guaranteed delivery | ❌ No guarantee |
| Speed | Slower | ✅ Faster |
| Use Case | Web, file transfers | Streaming, gaming, VoIP |

### Common Ports
| Port | Protocol |
|---|---|
| 21 | FTP (File Transfer Protocol) |
| 22 | SSH (Secure Shell) |
| 80 | HTTP |
| 443 | HTTPS |
| 445 | SMB (Server Message Block) |
| 3389 | RDP (Remote Desktop Protocol) |

---

## 12. Port Forwarding

**Port forwarding** allows external devices to access services hosted on a private network by mapping a public port to an internal IP and port.

> Example: Hosting a website locally and making it accessible to the outside world via the router.

---

## 13. Firewalls

A **firewall** controls what traffic is allowed in and out of a network based on defined rules.

### Firewall Types
| Type | Description |
|---|---|
| **Stateless** | Inspects each packet individually against static rules |
| **Stateful** | Tracks the state of connections; smarter and more secure |

Firewalls operate at specific layers of the OSI model and can be configured to block malicious packets from reaching servers.

---

## 14. VPN (Virtual Private Network)

A **VPN** creates an encrypted tunnel between networks or devices over the Internet, enabling:
- Secure communication across different geographic locations
- Privacy by masking real IP addresses

### VPN Technologies
| Technology | Description |
|---|---|
| **PPP** | Base tunneling protocol; handles authentication and encryption |
| **PPTP** | Point-to-Point Tunneling Protocol; easy to set up, older standard |
| **IPSec** | Strong encryption; widely used in enterprise VPNs |

---

## 15. LAN Networking Devices

### Router
- Connects different networks together
- Operates at **Layer 3** (Network layer)
- Determines the optimal path for data

### Switch
- Connects devices within the same network
- More intelligent than a hub — sends data only to the intended device
- **Layer 2 Switch** — uses MAC addresses
- **Layer 3 Switch** — can also perform routing functions

### VLAN (Virtual Local Area Network)
- Logically splits a physical network into separate virtual networks
- Improves **security** and **privacy** between departments (e.g. HR can't access Finance traffic)

---

## 🛠️ Tools Encountered
- **Ping** — ICMP-based connectivity and latency testing

## 📚 Key Concepts Learned
- Network types (private vs public), ARPANET, WWW history
- IPv4 vs IPv6, public vs private IPs
- MAC addresses and MAC spoofing
- ARP — mapping IPs to MACs
- DHCP — automatic IP assignment (4-step process)
- OSI Model — all 7 layers and their functions
- Packets vs Frames and their headers
- TCP three-way handshake and TCP vs UDP
- Common ports and protocols
- Port forwarding, firewalls (stateful vs stateless)
- VPN technologies (PPP, PPTP, IPSec)
- LAN devices: routers, switches, VLANs
- Subnetting — efficiency, security, scalability

---

*Notes from hands-on learning on TryHackMe. All labs performed in a legal, controlled environment.*
