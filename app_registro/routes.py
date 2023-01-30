from app_registro import app
from flask import render_template

@app.route("/")
def index():
   
   # Prueba de diccionario a vista html
    datos = [{ 'Fecha' : '18/12/2022', 'Concepto' : 'Regalo de reyes', 'Cantidad' : -275.50},
            { 'Fecha' : '19/12/2022', 'Concepto' : 'Cobro de trabajo', 'Cantidad' : 1200.00},
            { 'Fecha' : '18/12/2022', 'Concepto' : 'Ropa de navidad', 'Cantidad' : -355.50},]

    return render_template("index.html", pageTitle = "Lista", lista = datos)

@app.route("/new")
def create():
    return render_template("new.html", pageTitle = "Nuevo registro")

@app.route("/modify")
def modify():
    return render_template("update.html", pageTitle = "Modificar registro")

@app.route("/delete")
def delete():
    return render_template("delete.html", pageTitle = "Eliminar registro")