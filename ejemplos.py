# Lectura y escritura de archivos
import csv
from app_registro import routes
'''
with open("data/movimientos.csv", "r") as resultado:
    leer = resultado.readline()
    print(leer)


mifichero = open("data/movimientos.csv", "a", newline = '')
lectura = csv.writer(mifichero, delimiter = ',', quotechar = '"')
lectura.writerow(['19/12/2022', 'Compra de árbol de navidad', -100.50])
mifichero.close()

mifichero = open("data/movimientos.csv", "r") # Acceder al archivo y configurarlo para cargar un nuevo registro
csvReader = csv.reader(mifichero, delimiter = ",", quotechar = '"') # Accede a cada registro del archivo y lo formatea
datos = [] # Array de datos vacío para cargar los registros del archivo

for item in csvReader: # Recorrer el objeto csvReader y cargar cada registro al array
    datos.append(item)

print(len(datos))
print(type(datos))
print(datos[len(datos)-1])
print(datos[len(datos)-1][0])
print(type(datos[len(datos)-1][0]))
print(int(datos[len(datos)-1][0]))
print(type(int(datos[len(datos)-1][0])))

datos = routes.listItems("data/last_id.csv")
print(datos)
print(type(datos))
print(int(datos[0][0]) + 1)

from app_registro import routes

oldFile = routes.listItems("data/movimientos_prueba.csv")
newFile = oldFile

for itemPosition, item in enumerate(newFile):
    if int(item[0]) == 1:
        newFile.pop(itemPosition)
        break

with open("data/movimientos_prueba.csv", "w") as file:
    mywriter = csv.writer(file, delimiter = ",")
    mywriter.writerows(newFile)

'''