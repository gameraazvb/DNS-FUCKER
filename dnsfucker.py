# ASCII banner demo for Termux tools
import pyfiglet
from termcolor import colored
import time
import os
import socket

# Clear the terminal screen
os.system('clear')  # Use 'cls' on Windows

# Create ASCII banner
banner = pyfiglet.figlet_format("DNS FUCKER", font="slant")
colored_banner = colored(banner, 'red')

# Print with delay for dramatic effect
print(colored_banner)
print(colored("Author: Mohamed | Tool: DNS Validator", "cyan"))
print(colored("Initializing modules...", "yellow"))
time.sleep(1)
print(colored("Checking DNS configuration...", "yellow"))
time.sleep(1)
print(colored("Ready to launch!", "green"))
time.sleep(1)

# Ask user for domain
domain = input(colored("\nEnter a domain to resolve: ", "blue"))

# DNS resolution
try:
    ip = socket.gethostbyname(domain)
    print(colored(f"[✓] Domain resolved: {domain} → {ip}", "green"))
    with open("dns_log.txt", "a") as log:
        log.write(f"{domain} → {ip}\n")
except socket.gaierror:
    print(colored(f"[✗] Failed to resolve domain: {domain}", "red"))

# Exit prompt
input(colored("\nPress Enter to exit...", "magenta"))
