    # DNS FUCKER Toolkit by lyn4x

# Auto-install dependencies if missing
try:
    import pyfiglet
    from termcolor import colored
    import dns.resolver
    import dns.query
    import dns.zone
    import whois
    import requests
except ImportError:
    import os
    print("Installing missing dependencies...")
    os.system("pip install pyfiglet termcolor dnspython python-whois requests")
    print("Dependencies installed. Please re-run the script.")
    exit()

import time
import os
import socket

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
    print(colored("0. Exit", "yellow"))

def resolve_domain():
    domain = input(colored("\nEnter domain to resolve: ", "blue"))
    try:
        ip = socket.gethostbyname(domain)
        print(colored(f"[✓] {domain} → {ip}", "green"))
        with open("dns_log.txt", "a") as log:
            log.write(f"{domain} → {ip}\n")
    except socket.gaierror:
        print(colored(f"[✗] Failed to resolve: {domain}", "red"))

def view_log():
    print(colored("\nDNS Log:", "magenta"))
    try:
        with open("dns_log.txt", "r") as log:
            print(log.read())
    except FileNotFoundError:
        print(colored("No log file found.", "red"))

def about():
    print(colored("\nTool: DNS FUCKER", "cyan"))
    print(colored("Author: lyn4x", "cyan"))
    print(colored("Version: 2.0", "cyan"))
    print(colored("Use responsibly. Designed for DNS validation, scanning, and education.", "cyan"))

def whois_lookup():
    domain = input(colored("\nEnter domain for WHOIS lookup: ", "blue"))
    try:
        info = whois.whois(domain)
        print(colored("\nWHOIS Info:", "magenta"))
        print(info)
    except Exception as e:
        print(colored(f"[✗] WHOIS lookup failed: {e}", "red"))

def subdomain_scan():
    domain = input(colored("\nEnter domain to scan for subdomains: ", "blue"))
    subdomains = ["www", "mail", "ftp", "test", "dev", "admin", "api"]
    print(colored(f"\n[•] Scanning {domain} for common subdomains...", "yellow"))
    for sub in subdomains:
        url = f"http://{sub}.{domain}"
        try:
            response = requests.get(url, timeout=2)
            print(colored(f"[✓] Found: {url} ({response.status_code})", "green"))
        except:
            pass

def dns_benchmark():
    domain = input(colored("\nEnter domain to benchmark DNS resolution: ", "blue"))
    start = time.time()
    try:
        ip = socket.gethostbyname(domain)
        end = time.time()
        duration = round((end - start) * 1000, 2)
        print(colored(f"[✓] {domain} resolved to {ip} in {duration} ms", "green"))
    except socket.gaierror:
        print(colored(f"[✗] Failed to resolve: {domain}", "red"))

def dns_vulnerability_scan():
    domain = input(colored("\nEnter domain to scan for DNS vulnerabilities: ", "blue"))
    print(colored(f"\n[•] Scanning {domain} for DNS issues...", "yellow"))

    # Zone transfer test
    try:
        ns_records = dns.resolver.resolve(domain, 'NS')
        for ns in ns_records:
            ns_ip = socket.gethostbyname(str(ns))
            try:
                zone = dns.zone.from_xfr(dns.query.xfr(ns_ip, domain))
                print(colored(f"[!] Zone transfer allowed on {ns} ({ns_ip})", "red"))
            except Exception:
                print(colored(f"[✓] Zone transfer blocked on {ns} ({ns_ip})", "green"))
    except Exception as e:
        print(colored(f"[✗] Failed to resolve NS records: {e}", "red"))

    # Wildcard DNS test
    try:
        fake = "nonexistent." + domain
        answer = dns.resolver.resolve(fake, 'A')
        if answer:
            print(colored(f"[!] Wildcard DNS detected: {fake} resolves to {answer[0]}", "red"))
    except:
        print(colored("[✓] No wildcard DNS detected", "green"))

    with open("dns_vuln_log.txt", "a") as log:
        log.write(f"Scan for {domain} completed\n")

def nmap_scan():
    target = input(colored("\nEnter IP or domain for Nmap scan: ", "blue"))
    print(colored(f"[•] Running Nmap scan on {target}...", "yellow"))
    os.system(f"nmap -Pn -sV {target}")

def masscan_scan():
    target = input(colored("\nEnter IP range for Masscan (e.g. 192.168.1.0/24): ", "blue"))
    ports = input(colored("Enter ports to scan (e.g. 80,443): ", "blue"))
    print(colored(f"[•] Running Masscan on {target} ports {ports}...", "yellow"))
    os.system(f"masscan {target} -p{ports} --rate=1000")

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
    elif choice == "0":
        print(colored("Exiting... Stay ethical, lyn4x!", "green"))
        break
    else:
        print(colored("Invalid choice. Try again.", "red"))
