import csv
from config import *

def select_all(ruta): # Devuelve una lista con todos los registros del fichero
    with open(ruta, "r") as file:
        csvReader = csv.reader(file, delimiter = ",", quotechar = '"') # Accede a cada registro del archivo y lo formatea
        datos = [] # Array de datos vacío para cargar los registros del archivo
        for item in csvReader: # Recorrer el objeto csvReader y cargar cada registro al array
            datos.append(item)
    return datos

def select_by(id): # Devuelve un registro con el id de la entrada o vacío si no lo encuentra
    datos = select_all(ITEMS_DATABASE)
    
    selected = []
    
    for item in datos:
        if int(item[0]) == id:
            selected = item
            break
    
    selectedDictionary = dict()
    selectedDictionary["id"] = selected[0]
    selectedDictionary["Fecha"] = selected[1]
    selectedDictionary["Concepto"] = selected[2]
    selectedDictionary["Cantidad"] = selected[3]
    
    return selectedDictionary

def delete_by(id): # Elimina el registro con el id de la entrada
    oldFile = select_all(ITEMS_DATABASE)
    newFile = oldFile

    for itemPosition, item in enumerate(newFile):
        if int(item[0]) == id:
            newFile.pop(itemPosition)
            break

    with open(ITEMS_DATABASE, "w") as file:
        mywriter = csv.writer(file, delimiter = ",")
        mywriter.writerows(newFile)

def insert(requestForm): # Crea un nuevo registro cuando cumple con las condiciones del formulario y asigna un id único
    # Asigna ID
    datos = select_all(LAST_ID_DATABASE) 
    if not datos:
        id = 1
    else:
        id = int(datos[0][0]) + 1
    # Actualiza último ID
    with open(LAST_ID_DATABASE, "w") as file: 
        file.write(str(id))
    # Agrega nuevo registro
    with open(ITEMS_DATABASE, "a", newline = '') as file: # Acceder al archivo y configurarlo para cargar un nuevo registro
        mywriter = csv.writer(file, delimiter = ',', quotechar = '"') # Con método de escritura se define formato para csv
        mywriter.writerow([id, requestForm["Fecha"], requestForm["Concepto"], requestForm["Cantidad"]]) # Registramos los datos recibidos desde el formulario

def update_by(id, requestForm):
    oldFile = select_all(ITEMS_DATABASE)
    newFile = oldFile

    for item in newFile:
        if int(item[0]) == id:
            item[1] = requestForm["Fecha"]
            item[2] = requestForm["Concepto"]
            item[3] = requestForm["Cantidad"]
            break

    with open(ITEMS_DATABASE, "w") as file:
        mywriter = csv.writer(file, delimiter = ",")
        mywriter.writerows(newFile)