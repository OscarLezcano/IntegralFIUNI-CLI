from src.CLI.commands.subject_table import SubjectTable
from src.CLI.commands.assistance_table import AssistancesTable
from src.services.api_client import APIClient

def menu():
    """
    Muestra el menú principal y permite al usuario seleccionar opciones.
    """
    while True:
        print("\n--- Menú Principal ---")
        print("1. Mostrar tabla de materias")
        print("2. Mostrar tabla de asistencias")
        print("3. Salir")
        
        choice = input("Seleccione una opción: ")
        
        if choice == "1":
            client = APIClient()
            if client.fetch_student_data():
                SubjectTable().display_table()
            else:
                print("No se encontraron materias para el estudiante.")
                
        elif choice == "2":
            subject_id = input("Ingrese el ID de la materia para ver asistencias: ")
            client = APIClient()
            if client.fetch_assistances_data(subject_id):
                AssistancesTable().display_table()
            else:
                print("No se encontraron asistencias para la materia con ID:", subject_id)
                
        elif choice == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
