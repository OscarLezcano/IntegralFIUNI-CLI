from datetime import datetime

class DerechoExamen:
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
        if date_str == "0001-01-01T00:00:00":
            return "No Inscripto" 
        elif incluir_hora:
            return datetime.strptime(date_str[:16], "%Y-%m-%dT%H:%M").strftime("%d/%m/%Y\n%H:%M")
        else:
            return datetime.strptime(date_str[:10], "%Y-%m-%d").strftime("%d/%m/%Y")