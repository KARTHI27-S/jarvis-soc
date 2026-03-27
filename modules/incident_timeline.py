import subprocess
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def incident_timeline():

    console.print("\n[bold cyan]INCIDENT TIMELINE ANALYSIS[/bold cyan]\n")

    try:

        result = subprocess.run(
            ["journalctl", "-u", "ssh", "--no-pager"],
            capture_output=True,
            text=True
        )

        logs = result.stdout.splitlines()

        events = []

        for line in logs:

            if "Failed password" in line or "Invalid user" in line:
                timestamp = " ".join(line.split()[0:3])
                events.append((timestamp, "SSH Authentication Failure"))

            elif "Accepted password" in line:
                timestamp = " ".join(line.split()[0:3])
                events.sort(key=lambda x: x[0])
                events.append((timestamp, "Successful SSH Login"))

        if not events:
            console.print(
                Panel(
                    "[bold green]No SSH events found.[/bold green]",
                    border_style="green"
                )
            )
            return

        table = Table(title="Security Event Timeline")

        table.add_column("Time", style="cyan")
        table.add_column("Event", style="yellow")

        for time, event in events[-10:]:
            table.add_row(time, event)

        console.print(Panel(table, border_style="blue"))

    except Exception as e:

        console.print(
            Panel(
                f"[bold red]Error analyzing timeline:[/bold red] {e}",
                border_style="red"
            )
        )
