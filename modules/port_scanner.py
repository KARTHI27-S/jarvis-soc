import socket
from rich.console import Console
from rich.table import Table

console = Console()

def port_scan():
    console.print("\n[bold cyan]PORT SCAN[/bold cyan]\n")

    target = input("Enter target IP (default 127.0.0.1): ").strip()
    if not target:
        target = "127.0.0.1"

    ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 8080]

    table = Table(title=f"Open Ports on {target}")
    table.add_column("Port", style="cyan")
    table.add_column("Service", style="green")
    table.add_column("Status", style="red")

    open_found = False

    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)

            result = sock.connect_ex((target, port))

            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "unknown"

                table.add_row(str(port), service, "[green]OPEN[/green]")
                open_found = True

            sock.close()

        except Exception:
            continue

    if open_found:
        console.print(table)
    else:
        console.print("[yellow]No open ports found[/yellow]")
