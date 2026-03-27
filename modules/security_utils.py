import random
import secrets
import string
import psutil
import time
from rich.table import Table
from rich.console import Console
console = Console()

def generate_password():
    console.print("\n[bold cyan]PASSWORD GENERATOR[/bold cyan]\n")

    try:
        length = input("Enter password length (default 16): ").strip()
        length = int(length) if length else 16

        if length < 6:
            console.print("[red]Password too short! Minimum 6[/red]")
            return

        chars = string.ascii_letters + string.digits + string.punctuation
        password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
        ]

        password += [random.choice(chars) for _ in range(length - 4)]
        random.shuffle(password)
        password = ''.join(password)

        # Strength check
        strength = "LOW"
        color = "red"

        if length >= 12:
            strength = "STRONG"
            color = "green"
        elif length >= 8:
            strength = "MEDIUM"
            color = "yellow"

        # Count character types
        upper = sum(1 for c in password if c.isupper())
        lower = sum(1 for c in password if c.islower())
        digits = sum(1 for c in password if c.isdigit())
        symbols = sum(1 for c in password if c in string.punctuation)

        # Create table
        table = Table(title="Generated Password Details")
        table.add_column("Property", style="cyan")
        table.add_column("Value", style="magenta")

        table.add_row("Password", password)
        table.add_row("Length", str(length))
        table.add_row("Uppercase", str(upper))
        table.add_row("Lowercase", str(lower))
        table.add_row("Digits", str(digits))
        table.add_row("Symbols", str(symbols))
        table.add_row("Strength", f"[{color}]{strength}[/{color}]")

        console.print(table)

    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")


def check_processes():

    console.print("\n[bold cyan]Running Processes[/bold cyan]\n")

    table = Table(title="Top Processes")
    table.add_column("PID", style="green")
    table.add_column("CPU %", style="red")
    table.add_column("Process Name", style="yellow")
    table.add_column("Status", style="cyan")

    processes = []

    # 🔹 FIRST PASS (initialize CPU counters)
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent(None)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    # 🔹 WAIT to collect CPU usage
    time.sleep(0.5)

    # 🔹 SECOND PASS (get actual CPU values)
    for proc in psutil.process_iter():
        try:
            pid = proc.pid
            name = proc.name()
            cpu = proc.cpu_percent(None)

            processes.append({
                'pid': pid,
                'name': name,
                'cpu_percent': cpu
            })

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    # 🔹 SORT by CPU usage
    processes = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)

    # 🔹 DISPLAY TOP 10
    filtered = [p for p in processes if p['cpu_percent'] is not None and p['cpu_percent'] > 0.5]
    for p in filtered[:10]:
        cpu = p['cpu_percent']

        if cpu > 50:
            status = "[red]HIGH[/red]"
        elif cpu > 20:
            status = "[yellow]MEDIUM[/yellow]"
        else:
            status = "[green]LOW[/green]"

        table.add_row(
            str(p['pid']),
            f"{cpu:.1f}",
            p['name'],
            status
        )

    # 🔹 SAFETY CHECK
    if len(processes) == 0:
        console.print("[yellow]No processes found[/yellow]")
        return

    console.print(table)
