import json

class FileHandler:
    """
    Una clase de utilidad para manejar operaciones con archivos JSON.
    Métodos:
        read_json(file_path: str) -> dict:
            Lee un archivo JSON desde la ruta especificada y devuelve su contenido como un diccionario.
            Args:
                file_path (str): La ruta del archivo JSON a leer.
            Returns:
                dict: El contenido del archivo JSON.
                
        write_json(file_path: str, data: dict) -> None:
            Escribe un diccionario en un archivo JSON en la ruta especificada.
            Args:
                file_path (str): La ruta del archivo JSON a escribir.
                data (dict): Los datos del diccionario a escribir en el archivo JSON.
            Returns:
                None
    """

    @staticmethod
    def read_json(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def write_json(file_path, data):
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)