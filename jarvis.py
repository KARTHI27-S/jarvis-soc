# JARVIS v2 - SOC Console Engine
from modules.system_monitor import show_dashboard
from modules.network_monitor import show_network_info
from modules.log_analyzer import check_auth_logs
from modules.threat_intel import check_ip_reputation
from modules.security_utils import generate_password, check_processes
from modules.port_scanner import port_scan
from ui.console_style import show_banner, show_alert
from modules.realtime_monitor import system_monitor
from ui.menu import show_menu
from modules.hash_tools import hash_file
from modules.report_generator import generate_report
from modules.login_detector import detect_bruteforce
from modules.incident_timeline import incident_timeline
from modules.net_connections import net_connections
from modules.suspicious_process import detect_suspicious
from modules.threat_score import threat_score
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
console = Console()

def print_banner():

    banner_text = """
[bold cyan]JARVIS SOC CONSOLE v2[/bold cyan]

Security Operations Investigation Tool

[bold yellow]Author : Karthi[/bold yellow]
"""

    console.print(
        Panel(
            Align.center(banner_text),
            border_style="bright_blue",
            title="[bold green]JARVIS SECURITY FRAMEWORK[/bold green]",
            subtitle="[bold red]SOC Analyst Toolkit[/bold red]"
        )
    )

def command_loop():
    while True:
        command =console.input("[bold green][JARVIS-SOC][/bold green] [bold cyan] >>[/bold cyan] ").strip().lower()
        menu_map = {
            "1": "dashboard",
            "2": "net-info",
            "3": "process-check",
            "4": "port-scan",
            "5": "log-check",
            "6": "hash-file",
            "7": "password-gen",
            "8": "monitor",
            "9": "test-alert",
            "10": "menu",
            "11": "ip-reputation",
            "12": "generate-report",
            "13": "detect-bruteforce",
            "14": "incident-timeline",
            "15": "net-connections",
            "16": "detect-suspicious",
            "17": "threat-score",
            "18": "exit"
        }

        if command in menu_map:
            command = menu_map[command]
        if command == "help":
            print("\nAvailable Commands:")
            print(" help            - Show this help menu")
            print(" dashboard       - Show system dashboard (coming soon)")
            print(" modules         - List security modules")
            print(" net-info        - Show network information")
            print(" log-check       - Analyze authentication logs")
            print(" hash-file       - Generate SHA256 hash of a file")
            print(" password-gen    - Generate a secure random password")
            print(" process-check   - Show top running processes")
            print(" port-scan       - Scan common ports on a target")
            print(" test-alert      - Trigger SOC alert panel")
            print(" monitor         - Start real-time SOC monitoring")
            print(" menu            - Show SOC command menu")
            print(" generate-report - Generate SOC incident report")
            print(" detect-bruteforce - Detect brute-force login attempts")
            print(" exit            - Exit JARVIS\n")

        elif command == "modules":
            print("\nSecurity Modules:")
            print(" system_monitor")
            print(" network_monitor")
            print(" log_analysis")
            print(" threat_intel")
            print(" security_utils\n")

        elif command == "dashboard":
            show_dashboard()

        elif command == "net-info":
            show_network_info()

        elif command == "log-check":
            check_auth_logs()

        elif command == "hash-file":
            hash_file()

        elif command == "password-gen":
            generate_password()

        elif command == "process-check":
            check_processes()

        elif command == "port-scan":
            port_scan()

        elif command == "test-alert":
            show_alert()

        elif command == "monitor":
            system_monitor()

        elif command == "menu":
            show_menu()

        elif command == "ip-reputation":
            check_ip_reputation()

        elif command == "generate-report":
            generate_report()

        elif command == "detect-bruteforce":
            detect_bruteforce()

        elif command == "incident-timeline":
            incident_timeline()

        elif command == "net-connections":
            net_connections()

        elif command == "detect-suspicious":
            detect_suspicious()

        elif command == "threat-score":
            threat_score()

        elif command == "exit":
            print("\nShutting down JARVIS SOC Console...\n")
            break

        else:
            print("Unknown command. Type 'help'.")


def main():
    print_banner()
    show_menu()
    command_loop()


if __name__ == "__main__":
    main()
