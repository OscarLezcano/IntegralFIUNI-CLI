from rich.table import Table
from rich.console import Console
from src.utils.file_handler import FileHandler
from src.models.assistence import Assistance

class AssistancesTable:
    def __init__(self):
        self.file_path = "assistances.json"

    def load_assistances(self):
        data = FileHandler.read_json(self.file_path)
        assistances = data["assists"]
        
        student_assists = {
            item["assistanceId"]: item["present"] 
            for item in data["studentAssists"]
        }

        return [
            Assistance(assist["date"], student_assists.get(assist["id"]))
            for assist in assistances
        ]
    
    def display_table(self):
        assistances = self.load_assistances()
        table = Table()

        # Agregar encabezado
        table.add_column("Fecha", justify="center")
        table.add_column("Presente", justify="center")

        total_assistances = len(assistances)
        present_count = sum(1 for assist in assistances if assist.present == "Sí")
        absent_count = total_assistances - present_count

        for assist in assistances:
            color_asistencia = "green" if assist.present == "Sí" else "red"
            table.add_row(assist.date, 
                          f"[{color_asistencia}]{assist.present}[/{color_asistencia}]")

        table.add_section()  # Agregar una sección para separar estadísticas

        table.add_row("Total de Asistencias", str(total_assistances))
        table.add_row("Cantidad de Presentes", f"[green]{present_count}[/green]")
        table.add_row("Cantidad de Ausentes", f"[red]{absent_count}[/red]")

        console = Console()
        console.print(table)
