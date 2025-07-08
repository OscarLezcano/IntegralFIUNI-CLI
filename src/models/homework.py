class Homework:
    """
    Modelo que representa una tarea o trabajo práctico.
    """
    def __init__(self, nombre, tipo, puntaje_obtenido, puntaje_total, peso):
        """
        Inicializa un objeto Homework.
        Args:
            nombre (str): Nombre de la tarea.
            tipo (str): Tipo de tarea (por ejemplo, examen, TP, etc).
            puntaje_obtenido (int): Puntaje obtenido.
            puntaje_total (int): Puntaje total posible.
            peso (int): Peso de la tarea en porcentaje.
        """
        self.nombre = nombre
        self.tipo = tipo
        self.puntaje_obtenido = puntaje_obtenido
        self.puntaje_total = puntaje_total
        self.peso = peso

