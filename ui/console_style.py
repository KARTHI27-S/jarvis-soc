from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from datetime import datetime
console = Console()

def show_banner():

    banner = Text()
    banner.append("JARVIS ", style="bold cyan")
    banner.append("SECURITY OPERATIONS CONSOLE", style="bold green")

    console.print(
        Panel(
            banner,
            border_style="green"
        )
    )

def show_alert():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    alert_message = f"""
[bold red]🚨 SECURITY ALERT[/bold red]

[bold]Alert ID :[/bold] SOC-ALERT-001
[bold]Type     :[/bold] Suspicious Activity
[bold]Severity :[/bold] HIGH
[bold]Time     :[/bold] {now}
[bold]Source   :[/bold] SSH Authentication Logs
[bold]Component:[/bold] Authentication System (SSH)

Multiple indicators of compromise detected.
Immediate investigation recommended.
"""

    console.print(Panel(alert_message, border_style="red"))
