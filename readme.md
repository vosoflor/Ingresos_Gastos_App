# Aplicación web ingresos-gastos

Programa hecho en Python con el framework Flask

## Instalación

En su entorno de Python ejecutar el comando:
    ```
    pip install -r requirements.txt
    ```
La librería utilizada es Flask (https://flask.palletsprojects.com/en/2.2.x/quickstart/).

## Ejecución del programa

1. Comando para inicializar el servidor del programa:

    - En mac
        ```
        export FLASK_APP=main.py
        ```
    
    - En windows
        ```
        set FLASK_APP=main.py
        ```

    - Alternativa para que sea de forma automática y no tener que ejecutar el anterior comando: Crear archivo oculto .env y dentro agregar líneas:
        ```
        FLASK_APP = main.py
        FLASK_DEBUG = true
        ```

2. Comando para ejecutar el servidor:
    ```
    flask --app main run
    ```
    
    Al ejecutar el servidor aparece la ruta que en este caso sería el localhost http://127.0.0.1:5000.

3. Comando para ejecutar el servidor pero haciendo actualizaciones de código en tiempo real:
    ```
    flask --app main --debug run
    ```

4. Comando especial para lanzar el servidor en un puerto diferente. Ésto se utiliza en los casos que el puerto 5000 esté ocupado.
    ```
    flask --app main run -p 5001
    ```