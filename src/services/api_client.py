import os
import requests
from dotenv import load_dotenv
from src.utils.file_handler import FileHandler

class APIClient:
    """
    Cliente para interactuar con la API de FIUNI.
    Permite obtener materias y asistencias del estudiante y guardar los datos en archivos JSON.
    """
    def __init__(self):
        """
        Inicializa el cliente de la API cargando las variables de entorno, configurando
        el token de autorización, los encabezados, la URL base y la carga útil predeterminada
        para las solicitudes a la API.
        Raises:
            ValueError: Si la variable de entorno FIUNI_TOKEN no está configurada en el archivo .env.
        """
        
        load_dotenv()
        self._token = os.getenv("FIUNI_TOKEN")
        if not self._token:
            raise ValueError("El token FIUNI_TOKEN no está configurado en el archivo .env")

        self._headers = {
            "Authorization": f"Bearer {self._token}",
            "Content-Type": "application/json"
        }
        self._base_url = "https://integral.fiuni.edu.py/api/"
        self._default_payload = {
            "page": 1,
            "pageSize": 25,
            "filters": {}
        }

    def __save_json(self, filename, response): 
        """
        Guarda el contenido JSON de una respuesta HTTP en un archivo.
        Args:
            filename (str): El nombre del archivo donde se guardará el contenido JSON.
            response (requests.Response): El objeto de respuesta HTTP que contiene los datos JSON.
        Returns:
            bool: True si el contenido JSON se guardó correctamente, False si ocurrió un error HTTP.
        Raises:
            requests.exceptions.HTTPError: Si la respuesta HTTP contiene un código de estado de error.
        """
        try:
            response.raise_for_status()
            FileHandler.write_json(filename, response.json())
            return True
        except requests.exceptions.HTTPError as e:
            #print(f"Error HTTP: {e}")
            return False

    def fetch_student_data(self):
        """
        Obtiene datos sobre todas las materias asociadas con el estudiante.
        Este método envía una solicitud POST al endpoint "studentsubjects/all-my-subjects" 
        de la API para recuperar información sobre las materias del estudiante. 
        La respuesta se guarda como un archivo JSON llamado "student.json".
        Retorna:
            bool: Indica si el archivo JSON se guardó correctamente.
        """
        
        endpoint = "studentsubjects/all-my-subjects"
        url = self._base_url + endpoint

        response = requests.post(url, headers=self._headers, json={})
        return self.__save_json("student.json", response)

    def fetch_assistance_data(self, subject_id):
        """
        Obtiene datos de asistencias para una materia específica.
        Este método envía una solicitud POST a la API para recuperar datos de asistencias
        asociados con el ID de la materia proporcionado. La respuesta se guarda como un archivo JSON.
        Args:
            subject_id (str): El ID de la materia para la cual se obtendrán los datos de asistencias.
                              No debe estar vacío.
        Returns:
            bool: Indica si el archivo JSON se guardó correctamente.
        Raises:
            ValueError: Si el `subject_id` está vacío.
        """

        if not subject_id:
            raise ValueError("El id de la materia no puede estar vacío")

        endpoint = f"assistances/{subject_id}/my"
        url = self._base_url + endpoint

        response = requests.post(url, headers=self._headers, json=self._default_payload)
        return self.__save_json("assistances.json", response)

    def fetch_homework_data(self, subject_id):
        if not subject_id:
            raise ValueError("El id de la materia no puede estar vacío")
        
        endpoint = f"MateriasPeriodo/{subject_id}/homework/my"
        url = self._base_url + endpoint

        response = requests.post(url, headers=self._headers, json=self._default_payload)
        return self.__save_json("homework.json", response)
    
    def fetch_derecho_examen_data(self):
        endpoint = "studentsubjects/mis_derechos_a_examenes"
        url = self._base_url + endpoint

        response = requests.post(url, headers=self._headers, json=self._default_payload)
        return self.__save_json("mis_derechos_a_examenes.json", response)

    def enroll_exam(self, id_exam):
        if not id_exam:
            raise ValueError("El id del examen no puede estar vacío")

        if  self.fetch_derecho_examen_data() == False:
            raise ValueError("No se pudo obtener los derechos a examenes, verifique su conexión a internet o el token de la API")
        
        exams = FileHandler.read_json("mis_derechos_a_examenes.json")

        student_id = exams.get("items", [{}])[0].get("studentId")

        if not student_id:
            raise ValueError("No se pudo obtener el ID del estudiante de los derechos a exámenes")

        endpoint = f"inscripcionexamen/inscribirme"
        url = self._base_url + endpoint

        payload = {
            "examenId": int(id_exam),
            "id" : 0,
            "perfilAlumnoId": student_id,
            "calificacon": 0
        }

        response = requests.post(url, headers=self._headers, json=payload)
        return response.status_code == 200
    
    def enroll_all_exams(self):
        if not self.fetch_derecho_examen_data():
            raise ValueError("No se pudo obtener los derechos a examenes, verifique su conexión a internet o el token de la API")
        
        exams = FileHandler.read_json("mis_derechos_a_examenes.json")
        exam_items = exams.get("items", [])
        results = []

        for exam in exam_items:
            exam_id = exam.get("examenId")
            if exam_id:
                result = self.enroll_exam(exam_id)
                results.append({"examenId": exam_id, "success": result})
        
        return results
