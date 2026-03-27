import subprocess
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def classify_ip(ip):
    if ip.startswith("192.168") or ip.startswith("10.") or ip.startswith("172."):
        return "INTERNAL"
    elif ip in ["0.0.0.0", "::"]:
        return "SYSTEM"
    else:
        return "EXTERNAL"

def clean_address(addr):
    # Remove interface noise like %eth0
    if "%" in addr:
        addr = addr.split("%")[0]
    return addr

def format_state(state):
    if state == "ESTAB":
        return "ESTABLISHED"
    elif state == "LISTEN":
        return "LISTENING"
    return state

def net_connections():
    console.print("\n[bold cyan]NETWORK CONNECTION INVESTIGATION[/bold cyan]\n")

    try:
        result = subprocess.run(
            ["ss", "-tunap"],
            capture_output=True,
            text=True
        )

        lines = result.stdout.splitlines()

        table = Table(title="Active Network Connections")

        table.add_column("Protocol", style="cyan")
        table.add_column("Local Address", style="green")
        table.add_column("Remote Address", style="yellow")
        table.add_column("State", style="magenta")

        for line in lines[1:]:
            parts = line.split()

            if len(parts) >= 6:
                proto = parts[0]
                state = format_state(parts[1])

                local = clean_address(parts[4])
                remote = clean_address(parts[5])

                # Extract only IP (remove port)
                local_ip = local.split(":")[0]
                remote_ip = remote.split(":")[0]

                # Add classification
                local += f" ({classify_ip(local_ip)})"
                remote += f" ({classify_ip(remote_ip)})"

                table.add_row(proto, local, remote, state)

        console.print(Panel(table, border_style="blue"))

    except Exception as e:
        console.print(
            Panel(
                f"[bold red]Error reading network connections:[/bold red] {e}",
                border_style="red"
            )
        )
