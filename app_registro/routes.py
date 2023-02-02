from app_registro import app
from flask import render_template, request, redirect
from datetime import date, datetime
import csv

@app.route("/")
def index():
    fichero = open("data/movimientos.csv", "r") # Llama al archivo
    csvReader = csv.reader(fichero, delimiter = ",", quotechar = '"') # Accede a cada registro del archivo y lo formatea
    datos = [] # Array de datos vacío para cargar los registros del archivo

    for item in csvReader: # Recorrer el objeto csvReader y cargar cada registro al array
        datos.append(item)

    return render_template("index.html", pageTitle = "Lista", lista = datos)

@app.route("/new", methods = ["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("new.html", pageTitle = "Nuevo registro", typeAction = "un nuevo registro", buttonAction = "Guardar")
    else:
        dateForm = datetime.strptime(request.form["Fecha"], '%Y-%m-%d').date()
        if(dateForm <= date.today()):
            mifichero = open("data/movimientos.csv", "a", newline = '') # Acceder al archivo y configurarlo para cargar un nuevo registro
            lectura = csv.writer(mifichero, delimiter = ',', quotechar = '"') # Con método de escritura se define formato para csv
            lectura.writerow([request.form["Fecha"], request.form["Concepto"], request.form["Cantidad"]]) # Registramos los datos recibidos desde el formulario con request.form y lo añadimos con el método writerrow
            mifichero.close()
            return redirect("/")
        else:
            return redirect("/new")

@app.route("/modify")
def modify():
    return render_template("update.html", pageTitle = "Modificar registro", typeAction = "una modificación", buttonAction = "Modificar")

@app.route("/delete")
def delete():
    return render_template("delete.html", pageTitle = "Eliminar registro")