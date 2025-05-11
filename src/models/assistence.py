from datetime import datetime

class Assistance:
    def __init__(self, date, present):
        self.date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S").strftime("%d/%m/%Y")
        self.present = "Sí" if present else "No"
