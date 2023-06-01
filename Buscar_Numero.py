import os
import random

os.system("cls")

print("------------------------------------")
print("Buscar un valor dentro de una matriz")
print("------------------------------------\n")

filas = int(input("Digite el numero de filas:\t"))
columnas = int(input("Digite el numero de columnas:\t"))

busqueda = int(input("Digite el numero a buscar:\t"))

os.system("cls")

# Creamos una lista para usarla como matriz
matriz = []

control = []

for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        val = random.randint(i, filas)
        matriz[i].append(val)
        if val == busqueda:
            control.append([i, j])
        else:
            continue

for i in range(filas):
    print(matriz[i])

print(f"El numero valor {busqueda} esta en la posicion:{control}")
