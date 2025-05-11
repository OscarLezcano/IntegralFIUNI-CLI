from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
from rich.align import Align
from rich.rule import Rule

from src.CLI.commands.subject_table import SubjectTable
from src.CLI.commands.assistance_table import AssistancesTable
from src.services.api_client import APIClient

console = Console()

def menu():
    """
    Muestra el menú principal y permite al usuario seleccionar opciones.
    """
    while True:
        console.clear()
        
        # Título centrado
        title = Text("📘 Menú Principal", justify="center", style="bold magenta")
        console.print(Panel(Align.center(title), border_style="bright_cyan"))

        console.print(Rule(style="dim"))
        
        # Opciones alineadas a la izquierda
        console.print("[bold green][1][/bold green] 📚 Mostrar tabla de materias")
        console.print("[bold green][2][/bold green] 📅 Mostrar tabla de asistencias")
        console.print("[bold green][3][/bold green] 🚪 Salir")
        
        console.print(Rule(style="dim"))

        choice = Prompt.ask("\n[bold]Seleccione una opción[/bold]", choices=["1", "2", "3"], default="3")

        if choice == "1":
            client = APIClient()
            if client.fetch_student_data():
                console.print(Panel("📚 Materias encontradas", style="bold cyan"))
                SubjectTable().display_table()
            else:
                console.print("[red]⚠️ No se encontraron materias para el estudiante.[/red]")
            console.input("\nPresione [bold]Enter[/bold] para volver al menú...")

        elif choice == "2":
            subject_id = Prompt.ask("🆔 Ingrese el ID de la materia para ver asistencias")
            client = APIClient()
            if not subject_id:
                console.print("[red]⚠️ El ID de la materia no puede estar vacío.[/red]")
                continue
            elif client.fetch_assistances_data(subject_id):
                console.print(Panel(f"📅 Asistencias para la materia con ID: {subject_id}", style="bold cyan"))
                AssistancesTable().display_table()
            else:
                console.print(f"[red]⚠️ No se encontraron asistencias para la materia con ID: {subject_id}[/red]")
            console.input("\nPresione [bold]Enter[/bold] para volver al menú...")

        elif choice == "3":
            console.print("\n[bold yellow]👋 Saliendo del programa...[/bold yellow]\n")
            break
