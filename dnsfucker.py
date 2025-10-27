# ASCII banner demo for Termux tools
import pyfiglet
from termcolor import colored
import time
import os

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
