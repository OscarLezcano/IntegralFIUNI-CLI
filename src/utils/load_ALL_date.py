# NO VEAN ESTA LOCURA
# Este código es una locura y no debería ser utilizado en producción.




# from src.utils.file_handler import FileHandler
# from src.models.subject import Subject
# from src.models.assistence import Assistance
# from src.services.api_client import APIClient
# import os  # Importar para verificar la existencia del archivo

# def load_subject_aux():
#     data = FileHandler.read_json("student.json")
#     return [
#         Subject(
#             item["materiaPeriodoId"],
#             item["nombreMateria"],
#             item["porcentajePP"],
#             item["porcentajeAsistencia"],
#             None
#         )
#         for item in data["items"]
#     ]

# def load_subject():
#     client = APIClient()
#     subject_list = load_subject_aux()  
#     for subject in subject_list:
#         client.fetch_assistances_data(subject.materiaPeriodoId)
        
#         if not os.path.exists("assistances.json"):
#             print(f"Error: El archivo 'assistances.json' no se generó para la materia {subject.nombre_materia}")
#             continue

#         date = FileHandler.read_json("assistances.json")
        
#         assistance = []
#         for item in date["assists"]:
#             student_assist = next(
#                 (sa for sa in date["studentAssists"] if sa["assistanceId"] == item["id"]), 
#                 None
#             )
#             if student_assist:
#                 assistance.append(
#                     Assistance(
#                         item["date"],
#                         student_assist["present"]
#                     )
#                 )
#         subject.assistance = assistance

#     return subject_list

# date_list = load_subject()
# for subject in date_list:
#     print(subject.nombre_materia)
#     for assist in subject.assistance:
#         print(f"Fecha: {assist.date}, Asistencia: {assist.present}")