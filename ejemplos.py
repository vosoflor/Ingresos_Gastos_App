# Lectura y escritura de archivos
import csv

'''
with open("data/movimientos.csv", "r") as resultado:
    leer = resultado.readline()
    print(leer)
'''

mifichero = open("data/movimientos.csv", "a", newline = '')
lectura = csv.writer(mifichero, delimiter = ',', quotechar = '"')
lectura.writerow(['19/12/2022', 'Compra de árbol de navidad', -100.50])
mifichero.close()