from rich.console import Console
from rich.panel import Panel
import ipaddress

console = Console()

# Known IPs
KNOWN_SAFE = [
    "8.8.8.8",
    "1.1.1.1"
]

KNOWN_SUSPICIOUS = [
    "192.168.1.200",
    "10.10.10.10"
]


def check_ip_reputation():
    ip = input("Enter IP address > ").strip()

    # -------- STEP 1: Validate IP --------
    try:
        ip_obj = ipaddress.ip_address(ip)
    except ValueError:
        console.print("[bold red]❌ Invalid IP address[/bold red]")
        return

    # -------- STEP 2: Handle Private IPs --------
    if ip_obj.is_private:
        result = f"""
IP Address : {ip}
Status     : INTERNAL (Private Network)
Risk Level : LOW
"""
        console.print(Panel(result, title="IP REPUTATION CHECK", border_style="yellow"))
        return

    # -------- STEP 3: Reputation Check --------
    if ip in KNOWN_SAFE:
        result = f"""
IP Address : {ip}
Status     : Known Public DNS
Risk Level : LOW
"""

    elif ip in KNOWN_SUSPICIOUS:
        result = f"""
IP Address : {ip}
Status     : Suspicious IP
Risk Level : HIGH
"""

    else:
        result = f"""
IP Address : {ip}
Status     : Unknown
Risk Level : MEDIUM
"""

    # -------- STEP 4: Display --------
    console.print(Panel(result, title="IP REPUTATION CHECK", border_style="yellow"))
