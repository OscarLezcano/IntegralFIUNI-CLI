class Subject:
    """
    Modelo que representa una materia del estudiante.
    """
    def __init__(self, nombre_materia, porcentaje_pp, porcentaje_asistencia, materia_periodo_id=None, assistence=None):
        """
        Inicializa un objeto Subject.
        Args:
            nombre_materia (str): Nombre de la materia.
            porcentaje_pp (float): Porcentaje de PP.
            porcentaje_asistencia (float): Porcentaje de asistencia.
            materia_periodo_id (str, optional): ID de la materia en el periodo.
            assistence (list, optional): Lista de asistencias asociadas.
        """
        self.nombre_materia = nombre_materia
        self.porcentaje_pp = porcentaje_pp
        self.porcentaje_asistencia = porcentaje_asistencia
        self.materia_periodo_id = materia_periodo_id
        self.assistence = assistence