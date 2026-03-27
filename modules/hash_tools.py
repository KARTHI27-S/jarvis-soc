import hashlib
import os
from rich.console import Console
from rich.table import Table
import mimetypes

console = Console()

def hash_file():
    console.print("\n[bold cyan]FILE HASH ANALYSIS[/bold cyan]\n")

    file_path = input("Enter file path: ").strip()
    file_type, _ = mimetypes.guess_type(file_path)
    file_type = file_type or "Unknown"

    if not os.path.exists(file_path):
        console.print("[red]Error: File not found[/red]")
        return

    try:
        sha256 = hashlib.sha256()
        md5 = hashlib.md5()

        file_size = os.path.getsize(file_path)

        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
                md5.update(chunk)

        sha256_hash = sha256.hexdigest()
        md5_hash = md5.hexdigest()

        # ✅ Create UI table
        table = Table(title="File Hash Details")

        table.add_column("Property", style="cyan", no_wrap=True)
        table.add_column("Value", style="magenta")

        table.add_row("File", file_path)
        table.add_row("Size", f"{file_size} bytes")
        table.add_row("Type", file_type)
        table.add_row("MD5", md5_hash)
        table.add_row("SHA256", sha256_hash)

        console.print(table)
        if file_path.endswith((".exe", ".sh", ".py")):
            console.print("[red]Warning: Executable file - verify before running[/red]")

        # ✅ Simple SOC hint
        console.print("\n[yellow]Tip:[/yellow] Verify hash using VirusTotal or threat intel")

    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
