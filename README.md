# 🔥 Botnet IP Firewall Blocker – Python Script for Windows

A Python tool that fetches **real-time botnet and malware-related IP addresses** from [abuse.ch] and automatically blocks them using **Windows Firewall rules**.

This script is part of an enterprise-grade **centralized system security hardening** initiative at **P.E. Mathew & Company**, designed to reduce the risk of malware calling back to known command-and-control (C2) servers.

## ✅ Features

- 📡 **Fetches live threat intel** from [abuse.ch IP blocklists]
- 🛡️ Automatically applies **inbound and outbound firewall rules** for each IP
- 🧱 Helps **block botnet traffic and prevent malware callbacks**
- 💻 Designed for **Windows 10/11 Pro or Enterprise**, with admin privileges

## 📦 Requirements

- Python 3.6+
- Internet connection (to fetch live threat data)
- Windows 10/11 (Pro or Enterprise)
- **Admin privileges** (to add firewall rules)

## ⚙️ How to Use

1. Clone the repository:
   git clone https://github.com/Upasara/PEMcore.git
   cd botnet-ip-firewall-blocker

2. Run the script:
   python firewall_blocker.py
