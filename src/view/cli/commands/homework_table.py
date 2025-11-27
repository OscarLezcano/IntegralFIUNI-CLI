from rich.table import Table
from rich.console import Console
from src.utils.file_handler import FileHandler
from src.models.homework import Homework

class HomeworkTable:
    """
    Clase para mostrar la tabla de tareas en la consola.
    """

    def __init__(self, file_path=".homework.json"):
        """
        Inicializa la clase con la ruta al archivo JSON de tareas.
        Args:
            file_path (str): Ruta al archivo JSON de tareas.
        """
        self.file_path = file_path

    def load(self):
        """
        Carga los datos de tareas desde el archivo JSON y los convierte en objetos Homework.
        Returns:
            list[Homework]: Lista de objetos Homework.
        """
        data = FileHandler.read_json(self.file_path)
        return [
            Homework(
                item["tarea"],
                item["tipoTarea"]["label"],
                item["puntajeObtenido"],
                item["puntajeTotal"],
                item["porcentajePesoMateria"]
            )
            for item in data["items"]
        ]

    def display_table(self):
        """
        Muestra la tabla de tareas en la consola.
        """
        homeworks = self.load()
        table = Table()

        table.add_column("Nombre")
        table.add_column("Tipo", justify="center")
        table.add_column("Puntaje Obtenido", justify="center")
        table.add_column("Puntaje Total", justify="center")
        table.add_column("Peso (%)", justify="center")

        for hw in homeworks:
            table.add_row(
                hw.nombre,
                hw.tipo,
                str(hw.puntaje_obtenido),
                str(hw.puntaje_total),
                f"{int(hw.peso)}%"
            )

        console = Console()
        console.print(table)
