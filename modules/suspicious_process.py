import psutil
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

SUSPICIOUS_NAMES = ["nc", "netcat", "nmap", "hydra", "john", "hashcat"]

def detect_suspicious():
    console.print("\n[bold cyan]SUSPICIOUS PROCESS ANALYSIS[/bold cyan]\n")

    suspicious = []

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'username']):
        try:
            name = proc.info['name'] or ""
            cpu = proc.info['cpu_percent']
            user = proc.info['username']

            # Detection rules
            SAFE_PROCESSES = [
                "systemd", "dbus", "polkit", "pipewire", "gnome",
                "xfce", "gvfs", "NetworkManager", "accounts-daemon",
                "kworker", "at-spi", "udisks", "upower",
                "rtkit", "colord", "cron", "agetty"
            ]
            if any(safe in name.lower() for safe in SAFE_PROCESSES):
                continue
            if (
                cpu > 60 or
                any(tool in name.lower() for tool in SUSPICIOUS_NAMES)
            ):
                risk = "HIGH" if cpu > 80 else "MEDIUM"

                suspicious.append((
                    str(proc.info['pid']),
                    name,
                    f"{cpu}%",
                    user,
                    risk
                ))

        except:
            continue

    if not suspicious:
        console.print(
            Panel(
                "[bold green]No suspicious processes detected.[/bold green]",
                border_style="green"
            )
        )
        return

    table = Table(title="Suspicious Processes")

    table.add_column("PID", style="cyan")
    table.add_column("Process", style="red")
    table.add_column("CPU %", style="yellow")
    table.add_column("User", style="magenta")
    table.add_column("Risk", style="bold red")

    for row in suspicious:
        table.add_row(*row)

    console.print(Panel(table, border_style="red"))
