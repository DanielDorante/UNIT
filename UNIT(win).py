import os
import platform
import socket
import sys
import time

try:
    import requests
except ImportError:
    requests = None

try:
    import whois
except ImportError:
    whois = None

FAVORITES_FILE = "unit_favorites.txt"

ascii_art = r"""
 _    _ _   _ _____ 
| |  | | \ | |  _  |
| |  | |  \| | | | |
| |  | | . ` | | | |
| |__| | |\  | |/ / 
 \____/ \_| \_/___/  
User Network Interface Tool
"""

def get_commands():
    if platform.system() == "Windows":
        return {
            "ping": "ping 8.8.8.8",
            "traceroute": "tracert 8.8.8.8",
            "ipconfig": "ipconfig",
            "custom_ping": "ping {ip} -n {count}"
        }
    else:
        return {
            "ping": "ping -c 4 8.8.8.8",
            "traceroute": "traceroute 8.8.8.8",
            "ipconfig": "ifconfig",
            "custom_ping": "ping -c {count} {ip}"
        }

commands = get_commands()

def ping():
    os.system(commands["ping"])

def traceroute():
    os.system(commands["traceroute"])

def ip_config():
    os.system(commands["ipconfig"])

def custom_ping():
    ip = input("Enter IP or hostname to ping: ")
    count = input("How many packets? ")
    if not count.isdigit():
        print("Invalid packet count! Using default: 4")
        count = "4"
    os.system(commands["custom_ping"].format(ip=ip, count=count))

def dns_lookup():
    domain = input("Enter domain (e.g. example.com): ")
    try:
        ip = socket.gethostbyname(domain)
        print(f"{domain} resolves to {ip}")
    except Exception as e:
        print("DNS lookup failed:", e)

def reverse_dns():
    ip = input("Enter IP address: ")
    try:
        host = socket.gethostbyaddr(ip)[0]
        print(f"{ip} resolves to {host}")
    except Exception as e:
        print("Reverse lookup failed:", e)

def whois_lookup():
    if whois is None:
        print("python-whois not installed! Try: pip install python-whois")
        return
    domain = input("Enter domain for WHOIS: ")
    try:
        w = whois.whois(domain)
        print(w)
    except Exception as e:
        print("WHOIS lookup failed:", e)

def get_public_ip():
    if requests is None:
        print("requests module not installed! Try: pip install requests")
        return
    try:
        ip = requests.get('https://api.ipify.org').text
        print("Your public IP address is:", ip)
    except Exception as e:
        print("Could not retrieve public IP:", e)

def port_scanner():
    target = input("Enter host to scan (IP or domain): ")
    ports = input("Enter ports to scan (e.g. 20-25 or 80,443): ")
    port_list = []
    if '-' in ports:
        start, end = [int(x) for x in ports.split('-')]
        port_list = list(range(start, end + 1))
    else:
        port_list = [int(p) for p in ports.split(',') if p.isdigit()]
    print(f"Scanning {target}...")
    for port in port_list:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            try:
                result = s.connect_ex((target, port))
                if result == 0:
                    print(f"Port {port}: OPEN")
            except Exception:
                pass
    print("Scan complete.")

def save_favorite():
    host = input("Enter IP or domain to save as favorite: ")
    try:
        with open(FAVORITES_FILE, "a") as f:
            f.write(host + "\n")
        print(f"Saved {host} to favorites.")
    except Exception as e:
        print("Could not save favorite:", e)

def show_favorites():
    try:
        with open(FAVORITES_FILE, "r") as f:
            favorites = f.readlines()
        if not favorites:
            print("No favorites saved yet.")
        else:
            print("Favorites:")
            for i, host in enumerate(favorites, 1):
                print(f"  [{i}] {host.strip()}")
    except FileNotFoundError:
        print("No favorites saved yet.")

def system_info():
    print("OS:", platform.system(), platform.release())
    print("Node:", platform.node())
    print("Machine:", platform.machine())
    print("Processor:", platform.processor())
    print("Python Version:", platform.python_version())

def uptime():
    if platform.system() == "Windows":
        os.system("net stats workstation | find \"Statistics since\"")
    else:
        os.system("uptime")

def exit_program():
    print("Goodbye, happy networking!")
    sys.exit(0)

def get_command_map():
    """
    Hash map for storing user inputs to actual command functions.
    This implements a switch-state pattern for cleaner command dispatch.
    """
    return {
        "1": ping,
        "2": traceroute,
        "3": ip_config,
        "4": custom_ping,
        "5": dns_lookup,
        "6": reverse_dns,
        "7": whois_lookup,
        "8": get_public_ip,
        "9": port_scanner,
        "10": save_favorite,
        "11": show_favorites,
        "12": system_info,
        "13": uptime,
        "14": exit_program
    }

def menu():
    print("""
[1] Ping the Internet
[2] Trace Internet Route
[3] Network Adapter Details
[4] Customized Ping
[5] DNS Lookup (Forward)
[6] Reverse DNS Lookup
[7] WHOIS Lookup
[8] Get Public IP Address
[9] Port Scanner
[10] Save Favorite Host/IP
[11] Show Favorites
[12] System Info
[13] Uptime
[14] Exit/Quit
    """)

def main():
    print(ascii_art)
    command_map = get_command_map()
    
    while True:
        menu()
        choice = input("Select an option: ").strip()
        
        # Use hash map lookup instead of if-elif chain (switch state pattern)
        command_func = command_map.get(choice)
        
        if command_func:
            command_func()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
