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
    
        ```export FLASK_APP=hello.py```
    
    - En windows
    
        ```set FLASK_APP=hello.py```

2. Comando para ejecutar el servidor:

    ```flask --app hello run```
    
    Al ejecutar el servidor aparece la ruta que en este caso sería el localhost http://127.0.0.1:5000.

3. Comando para ejecutar el servidor pero haciendo actualizaciones de código en tiempo real:

    ```flask --app hello --debug run```

4. Comando especial para lanzar el servidor en un puerto diferente. Ésto se utiliza en los casos que el puerto 5000 esté ocupado.

    ```flask --app hello run -p 5001```