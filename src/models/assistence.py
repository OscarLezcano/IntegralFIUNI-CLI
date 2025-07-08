from datetime import datetime

class Assistance:
    """
    Modelo que representa una asistencia a clase.
    """
    def __init__(self, date, present):
        """
        Inicializa un objeto Assistance.
        Args:
            date (str): Fecha de la asistencia en formato ISO.
            present (bool): True si estuvo presente, False si estuvo ausente
        """
        self.date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S").strftime("%d/%m/%Y")
        self.present = "Sí" if present else "No"
