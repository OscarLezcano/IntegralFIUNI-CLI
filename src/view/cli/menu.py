from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
from rich.align import Align
from rich.rule import Rule

from src.view.cli.commands.subject_table import SubjectTable
from src.view.cli.commands.assistance_table import AssistancesTable
from src.view.cli.commands.homework_table import HomeworkTable
from src.view.cli.commands.exam_table import ExamTable
from src.services.api_client import APIClient
from src.view.cli.commands.derecho_examen_table import DerechoExamenTable

console = Console()
client = APIClient()

def show_subjects():
    console.print(Panel("🔄 Cargando...", style="bold yellow"))
    if client.fetch_student_data():
        console.print(Panel("📚 Materias encontradas", style="bold cyan"))
        SubjectTable().display_table()
    else:
        console.print("[red]⚠️ No se encontraron materias para el estudiante.[/red]")
    console.input("\nPresione [bold]Enter[/bold] para volver al menú...")

def show_assistance():
    subject_id = Prompt.ask("🆔 Ingrese el ID de la materia para ver asistencias")
    console.print(Panel("🔄 Cargando...", style="bold yellow"))
    if not subject_id:
        console.print("[red]⚠️ El ID de la materia no puede estar vacío.[/red]")
        return
    elif client.fetch_assistance_data(subject_id):
        console.print(Panel(f"📅 Asistencias para la materia con ID: {subject_id}", style="bold cyan"))
        AssistancesTable().display_table()
    else:
        console.print(f"[red]⚠️ No se encontraron asistencias para la materia con ID: {subject_id}[/red]")
    console.input("\nPresione [bold]Enter[/bold] para volver al menú...")

def show_homework():
    subject_id = Prompt.ask("🆔 Ingrese el ID de la materia para ver tareas")
    console.print(Panel("🔄 Cargando...", style="bold yellow"))
    if not subject_id:
        console.print("[red]⚠️ El ID de la materia no puede estar vacío.[/red]")
        return
    elif client.fetch_homework_data(subject_id):
        console.print(Panel(f"📝 Tareas para la materia con ID: {subject_id}", style="bold cyan"))
        HomeworkTable().display_table()
    else:
        console.print(f"[red]⚠️ No se encontraron tareas para la materia con ID: {subject_id}[/red]")
    console.input("\nPresione [bold]Enter[/bold] para volver al menú...")

def show_exams():
    console.print(Panel("🔄 Cargando...", style="bold yellow"))
    if client.fetch_exam_data():
        console.print(Panel("📅 Exámenes encontrados", style="bold cyan"))
        ExamTable().display_table()
    else:
        console.print("[red]⚠️ No se encontraron exámenes para el estudiante.[/red]")
    console.input("\nPresione [bold]Enter[/bold] para volver al menú...")

def show_derecho_examen():
    console.print(Panel("🔄 Cargando...", style="bold yellow"))
    if client.fetch_derecho_examen_data():
        console.print(Panel("📘 Derechos a Exámenes encontrados", style="bold cyan"))
        DerechoExamenTable().display_table()
    else:
        console.print("[red]⚠️ No se encontraron derechos a exámenes para el estudiante.[/red]")
    console.input("\nPresione [bold]Enter[/bold] para volver al menú...")

def enroll_exam():
    console.print(Panel("🔄 Cargando...", style="bold yellow"))
    exam_id = Prompt.ask("🆔 Ingrese el ID del examen que desea inscribir")
    if not exam_id:
        console.print("[red]⚠️ El ID del examen no puede estar vacío.[/red]")
    elif client.enroll_exam(exam_id):
        console.print(f"[green]✅ Inscripción exitosa al examen con ID: {exam_id}[/green]")
    else:
        console.print(f"[red]⚠️ Error al inscribir al examen con ID: {exam_id}[/red]")
    console.input("\nPresione [bold]Enter[/bold] para volver al menú...")

def enroll_all_exams():
    console.print(Panel("🔄 Cargando...", style="bold yellow"))
    exams = client.enroll_all_exams()
    console.print("[green]\nSe te ha inscripto a los siguientes examenes:[/green]")
    for exam in exams:
        if exam['success']:
            console.print(f"[yellow]\t*{exam['materia']}[/yellow]")
    console.input("\nPresione [bold]Enter[/bold] para volver al menú...")


def exit_program():
    console.print("\n[bold yellow]👋 Saliendo del programa...[/bold yellow]\n")
    return True

menu_options = {
    "1": ("📚 Mostrar tabla de materias", show_subjects),
    "2": ("📅 Mostrar tabla de asistencias", show_assistance),
    "3": ("📝 Mostrar tabla de tareas", show_homework),
    "4": ("📤 Mostrar tabla de exámenes", show_exams),
    "5": ("📘 Mostrar derechos a exámenes", show_derecho_examen),
    "6": ("☑️ Inscribirte a un examen", enroll_exam),
    "7": ("☑️ Inscribirte a todos los exámenes disponibles", enroll_all_exams),
    "8": ("🚪 Salir", exit_program)
}

def menu():
    while True:
        console.clear()
        title = Text("BIENVENIDO A INTEGRAL CLI", justify="center", style="bold magenta")
        console.print(Panel(Align.center(title), border_style="bright_cyan"))
        console.print(Rule(style="dim"))

        salir = None
        for nro, (desc, _) in menu_options.items():
            console.print(f"[bold green][{nro}][/bold green] {desc}")
            salir = nro

        console.print(Rule(style="dim"))
        choice = Prompt.ask("\n[bold]Seleccione una opción[/bold]", choices=list(menu_options.keys()), default=salir)

        _, action = menu_options[choice]
        should_exit = action()
        if should_exit:
            break