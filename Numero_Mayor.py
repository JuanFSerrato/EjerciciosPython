import os
import random

os.system("cls")

print("--------------------")
print("Cargador de matrices")
print("--------------------\n")

filas = int(input("Digite el numero de filas:\t"))
columnas = int(input("Digite el numero de columnas:\t"))

os.system("cls")

# Creamos una lista para usarla como matriz
matriz = []

if filas != columnas:
    print("------------------------")
    print("La matriz NO es cuadrada")
    print("------------------------")
    exit()

numero_mayor = 0
auxiliar = 0

for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        val = random.randint(i, filas)
        matriz[i].append(val)
        if val > auxiliar:
            auxiliar = val
            numero_mayor = val

for i in range(filas):
    print(matriz[i])

print(f"El numero mayor es: {numero_mayor}")
