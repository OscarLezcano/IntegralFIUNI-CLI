# IntegralFIUNI-CLI

## Instalación en Windows

### 1. Instala Python

- Descarga e instala [Python 3.13 o superior](https://www.python.org/).
- Durante la instalación, asegúrate de marcar la opción **"Add Python to PATH"**.

### 2. Descarga el proyecto

- Descarga el repositorio como ZIP desde GitHub o clónalo usando Git:
  ```sh
  git clone https://github.com/usuario/IntegralFIUNI-CLI.git
  ```
- Descomprime el archivo ZIP (si corresponde) y abre la carpeta del proyecto en Visual Studio Code o tu editor favorito.

### 3. Instala las dependencias

- Abre una terminal en la carpeta raíz del proyecto (en VS-Code presiona "Control + Ñ") y ejecuta:
  ```sh
  pip install -r requirements.txt
  ```

### 4. Configura las variables de entorno y el PATH

- Crea un archivo llamado `.env` en la raíz del proyecto.
- Copia el contenido de `.env_example` en `.env` y completa los datos necesarios.

### 5. Agrega el programa al PATH de Windows

- Para poder ejecutar el programa desde cualquier ubicación en la terminal, agrega la carpeta del proyecto al **PATH** de Windows:
  1. Copia la ruta completa de la carpeta donde está tu archivo `integralcli.bat`.
  2. Presiona `Win + R`, escribe `sysdm.cpl` y presiona Enter.
  3. Ve a la pestaña **Opciones avanzadas** y haz clic en **Variables de entorno** (por si no lo encuentras esta en la esquina inferior derecha).
  4. En **Variables del sistema**, selecciona la variable llamada `Path` y haz clic en **Editar**.
  5. Haz clic en **Nuevo** y pega la ruta copiada.
  6. Acepta todos los cambios y cierra las ventanas.

### 6. Ejecuta el programa

- Desde la terminal, ejecuta:

  ```sh
  integralcli
  ```

---

¡Listo! El programa debería estar funcionando correctamente.  
Si tienes problemas, revisa que Python y las dependencias estén correctamente instaladas y que el