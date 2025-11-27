from rich.table import Table
from rich.console import Console
from src.utils.file_handler import FileHandler
from src.models.exam import Exam

class ExamTable:
    def __init__(self):
        self.file_path = ".exams.json"

    def load(self):
        data = FileHandler.read_json(self.file_path)
        return [
            Exam(
                item["examenId"],
                item["materia"],
                item["semestre"],
                item["fechaExamen"],
                item["instancia"]["label"],
                item["porcentajePP"],
                item["porcentajePF"],
                item["porcentajePC"],
                item["calificacion"]
            )
            for item in data["items"]
        ]
    
    def display_table(self):
        exams = self.load()[::-1]
        table = Table()
        table.add_column("ID", justify="center")
        table.add_column("Materia", justify="center")
        table.add_column("Semestre", justify="center")
        table.add_column("Fecha Examen", justify="center", style="green")
        table.add_column("Instancia", justify="center")
        table.add_column("PP (%)", justify="center")
        table.add_column("PF (%)", justify="center")
        table.add_column("PC (%)", justify="center")
        table.add_column("Calificación", justify="center", style="bold")

        color_calificacion = {
            5: "green",
            4: "blue",
            3: "cyan",
            2: "yellow",
            1: "red",
            0: "white"
        }

        for exam in exams:
            calificacion_color = color_calificacion[exam.calificacion]
            
            table.add_row(
                str(exam.exam_id),
                exam.name,
                str(exam.semestre),
                exam.fecha_examen,
                exam.instancia,
                f"{int(exam.porcentaje_pp)}%",
                f"{int(exam.porcentaje_pf)}%",
                f"{int(exam.porcentaje_pc)}%",
                f"[{calificacion_color}]{exam.calificacion}[/{calificacion_color}]",
                end_section=True
            )

        console = Console()
        console.print(table)