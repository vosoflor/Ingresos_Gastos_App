from app_registro import app
from flask import render_template, request, redirect
from datetime import date, datetime
import csv
from config import *
from models import *

@app.route("/")
def index():
    datos = select_all(ITEMS_DATABASE)
    return render_template("index.html", pageTitle = "Lista", lista = datos)

@app.route("/new", methods = ["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("new.html", urlForm = "/new", pageTitle = "Nuevo registro", typeAction = "un nuevo registro", buttonAction = "Guardar", requestForm = {})
    else:
        error = validateForm(request.form)
        if not error:
            insert(request.form)
            return redirect("/") # Direcciona a URL de inicio (index)
        else:
            return render_template("new.html", urlForm = "/new", pageTitle = "Nuevo registro", typeAction = "un nuevo registro", buttonAction = "Guardar", msgError = error, requestForm = request.form)

@app.route("/modify/<int:id>", methods = ["GET", "POST"])
def modify(id):
    if request.method == "GET":
        registroBuscado = select_by(id)
        if registroBuscado:
            return render_template("update.html", urlForm = f"/modify/{id}", pageTitle = "Modificar registro", typeAction = "una modificación", buttonAction = "Modificar", requestForm = registroBuscado)
        else:
            return redirect("/")
    else:
        error = validateForm(request.form)
        if not error:
            update_by(id, request.form)  
            return redirect("/") # Direcciona a URL de inicio (index)
        else:
            return render_template("update.html", urlForm = f"/modify/{id}", pageTitle = "Modificar registro", typeAction = "una modificación", buttonAction = "Modificar", msgError = error, requestForm = request.form)      

@app.route("/delete/<int:id>", methods = ["GET", "POST"])
def delete(id):
    if request.method == "GET":
        registroBuscado = select_by(id)
        if registroBuscado:
            return render_template("delete.html", pageTitle = "Eliminar registro", requestForm = registroBuscado)
        else:
            return redirect("/")
    else:
        delete_by(id)
        return redirect("/")

# Función para hacer validación de datos del formulario
def validateForm(requestForm):
    error = []
    requestDate = datetime.strptime(requestForm["Fecha"], '%Y-%m-%d').date()
    if requestForm["Fecha"] == "" or requestDate > date.today():
        error.append("Fecha inválida: La fecha introducida es en el futuro o está vacía")
    if requestForm["Concepto"] == "":
        error.append("Concepto vacío: Introduce una descripción")
    if requestForm["Cantidad"] == "" or float(requestForm["Cantidad"]) == 0.0:
        error.append("Cantidad vacío o cero: Debes introducir un monto válido")
    return error