# 🔥 DNS TOOL Toolkit by lyn4x

A modular Termux-based cybersecurity tool for DNS TEST, scanning, and ethical reconnaissance. Built for learners, educators, and professionals who want fast, reliable DNS insights with a splash of style.

---

## 🧠 Features

- ✅ DNS resolution with logging  
- ✅ WHOIS lookup  
- ✅ Subdomain scanner (basic)  
- ✅ DNS benchmarking (response time)  
- ✅ DNS vulnerability finder (zone transfer, wildcard detection)  
- ✅ Nmap integration (port & service scan)  
- ✅ Masscan integration (ultra-fast port scan)  
- ✅ Auto-installs Python dependencies  
- ✅ ASCII splash screen and menu system  
- ✅ Designed for Termux and Linux  

---

## ⚙️ Installation

### 📱 Termux

```bash
# 1. Update Termux and install core packages
pkg update && pkg upgrade
pkg install python git nmap clang

# 2. Clone the repository
git clone https://github.com/gameraazvb/DNS-TOOL.git
cd DNS-TOOL

# 3. Build Masscan (optional but recommended)
git clone https://github.com/robertdavidgraham/masscan
cd masscan
make
cd ..
and use --rate for custom request dont go eg:10000000000 it will cause problem 

# 4. Run the tool
python dnsfucker.py

### kali linux
# 1. Update system and install core packages
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 git nmap clang make

# 2. Clone the repository
git clone https://github.com/gameraazvb/DNS-TOOL.git
cd DNS-TOOL

# 3. Build Masscan (optional but recommended)
git clone https://github.com/robertdavidgraham/masscan
cd masscan
make
cd ..

# 4. Run the tool
python3 dnsfucker.py

