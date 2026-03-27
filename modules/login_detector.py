import subprocess
import re
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def detect_bruteforce():
    console.print("\n[bold cyan]BRUTE FORCE DETECTION[/bold cyan]\n")

    try:
        # Fetch SSH logs (last 5 minutes)
        result = subprocess.run(
            ["journalctl", "-u", "ssh", "--since", "5 minutes ago", "--no-pager"],
            capture_output=True,
            text=True
        )

        logs = result.stdout.splitlines()

        failed_attempts = {}

        for line in logs[:20]:
            print(line)
            if "Failed password" in line:

                parts = line.split()

                try:
                    if "invalid" in parts:
                        user = parts[parts.index("user") + 1]
                    else:
                        user = parts[parts.index("for") + 1]

                    ip = parts[parts.index("from") + 1]

                    if ip == "::1":
                        ip = "127.0.0.1 (localhost)"

                except Exception:
                    user = "unknown"
                    ip = "unknown"

                key = (user, ip)
                failed_attempts[key] = failed_attempts.get(key, 0) + 1

        # No attacks found
        if not failed_attempts:
            console.print(
                Panel(
                    "[bold green]No brute-force activity detected.[/bold green]",
                    title="Security Status",
                    border_style="green"
                )
            )
            return

        # Create table
        table = Table(title="Suspicious Login Attempts")

        table.add_column("User", style="cyan")
        table.add_column("IP Address", style="magenta")
        table.add_column("Attempts", style="red")
        table.add_column("Severity", style="bold yellow")

        for (user, ip), count in failed_attempts.items():
            risk = "HIGH" if count >= 5 else "LOW"
            table.add_row(user, ip, str(count), risk)

        console.print(Panel(table, border_style="red"))

        console.print("\n[bold yellow]Tip: Monitor SSH logs continuously for better detection[/bold yellow]\n")

    except Exception as e:
        console.print(
            Panel(
                f"[bold red]Error reading authentication logs:[/bold red] {e}",
                border_style="red"
            )
        )
