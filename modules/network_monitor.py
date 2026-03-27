import psutil
import socket

def show_network_info():
    from rich.panel import Panel
    from rich.console import Console
    from rich.align import Align


    console = Console()

    # Host info
    hostname = socket.gethostname()
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
    except:
        local_ip = "Unavailable"

    # Interfaces
    interfaces = psutil.net_if_addrs()
    interface_list = "\n".join([f"- {i}" for i in interfaces])

    # ALL active connections (no limit)
    connections = psutil.net_connections(kind='inet')
    connection_list = []
    for conn in connections:
        if conn.laddr:
            try:
                ip = conn.laddr.ip
                port = conn.laddr.port
                proto = "TCP" if conn.type == socket.SOCK_STREAM else "UDP"
                pid = conn.pid
                try:
                    process = psutil.Process(pid).name() if pid else "Unknown"
                except:
                    process = "Unknown"
                status = conn.status if conn.status != "NONE" else "UNKNOWN"
                if conn.type == socket.SOCK_DGRAM:
                    status = "[cyan]ACTIVE[/cyan]"
                elif conn.status == "ESTABLISHED":
                    status = "[green]ESTABLISHED[/green]"
                elif conn.status == "LISTEN":
                    status = "[yellow]LISTEN[/yellow]"
                else:
                    status = "[red]{conn.status}[/red]"
                if conn.raddr:
                    remote_ip = conn.raddr.ip
                    remote_port = conn.raddr.port
                else:
                    remote_ip = "0.0.0.0"
                    remote_port = "-"
                connection_list.append(f"{ip}:{port} -> {remote_ip}:{remote_port}" f"({proto}, {status}, PID:{pid}, {process})")
            except Exception as e:
                print(f"Error: {e}")

    connection_output = "\n".join(connection_list) if connection_list else "No active connections"

    # Final UI
    content = f"""Hostname : {hostname}
Local IP : {local_ip}

Network Interfaces:
{interface_list}

Active Connections:
{connection_output}"""

    console.print(
        Panel(
            Align.left(content),
            title=" NETWORK INFORMATION ",
            border_style="cyan",
            padding=(1, 4)
        )
    )
