from app_registro import app
from flask import render_template, request, redirect
from datetime import date, datetime
import csv

@app.route("/")
def index():
    datos = listItems("data/movimientos.csv")
    return render_template("index.html", pageTitle = "Lista", lista = datos)

@app.route("/new", methods = ["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("new.html", pageTitle = "Nuevo registro", typeAction = "un nuevo registro", buttonAction = "Guardar", requestForm = {})
    else:
        error = validateForm(request.form)
        if not error:
            # Asigna ID
            datos = listItems("data/last_id.csv")
            if not datos:
                id = 1
            else:
                id = int(datos[0][0]) + 1
            
            # Actualiza último ID
            last_id = open("data/last_id.csv", "w")
            last_id.write(str(id))
            last_id.close()

            # Agrega nuevo registro
            mifichero = open("data/movimientos.csv", "a", newline = '') # Acceder al archivo y configurarlo para cargar un nuevo registro
            lectura = csv.writer(mifichero, delimiter = ',', quotechar = '"') # Con método de escritura se define formato para csv
            lectura.writerow([id, request.form["Fecha"], request.form["Concepto"], request.form["Cantidad"]]) # Registramos los datos recibidos desde el formulario con request.form y lo añadimos con el método writerrow
            mifichero.close()
            # Direcciona a URL de inicio (index)
            return redirect("/")
        else:
            return render_template("new.html", pageTitle = "Nuevo registro", typeAction = "un nuevo registro", buttonAction = "Guardar", msgError = error, requestForm = request.form)

@app.route("/modify/<int:id>", methods = ["GET", "POST"])
def modify(id):
    if request.method == "GET":
        registroBuscado = lookUpItem(id)
        if registroBuscado:
            return render_template("update.html", pageTitle = "Modificar registro", typeAction = "una modificación", buttonAction = "Modificar", requestForm = request.form)

@app.route("/delete/<int:id>", methods = ["GET", "POST"])
def delete(id):
    if request.method == "GET":
        registroBuscado = lookUpItem(id)
        if registroBuscado:
            return render_template("delete.html", pageTitle = "Eliminar registro", registro = registroBuscado, buttonAction = "Eliminar")
        else:
            return redirect("/")
    else:
        oldFile = listItems("data/movimientos.csv")
        newFile = oldFile

        for itemPosition, item in enumerate(newFile):
            if int(item[0]) == id:
                newFile.pop(itemPosition)
                break

        with open("data/movimientos.csv", "w") as file:
            mywriter = csv.writer(file, delimiter = ",")
            mywriter.writerows(newFile)

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
 
# Función para devolver lista de registros en fichero de datos
def listItems(ruta):
    fichero = open(ruta, "r") # Llama al archivo
    csvReader = csv.reader(fichero, delimiter = ",", quotechar = '"') # Accede a cada registro del archivo y lo formatea
    datos = [] # Array de datos vacío para cargar los registros del archivo

    for item in csvReader: # Recorrer el objeto csvReader y cargar cada registro al array
        datos.append(item)
    
    return datos

# Función para devolver registro específico en fichero de datos
def lookUpItem(id):
    datos = listItems("data/movimientos.csv")
    for item in datos:
        if int(item[0]) == id:
            return item
        else:
            return []

