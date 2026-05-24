ARPGuard: ARP Spoofing Detection and Visualization

ARPGuard is a Python-based tool designed to detect ARP spoofing attacks and visualize network topology in real-time. It uses Scapy for packet manipulation, Tkinter for the dashboard, and NetworkX for network graph visualization. This project is suitable for educational and small-scale network security monitoring.

Table of Contents

Installation

Usage

Features

Project Structure

Dependencies

Contributing

License

Installation

Clone the repository:
git clone https://github.com/yourusername/ARPGuard.git
cd ARPGuard

Install dependencies:
pip install scapy tkinter networkx matplotlib requests

Usage

ARP Spoofing (attacker.py)
Run the attacker module to simulate ARP spoofing:
python attacker.py <target_ip> <spoof_ip>
Replace <target_ip> and <spoof_ip> with the respective IP addresses.

ARP Detection (detector.py)
Start the detector to monitor ARP packets:
python detector.py
The detector will print alerts if it detects ARP anomalies.

Visualization Dashboard (ui.py)
Launch the dashboard for network visualization:
python ui.py
The dashboard will display a network graph and allow you to view ARP alerts.

Features

Real-time ARP packet sniffing and anomaly detection.

Network topology visualization using NetworkX and Matplotlib.

Simple Tkinter-based dashboard for monitoring.

Modular design for easy extension.

Project Structure

ARPGuard/
├── attacker.py # ARP spoofing module
├── detector.py # ARP detection module
├── ui.py # Visualization dashboard
├── alerts.py # Alerting module (Telegram/Slack)
└── README.md # This file

Dependencies

Python 3.7+

Scapy

Tkinter

NetworkX

Matplotlib

Requests