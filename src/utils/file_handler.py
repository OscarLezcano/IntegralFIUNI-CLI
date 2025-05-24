import json

class FileHandler:
    """
    Una clase de utilidad para manejar operaciones con archivos JSON.
    """

    @staticmethod
    def read_json(file_path):
        """
        Lee un archivo JSON y devuelve su contenido como un diccionario.
        Args:
            file_path (str): Ruta al archivo JSON.
        Returns:
            dict: Contenido del archivo.
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def write_json(file_path, data):
        """
        Escribe un diccionario en un archivo JSON.
        Args:
            file_path (str): Ruta al archivo JSON.
            data (dict): Datos a escribir.
        """
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)