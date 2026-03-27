from rich.console import Console
from rich.panel import Panel

console = Console()

def show_menu():

    menu_text = """
Available Commands

1   dashboard           - System monitoring panel
2   net-info            - Show network information
3   process-check       - Investigate running processes
4   port-scan           - Scan open ports
5   log-check           - Analyze authentication logs
6   hash-file           - Generate file hash
7   password-gen        - Generate strong password
8   monitor             - Start real-time monitoring
9   test-alert          - Trigger security alert
10  menu                - Show this menu
11  ip-reputation       - Check IP threat intelligence
12  generate-report     - Generate SOC incident report
13  detect-bruteforce   - Detect brute-force login attempts
14  incident-timeline   - Reconstruct security event timeline
15  net-connections     - Investigate active network connections
16  detect-suspicious   - Detect abnormal CPU process
17  threat-score        - Calculate system threat level
18  exit                - Exit JARVIS
"""
    console.print(
        Panel(menu_text, title="JARVIS SOC COMMAND REFERENCE", border_style="cyan")
    )

