import psutil
import platform
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
console = Console()
def get_cpu_model():
    try:
        with open("/proc/cpuinfo") as f:
            for line in f:
                if "model name" in line:
                    return line.split(":")[1].strip()
    except:
        return "Unknown CPU"


def show_dashboard():

    table = Table(title="System Monitoring")

    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    # CPU Status
    if cpu > 80:
        cpu_status = "[red]HIGH[/red]"
    elif cpu > 50:
        cpu_status = "[yellow]MEDIUM[/yellow]"
    else:
        cpu_status = "[green]LOW[/green]"

    # Memory Status
    if memory > 80:
        mem_status = "[red]HIGH[/red]"
    elif memory > 50:
        mem_status = "[yellow]MEDIUM[/yellow]"
    else:
        mem_status = "[green]LOW[/green]"

    # Disk Status
    if disk > 80:
        disk_status = "[red]FULL[/red]"
    elif disk > 50:
        disk_status = "[yellow]USAGE[/yellow]"
    else:
        disk_status = "[green]NORMAL[/green]"

    table.add_row("System", f"{platform.system()} {platform.release()}")
    table.add_row("Processor", get_cpu_model())
    table.add_row("CPU Usage", f"{cpu}% ({cpu_status})")
    table.add_row("Memory Usage", f"{memory}% ({mem_status})")
    table.add_row("Disk Usage", f"{disk}% ({disk_status})")
    table.add_row("Processes", str(len(psutil.pids())))

    console.print(
        Panel(
            table,
            title="SOC SYSTEM DASHBOARD",
            border_style="cyan"
        )
    )
