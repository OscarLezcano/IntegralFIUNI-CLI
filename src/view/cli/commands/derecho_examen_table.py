from rich.table import Table
from rich.console import Console
from src.utils.file_handler import FileHandler
from src.models.derecho_examen import DerechoExamen

class DerechoExamenTable:
    def __init__(self):
        self.file_path = "mis_derechos_a_examenes.json"

    def load(self):
        data = FileHandler.read_json(self.file_path)
        return [
            DerechoExamen(
                item["examenId"],
                item["materia"],
                item["porcentajePP"],
                item["porcentajeAsistencia"],
                item["fechaExamen"],
                item["fechaLimiteInscripcionExamen"],
                item["fechaInscripcion"],
                item["instancia"]["label"]
            )
            for item in data["items"]
        ]

    def display_table(self):
        der_exams = self.load()
        table = Table()

        table.add_column("Id")
        table.add_column("Materia")
        table.add_column("Porcentaje PP", justify="center")
        table.add_column("Porcentaje Asistencia", justify="center")
        table.add_column("Fecha de examen", justify="center")
        table.add_column("Fecha limite de inscripcion", justify="center")
        table.add_column("Fecha de inscripcion", justify="center")
        table.add_column("Instancia", justify="center")

        for exam in der_exams:
            # Que genio que es chatGPT, mira un poco como uso las variables
            instancia_color = "green"
            if exam.instancia == "Invalido":
                instancia_color = "red"
            elif exam.instancia == "Recuperatorio":
                instancia_color = "yellow"

            table.add_row(
                str(exam.id_examenes),
                exam.materia,
                str(exam.porcentaje_pp),
                str(exam.porcentaje_asistencia),
                exam.fecha_examen,
                exam.fecha_limite_inscripcion,
                exam.fecha_inscripcion,
                f"[{instancia_color}]{exam.instancia}[/{instancia_color}]",
                end_section=True
            )

        console = Console()
        console.print(table)
