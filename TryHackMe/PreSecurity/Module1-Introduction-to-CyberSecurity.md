NOTE:This notes are structured using AI

## Module 1: Introduction to Cybersecurity

> **Platform:** TryHackMe  
> **Path:** Penetration Testing  
> **Status:** ✅ Completed

---

## 📌 Overview

This module introduced the two core pillars of cybersecurity — **Offensive Security** and **Defensive Security** — along with hands-on lab practice and an overview of career paths in the field.

---

## 1. Offensive Security

### What is Offensive Security?
Offensive security involves thinking and acting like an attacker to find vulnerabilities before malicious actors do. The goal is to proactively identify and exploit weaknesses in systems, applications, and networks.

### 🔬 Lab — Hacking a Bank Application
Completed a simulated bank application hack to understand real-world attack vectors.

**Scenario:**
- Accessed a mock banking UI showing account details (account number, cash balance, etc.)
- Goal: Find hidden/sensitive functionality not intended for regular users

**Technique Used: Hidden URL Discovery (Forced Browsing)**

Applications sometimes expose sensitive functionality through secret or unlinked URLs. By discovering these, an attacker can perform actions a normal user shouldn't be able to.

**Tool: DIRB**

DIRB is a web content scanner that uses a brute-force approach to find hidden pages and directories.

**How it works:**
1. Takes a wordlist of common/potential page names (e.g., `common.txt`)
2. Tests each name against the target website one by one
3. Returns URLs that exist, including hidden or sensitive ones

**Command used:**
```bash
dirb <website_url>
```

**Result:** Discovered hidden URLs exposing sensitive endpoints (e.g., `/bank-transfer`) that allowed actions beyond normal user permissions.

---

## 2. Defensive Security

### What is Defensive Security?
Defensive security focuses on **protecting** systems, detecting threats, and responding to incidents. Unlike offensive security, the goal is to prevent and mitigate attacks.

### Key Roles in Defensive Security

| Role | Responsibility |
|---|---|
| **SOC (Security Operations Center)** | Monitors systems 24/7 for suspicious activity |
| **Threat Intelligence** | Gathers info on actual and potential threat actors |
| **DFIR (Digital Forensics & Incident Response)** | Investigates incidents and recovers evidence |
| **Malware Analysis** | Analyzes malicious software to understand behavior |

### Threat Intelligence
- Involves learning about adversaries — their **tactics, techniques, and procedures (TTPs)**
- Helps predict attacker behavior and prepare defense strategies
- Goal: Identify threat actors early and mitigate attacks before they cause damage

### SIEM (Security Information and Event Management)
- A tool used by SOC teams to **aggregate security events and logs** from multiple sources into a single dashboard
- Generates alerts when suspicious activity is detected
- Security analysts review alerts and determine which are genuine threats

**Practical Example:**
> A bank's SOC uses a SIEM tool to collect events across their network. When the SIEM flags a suspicious login, an analyst investigates whether it's a real threat or a false positive.

### Identifying Suspicious Activity
Practiced spotting real-world indicators of malicious activity, including:
- 🚩 Suspicious emails (fake senders, unusual reasons, unfamiliar names)
- 🚩 Phishing login pages mimicking legitimate websites
- 🚩 Suspicious/malicious links
- 🚩 Any communication that feels "off" or unverifiable

---

## 3. Careers in Cybersecurity

Explored the major roles across both offensive and defensive security:

| Role | Description |
|---|---|
| **Security Analyst** | Monitors and analyzes security events; identifies threats |
| **Security Engineer** | Builds and maintains security systems and infrastructure |
| **Incident Responder** | Responds to and contains active security breaches |
| **Digital Forensics Examiner** | Collects and analyzes digital evidence post-incident |
| **Malware Analyst** | Reverse engineers malware to understand its purpose and impact |
| **Penetration Tester** | Ethically hacks systems to find vulnerabilities before attackers do |
| **Red Teamer** | Simulates full-scale attacks to test an organization's overall defenses |

> **Note:** Security Analyst vs Security Engineer — Analysts focus on *monitoring and detection*, while Engineers focus on *building and maintaining* security tools and infrastructure.

---

## 🛠️ Tools Encountered
- **DIRB** — Web content brute-forcer for discovering hidden URLs
- **SIEM** — Security event aggregation and alerting platform

## 📚 Key Concepts Learned
- Offensive vs Defensive Security mindset
- Forced browsing / hidden URL discovery
- Threat intelligence and TTPs
- How SOC teams operate with SIEM tools
- Identifying phishing and suspicious activity
- Cybersecurity career landscape

---

*Notes from hands-on learning on TryHackMe. All labs performed in a legal, controlled environment.*
