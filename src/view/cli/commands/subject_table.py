from rich.table import Table
from rich.console import Console
from src.utils.file_handler import FileHandler
from src.models.subject import Subject

class SubjectTable:
    """
    Clase para mostrar la tabla de materias del estudiante en la consola.
    Utiliza Rich para el formateo de la tabla.
    """

    def __init__(self):
        """
        Inicializa la clase con la ruta al archivo JSON de materias.
        """
        self.file_path = "student.json"

    def load(self):
        """
        Carga los datos de materias desde el archivo JSON y los convierte en objetos Subject.
        Returns:
            list[Subject]: Lista de objetos Subject.
        """
        data = FileHandler.read_json(self.file_path)
        return [
            Subject(
                item["nombreMateria"],
                item["porcentajePP"],
                item["porcentajeAsistencia"],
                item["materiaPeriodoId"]
            )
            for item in data["items"]
        ]

    def display_table(self):
        """
        Muestra la tabla de materias en la consola con colores según el porcentaje de asistencia.
        """
        students = self.load()
        table = Table()

        # Agregar encabezados
        table.add_column("Id", justify="center")
        table.add_column("Materia", justify="center")
        table.add_column("Porcentaje PP", justify="center")
        table.add_column("Porcentaje Asistencia", justify="center")

        for student in students:
            # Que genio que es chatGPT, mira un poco como uso las variables
            asistencia_color = "green"
            if student.porcentaje_asistencia < 70:
                asistencia_color = "red"
            elif 70 <= student.porcentaje_asistencia < 80:
                asistencia_color = "yellow"

            table.add_row (
                str(student.materia_periodo_id),
                student.nombre_materia,
                str(student.porcentaje_pp),
                f"[{asistencia_color}]{student.porcentaje_asistencia}[/{asistencia_color}]",
                end_section=True
            )

        console = Console()
        console.print(table)