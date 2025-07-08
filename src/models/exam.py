from datetime import datetime

class Exam:
    """
    Clase que representa un examen académico.

    Atributos:
        exam_id (int): Identificador único del examen.
        name (str): Nombre del examen.
        semestre (str): Semestre al que pertenece el examen.
        fecha_examen (str): Fecha y hora del examen en formato (0001-01-01T00:00:00).
        instancia (str): Instancia o convocatoria del examen.
        porcentaje_pp (int): Porcentaje correspondiente a la parte práctica.
        porcentaje_pf (int): Porcentaje correspondiente a la parte final.
        porcentaje_pc (int): Porcentaje correspondiente a la parte conceptual.
        calificacion (int): Calificación obtenida en el examen.

        Nota:
        - La fecha del examen se formatea para mostrarla como (dd/mm/yyyy\nHH:MM).
    """
    def __init__(self, exam_id, name, semestre, fecha_examen, instancia,
                 porcentaje_pp, porcentaje_pf, porcentaje_pc, calificacion):
        self.exam_id = exam_id
        self.name = name
        self.semestre = semestre
        self.fecha_examen = datetime.strptime(fecha_examen[:16], "%Y-%m-%dT%H:%M").strftime("%d/%m/%Y\n%H:%M")
        self.instancia = instancia
        self.porcentaje_pp = porcentaje_pp
        self.porcentaje_pf = porcentaje_pf
        self.porcentaje_pc = porcentaje_pc
        self.calificacion = calificacion