import subprocess
import psutil
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def threat_score():

    console.print("\n[bold cyan]SYSTEM THREAT ANALYSIS[/bold cyan]\n")

    # ---- INPUTS (replace these with your actual module outputs) ----
    brute_force = "HIGH"
    process = "LOW"
    network = "MEDIUM"

    # ---- SCORING SYSTEM ----
    score = 0

    # Brute Force Weight
    if brute_force == "HIGH":
        score += 50
    elif brute_force == "MEDIUM":
        score += 30
    else:
        score += 10

    # Process Weight
    if process == "HIGH":
        score += 50
    elif process == "MEDIUM":
        score += 30
    else:
        score += 10

    # Network Weight
    if network == "HIGH":
        score += 40
    elif network == "MEDIUM":
        score += 20
    else:
        score += 10

    # ---- FINAL DECISION ----
    if score >= 90:
        overall = "HIGH"
        color = "bold red"
    elif score >= 60:
        overall = "MEDIUM"
        color = "bold yellow"
    else:
        overall = "LOW"
        color = "bold green"

    # ---- DISPLAY TABLE ----
    table = Table(title="System Threat Analysis")

    table.add_column("Category", style="cyan")
    table.add_column("Threat Level", style="bold")

    table.add_row("Brute Force Attempts", f"[red]{brute_force}[/red]" if brute_force=="HIGH" else brute_force)
    table.add_row("Suspicious Processes", f"[green]{process}[/green]" if process=="LOW" else process)
    table.add_row("Network Risk", f"[yellow]{network}[/yellow]" if network=="MEDIUM" else network)

    console.print(Panel(table, border_style="yellow"))

    # ---- FINAL OUTPUT ----
    console.print(
        Panel(
            f"[{color}]OVERALL SYSTEM THREAT LEVEL : {overall}[/{color}]",
            border_style="red" if overall == "HIGH" else "yellow"
        )
    )
    if overall == "HIGH":
        recommendation = "[bold red]Immediate investigation required![/bold red]"
    elif overall == "MEDIUM":
        recommendation = "[bold yellow]Monitor system closely.[/bold yellow]"
    else:
        recommendation = "[bold green]System is stable.[/bold green]"

    console.print(Panel(recommendation))
