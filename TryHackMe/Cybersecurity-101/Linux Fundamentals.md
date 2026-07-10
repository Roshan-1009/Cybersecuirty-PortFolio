# TryHackMe — Pre-Security Path
## Module 3: Linux Fundamentals (Parts 1, 2 & 3)

> **Platform:** TryHackMe  
> **Path:** Penetration Testing  
> **Status:** ✅ Completed

---

## 📌 Overview

This module covered the essentials of using Linux — from basic terminal commands to file permissions, process management, automation, and system maintenance. Split across three parts, it builds practical Linux skills essential for cybersecurity work.

---

## Part 1 — Introduction to Linux

### Why Linux?
Linux is widely used in cybersecurity due to its flexibility, open-source nature, and the large variety of security-focused distributions (flavors) available (e.g. Kali Linux, Ubuntu, Parrot OS).

### Basic Commands

| Command | Description |
|---|---|
| `echo` | Prints text to the terminal |
| `whoami` | Displays the current logged-in user |
| `ls` | Lists files and directories |
| `cd` | Changes the current directory |
| `cat` | Concatenates and displays file contents |
| `pwd` | Prints the current working directory |

### Searching for Files

| Command | Description |
|---|---|
| `find` | Searches for files and directories by name, type, size, etc. |
| `grep` | Searches for specific text/patterns within files |
| `grep -r` | Recursively searches through directories and subdirectories |

### Shell Operators

| Operator | Description |
|---|---|
| `&&` | Runs the second command only if the first succeeds |
| `>` | Redirects output to a file (overwrites existing content) |
| `>>` | Redirects output to a file (appends to existing content) |

---

## Part 2 — Flags, Permissions & The Filesystem

### Flags & Switches
Most Linux commands accept **flags** (arguments preceded by a hyphen) that modify their behaviour.

**Example:** `ls -a` (the `-a` flag shows all files, including hidden ones)

**How to find available flags:**
```bash
<command> --help      # Quick reference for flags
man <command>         # Full manual page (e.g. man ls)
```

### File Management Commands

| Command | Description |
|---|---|
| `touch` | Creates a new empty file |
| `mkdir` | Creates a new directory |
| `cp` | Copies a file or directory |
| `mv` | Moves or renames a file or directory |
| `rm` | Removes a file |
| `file` | Determines the type of a file |

### File Permissions

The command `ls -lh` displays files with detailed permission and ownership information.

**Permission format:** `rwxrwxrwx` → (User)(Group)(Others)

| Character | Meaning |
|---|---|
| `r` | Read |
| `w` | Write |
| `x` | Execute |
| `-` | Permission not granted |

**Modifying permissions:**
```bash
chmod <permissions> <file>    # Change file permissions
```

### Switching Users

| Command | Description |
|---|---|
| `su <username>` | Switch to another user |
| `su -l <username>` | Switch to another user and load their environment |

### Important Filesystem Directories

| Directory | Purpose |
|---|---|
| `/etc` | System configuration files |
| `/var` | Variable data (logs, databases) |
| `/root` | Home directory of the root user |
| `/tmp` | Temporary files; cleared on reboot |

---

## Part 3 — Terminal Skills, Processes & Automation

### Text Editors

| Tool | Description |
|---|---|
| `nano` | Beginner-friendly terminal text editor |
| `vim` | Advanced, highly configurable terminal text editor |
| `echo` | Can also be used to write content into files using `>` or `>>` |

### File Transfer Utilities

**SCP (Secure Copy)** — Securely copies files between machines over SSH:
```bash
scp <source> <user>@<host>:<destination>
```

**Serving files over HTTP** — Host a file using Python's built-in HTTP server:
```bash
python3 -m http.server
```

Then download from another machine using:
```bash
wget <URL>      # Download a file
curl <URL>      # Transfer data from a URL
```

### Process Management

| Command | Description |
|---|---|
| `ps` | Lists currently running processes |
| `ps aux` | Lists all running processes for all users with details |

**Process signals:**

| Signal | Description |
|---|---|
| `SIGTERM` | Gracefully terminate a process |
| `SIGKILL` | Forcefully kill a process immediately |
| `SIGSTOP` | Pause/suspend a process |

### PID (Process ID)
Every running process is assigned a unique **PID**. This is used to manage and target specific processes.

### systemd & systemctl

**systemd** is the init system used by Linux to manage services and processes at startup.

**systemctl** is the command used to interact with systemd:
```bash
systemctl start <service>      # Start a service
systemctl stop <service>       # Stop a service
systemctl enable <service>     # Enable service to start on boot
systemctl status <service>     # Check service status
```

### Automation with Crontabs

**Crontabs** allow scheduling commands to run automatically at set intervals.

```bash
crontab -e      # Edit crontab (create/modify scheduled tasks)
crontab -l      # List current crontab entries
```

**Crontab syntax:**
```
* * * * * <command>
│ │ │ │ │
│ │ │ │ └── Day of week (0-7)
│ │ │ └──── Month (1-12)
│ │ └────── Day of month (1-31)
│ └──────── Hour (0-23)
└────────── Minute (0-59)
```

### Package Management

| Command | Description |
|---|---|
| `apt` | Package manager for installing/removing software |
| `sudo apt install <package>` | Install a package |
| `sudo add-apt-repository` | Add a new software repository as a source |

> `sudo` (superuser do) runs commands with elevated/root privileges.

### System Logs

Linux maintains logs that help monitor system activity and troubleshoot issues.

| Log File | Purpose |
|---|---|
| `/var/log/auth.log` | Authentication events (logins, sudo usage) |
| `/var/log/syslog` | General system activity |
| `/var/log/error.log` | System and application errors |

> Reviewing logs is a critical skill in cybersecurity for detecting suspicious activity and investigating incidents.

---

## 🛠️ Commands Reference Summary

```bash
# Navigation & Files
echo, whoami, ls, cd, cat, pwd, find, grep, grep -r

# File Management
touch, mkdir, cp, mv, rm, file, chmod, su, su -l

# Text Editors
nano, vim

# File Transfer
scp, python3 -m http.server, wget, curl

# Processes
ps, ps aux, SIGTERM, SIGKILL, SIGSTOP

# Services
systemctl start/stop/enable/status

# Automation
crontab -e, crontab -l

# Package Management
sudo apt install, sudo add-apt-repository

# Help
--help, man
```

## 📚 Key Concepts Learned
- Why Linux is essential in cybersecurity and its various distributions
- Core terminal navigation and file management commands
- Using flags and switches to extend command functionality
- Linux file permissions (read, write, execute) and how to modify them
- Switching between users and understanding root privileges
- Important Linux filesystem directories (`/etc`, `/var`, `/root`, `/tmp`)
- Transferring files securely with SCP and serving via HTTP
- Managing and killing processes using signals and PIDs
- systemd and systemctl for service management
- Automating tasks with crontabs
- Managing packages with APT
- Reading and interpreting system logs for security monitoring

---

*Notes from hands-on learning on TryHackMe. All labs performed in a legal, controlled environment.*
