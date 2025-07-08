from datetime import datetime

class Exam:
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