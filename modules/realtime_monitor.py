from rich.live import Live
from rich.table import Table
import psutil
import time

def system_monitor():
    try:
        with Live(refresh_per_second=1) as live:
            while True:
                cpu = psutil.cpu_percent()
                memory = psutil.virtual_memory().percent
                processes = len(psutil.pids())

                # Colors
                cpu_color = "green"
                mem_color = "green"

                if cpu > 70:
                    cpu_color = "red"
                elif cpu > 40:
                    cpu_color = "yellow"

                if memory > 70:
                    mem_color = "red"
                elif memory > 40:
                    mem_color = "yellow"

                # Create table (UI)
                table = Table(title="SYSTEM MONITOR (LIVE)")
                table.add_column("Metric", style="cyan")
                table.add_column("Value", style="magenta")

                table.add_row("CPU Usage", f"[{cpu_color}]{cpu}%[/{cpu_color}]")
                table.add_row("Memory Usage", f"[{mem_color}]{memory}%[/{mem_color}]")
                table.add_row("Processes", f"[cyan]{processes}[/cyan]")

                if cpu > 80 or memory > 80:
                    table.add_row("Alert", "[bold red]High Resource Usage![/bold red]")

                live.update(table)
                time.sleep(1)

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
