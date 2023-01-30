from flask import Flask

app = Flask(__name__)

# Declaración que hace referencia a todas las rutas defindias dentro de routes.py
from app_registro.routes import * 