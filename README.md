# 🔥 DNS FUCKER Toolkit by lyn4x

A modular Termux-based cybersecurity tool for DNS FUCKING, scanning, and ethical reconnaissance. Built for learners, educators, and professionals who want fast, reliable DNS insights with a splash of style.

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

## ⚙️ Installation (Termux)

### 1. Update Termux and install core packages
```bash
pkg update && pkg upgrade
pkg install python git nmap clang
### 2. clone the repository
git clone https://github.com/gameraazvb/DNS-FUCKER-TERMUX.git
cd DNS-FUCKER-TERMUX
### 3. Build Masscan (optional but recommended)
git clone https://github.com/robertdavidgraham/masscan
cd masscan
make
cd ..
### 4. usage
python dnsfucker.py

