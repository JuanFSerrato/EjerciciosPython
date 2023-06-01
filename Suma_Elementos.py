import os
import random

os.system("cls")

print("-----------------------------------------")
print("Suma de todos los elementos de una matriz")
print("-----------------------------------------\n")

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

# Contador para guardar la suma
resultado = 0

for i in range(filas):
    # Agregamos una lista por cada fila
    matriz.append([])
    for j in range(columnas):
        val = random.randint(i, filas)
        matriz[i].append(val)
        resultado += val

for i in range(filas):
    print(matriz[i])

print(f"La suma de todos los elementos es: {resultado}")
