
# ARPGuard – Real-Time ARP Spoofing Detection & Network Visualization

## Overview
ARPGuard is a Python-based cybersecurity project designed to detect, visualize, and respond to ARP Spoofing / ARP Poisoning attacks in real time.

The project combines:
- Real-time ARP packet monitoring
- ARP anomaly detection
- Network topology visualization
- Telegram alert integration
- Automated response mechanisms
- GUI dashboards using Tkinter
- Graph-based network mapping using NetworkX

This project is intended for:
- Cybersecurity students
- Ethical hacking labs
- Network security research
- Educational demonstrations
- Small-scale LAN monitoring

------------------------------------------------------------

## Features

### Real-Time ARP Monitoring
- Continuously sniffs ARP packets using Scapy
- Monitors IP ↔ MAC mappings
- Detects suspicious changes instantly

### ARP Spoofing Detection
- Detects multiple MAC addresses for a single IP
- Prints real-time alerts
- Helps identify MITM attacks

### Network Visualization
- Uses NetworkX + Matplotlib
- Displays device relationships graphically
- GUI dashboard with Tkinter

### Telegram Alert Integration
- Sends attack notifications to Telegram
- Can be extended to Slack/Discord

### Automated Response
- Block attacker MAC addresses
- Configure static ARP entries
- Restore correct mappings

### Modular Design
Separate modules for:
- Detection
- Visualization
- Attacking
- Alerts
- Response handling

------------------------------------------------------------

## Project Structure

ARPGuard/
│
├── attacker.py          # Simulates ARP spoofing attack
├── detector.py          # Detects ARP anomalies
├── alert.py             # Telegram alert integration
├── reponse.py           # Automated response mechanisms
├── ui.py                # Basic GUI dashboard
├── ui_advanced.py       # Advanced visualization dashboard
├── README.md            # Project documentation
│
└── requirements.txt     # Dependencies

------------------------------------------------------------

## Technologies Used

- Python
- Scapy
- Tkinter
- NetworkX
- Matplotlib
- Requests
- iptables

------------------------------------------------------------

## Installation

### Clone the Repository

git clone https://github.com/yourusername/ARPGuard.git
cd ARPGuard

### Create Virtual Environment

Linux / Mac:
python3 -m venv venv
source venv/bin/activate

Windows:
python -m venv venv
venv\Scripts\activate

### Install Dependencies

pip install scapy networkx matplotlib requests

------------------------------------------------------------

## Requirements

Python 3.7+
Scapy
Tkinter
NetworkX
Matplotlib
Requests

------------------------------------------------------------

## Usage

### 1. ARP Spoofing Simulation

Run:
sudo python attacker.py <target_ip> <spoof_ip>

Example:
sudo python attacker.py 192.168.1.5 192.168.1.1

What it does:
- Sends fake ARP replies
- Associates attacker MAC with router IP
- Redirects victim traffic through attacker

------------------------------------------------------------

### 2. ARP Detection Engine

Run:
sudo python detector.py

Detection logic:
- Tracks IP ↔ MAC mappings
- Detects when one IP changes MAC address
- Raises alerts for anomalies

Example Alert:
ALERT: ARP anomaly for IP 192.168.1.1

------------------------------------------------------------

### 3. Visualization Dashboard

Run:
python ui.py

Features:
- Displays network graph
- Shows IP ↔ MAC relationships
- Tkinter-based interface

------------------------------------------------------------

### 4. Advanced Dashboard

Run:
python ui_advanced.py

Features:
- Embedded Matplotlib graphs
- Interactive GUI
- Real-time topology updates

------------------------------------------------------------

### 5. Telegram Alert System

Configure:
token = "YOUR_BOT_TOKEN"
chat_id = "YOUR_CHAT_ID"

Usage:
send_telegram_alert(
    "ARP Spoofing Detected!",
    token,
    chat_id
)

------------------------------------------------------------

### 6. Automated Defense Mechanisms

Features:
- Block malicious MAC addresses
- Configure static ARP entries
- Restore correct mappings

------------------------------------------------------------

## Testing Environment

Recommended Lab Setup:

- Kali Linux VM → Attacker
- Ubuntu VM → Detector
- Windows/Linux VM → Victim
- Router VM → Gateway

------------------------------------------------------------

## Future Enhancements

- Flask Web Dashboard
- Machine Learning Anomaly Detection
- Cloud Logging Support
- Wireless Network Monitoring
- Multi-threaded Packet Processing
- Threat Intelligence Integration

------------------------------------------------------------

## Development Roadmap

Phase 1:
- Linux VMs
- ARP fundamentals
- Wireshark packet analysis

Phase 2:
- ARP poisoning using Scapy
- MITM attack simulation

Phase 3:
- Real-time packet sniffing
- Anomaly detection
- Auto-recovery system

Phase 4:
- Dashboard visualization
- Network graph generation
- Alert integration

Phase 5:
- Modular architecture
- Testing
- Documentation
- Final presentation

------------------------------------------------------------

## Security Disclaimer

This project is intended strictly for:
- Educational purposes
- Authorized penetration testing
- Cybersecurity research
- Lab environments

Do NOT use this tool on unauthorized networks.

------------------------------------------------------------

## Author

Tarun V
Cybersecurity Engineer 
