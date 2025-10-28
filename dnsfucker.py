import os
import sys
import time
import socket
import shutil
import subprocess

# Detect environment
def is_termux():
    return os.path.exists("/data/data/com.termux/files/usr/bin/pkg")

def is_kali():
    return os.path.exists("/etc/os-release") and "Kali" in open("/etc/os-release").read()

# Safe pip install for Kali
def safe_pip_install(packages):
    args = [sys.executable, "-m", "pip", "install"] + packages
    if is_kali():
        args.append("--break-system-packages")
    subprocess.run(args)

# Auto-install Python dependencies
def install_python_deps():
    required = ["pyfiglet", "termcolor", "dnspython", "python-whois", "requests"]
    try:
        for pkg in required:
            __import__(pkg if pkg != "python-whois" else "whois")
    except ImportError:
        print("Installing missing Python dependencies...")
        safe_pip_install(required)

# Check and install external tools
def check_tool(tool):
    return shutil.which(tool) is not None

def install_external_tools():
    tools = ["masscan", "ettercap", "bettercap"]
    missing = [t for t in tools if not check_tool(t)]
    if missing:
        print(colored(f"Installing missing tools: {', '.join(missing)}", "yellow"))
        installer = "pkg" if is_termux() else "apt"
        result = subprocess.run([installer, "install", "-y"] + missing)
        if result.returncode != 0:
            fallback_repos = {
                "masscan": "https://github.com/robertdavidgraham/masscan.git",
                "ettercap": "https://github.com/Ettercap/ettercap.git",
                "bettercap": "https://github.com/bettercap/bettercap.git"
            }
            for tool in missing:
                print(colored(f"Cloning {tool} from GitHub...", "yellow"))
                subprocess.run(["git", "clone", fallback_repos[tool]])
        print(colored("Tools installed. Please re-run the script.", "green"))
        exit()

# Imports after setup
install_python_deps()
import pyfiglet
from termcolor import colored
import dns.resolver
import dns.query
import dns.zone
import whois
import requests

# Setup tools
install_external_tools()

# Clear screen
os.system('clear')

# Banner
banner = pyfiglet.figlet_format("DNS FUCKER", font="slant")
print(colored(banner, 'red'))
print(colored("Author: lyn4x | Tool: DNS FUCKER", "cyan"))
print(colored("Initializing modules...", "yellow"))
time.sleep(1)

# Menu system
def show_menu():
    print(colored("\nSelect an option:", "blue"))
    print(colored("1. Resolve a domain", "yellow"))
    print(colored("2. View DNS log", "yellow"))
    print(colored("3. About", "yellow"))
    print(colored("4. WHOIS Lookup", "yellow"))
    print(colored("5. Subdomain Scanner", "yellow"))
    print(colored("6. DNS Benchmark", "yellow"))
    print(colored("7. DNS Vulnerability Finder", "yellow"))
    print(colored("8. Nmap Scan", "yellow"))
    print(colored("9. Masscan Scan", "yellow"))
    print(colored("10. Ettercap Sniffing", "yellow"))
    print(colored("11. Bettercap Sniffing", "yellow"))
    print(colored("0. Exit", "yellow"))

# [Insert your original function definitions here: resolve_domain(), view_log(), etc.]

# Main loop
while True:
    show_menu()
    choice = input(colored("\nEnter your choice: ", "blue"))
    if choice == "1":
        resolve_domain()
    elif choice == "2":
        view_log()
    elif choice == "3":
        about()
    elif choice == "4":
        whois_lookup()
    elif choice == "5":
        subdomain_scan()
    elif choice == "6":
        dns_benchmark()
    elif choice == "7":
        dns_vulnerability_scan()
    elif choice == "8":
        nmap_scan()
    elif choice == "9":
        masscan_scan()
    elif choice == "10":
        ettercap_sniff()
    elif choice == "11":
        bettercap_sniff()
    elif choice == "0":
        print(colored("Exiting... Stay ethical, lyn4x!", "green"))
        break
    else:
        print(colored("Invalid choice. Try again.", "red"))
