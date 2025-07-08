from datetime import datetime

class DerechoExamen:
    """
    Clase que representa el derecho a examen de un estudiante para una materia específica.
    Atributos:
        id_examenes (int): Identificador único del examen.
        materia (str): Nombre de la materia asociada al examen.
        porcentaje_pp (int): Porcentaje de puntos parciales obtenidos.
        porcentaje_asistencia (int): Porcentaje de asistencia registrado.
        fecha_examen (str): Fecha y hora del examen, formateada como '0001-01-01T00:00:00'.
        fecha_limite_inscripcion (str): Fecha límite para inscribirse al examen, formateada como '0001-01-01T00:00:00'.
        fecha_inscripcion (str): Fecha y hora de inscripción al examen, formateada como '0001-01-01T00:00:00'.
        instancia (str): Instancia o convocatoria del examen.

        Nota:
        - La fecha de examen, fecha límite de inscripción y fecha de inscripción se formatean
          para mostrar solo la fecha o la fecha y hora según sea necesario (dd/mm/yyyy\nHH:MM) 
          o solo (dd/mm/yyyy).
        - Si la fecha es "0001-01-01T00:00:00", se guarda como "No Inscripto".
    """
    def __init__(self, id_examenes, materia, porcentaje_pp, porcentaje_asistencia, fecha_examen, fecha_limite_inscripcion, fecha_inscripcion, instancia):
        self.id_examenes = id_examenes
        self.materia = materia
        self.porcentaje_pp = porcentaje_pp
        self.porcentaje_asistencia = porcentaje_asistencia
        self.fecha_examen = self.formatear_fecha(fecha_examen, incluir_hora=True)
        self.fecha_limite_inscripcion = self.formatear_fecha(fecha_limite_inscripcion)
        self.fecha_inscripcion = self.formatear_fecha(fecha_inscripcion, incluir_hora=True)
        self.instancia = instancia

    def formatear_fecha(self, date_str, incluir_hora=False):
        """
        Formatea una cadena de fecha en el formato adecuado para mostrar.
            Si la fecha es "0001-01-01T00:00:00", retorna "No Inscripto".
            Si incluir_hora es True, retorna la fecha y hora en formato 'dd/mm/yyyy\nHH:MM'.
            Si incluir_hora es False, retorna solo la fecha en formato 'dd/mm/yyyy'.
        """
        
        if date_str == "0001-01-01T00:00:00":
            return "No Inscripto" 
        elif incluir_hora:
            return datetime.strptime(date_str[:16], "%Y-%m-%dT%H:%M").strftime("%d/%m/%Y\n%H:%M")
        else:
            return datetime.strptime(date_str[:10], "%Y-%m-%d").strftime("%d/%m/%Y")