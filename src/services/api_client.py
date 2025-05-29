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

    def fetch_assistances_data(self, subject_id):
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