import subprocess
from rich.console import Console
from rich.table import Table
from collections import defaultdict
console = Console()

def check_auth_logs():
    console.print("\n[bold cyan]AUTHENTICATION LOG CHECK[/bold cyan]\n")

    logs = []

    # 🔹 STEP 1: Try auth.log
    try:
        with open("/var/log/auth.log", "r") as f:
            logs = f.readlines()

    except FileNotFoundError:
        console.print("[yellow]auth.log not found, using journalctl...[/yellow]\n")

        try:
            result = subprocess.run(
                ["journalctl", "-u", "ssh", "--since", "5 minutes ago", "--no-pager"],
                capture_output=True,
                text=True
            )
            logs = result.stdout.splitlines()

        except Exception as e:
            console.print(f"[red]Error reading logs: {e}[/red]")
            return

    # 🔹 STEP 2: Filter failed logins
    suspicious = [line for line in logs if "Failed password" in line]

    if not suspicious:
        console.print("[green]No suspicious activity found[/green]")
        return


    # 🔹 STEP 3: Create table
    table = Table(title="Suspicious Login Attempts")

    table.add_column("User", style="yellow")
    table.add_column("IP", style="red")
    table.add_column("Attempts", style="cyan")
    table.add_column("Severity", style="bold")


    # 🔹 STEP 4: Parse logs properly
    from collections import defaultdict

    attack_map = defaultdict(int)

    for line in suspicious:
        try:
            # USER
            if "invalid user" in line:
                user = line.split("invalid user")[1].split()[0]
            else:
                user = line.split("for")[1].split()[0]

            # IP
            ip = line.split("from")[1].split()[0]

            key = f"{user}@{ip}"
            attack_map[key] += 1

        except:
            continue

    if not attack_map:
        console.print("[green]No suspicious activity found in last 1 hour [/green]")
        return

    high_alert = False
    sorted_attacks = sorted(attack_map.items(), key=lambda x: x[1], reverse=True)
    for key, count in sorted_attacks:
        user, ip = key.split("@")

        if count >= 10:
            severity = "[red]HIGH[/red]"
            high_alert = True
        elif count >= 5:
            severity = "[yellow]MEDIUM[/yellow]"
        else:
            severity = "[green]LOW[/green]"

        table.add_row(user, ip, str(count), severity)


    # 🔹 STEP 5: Display
    console.print(table)
    if high_alert:
        console.print("\n[bold red]⚠️ ALERT: Possible brute-force attack detected![/bold red]")
