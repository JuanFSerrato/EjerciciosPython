import os
import random

os.system("cls")

print("--------------------------------")
print("Suma de diagonales de una matriz")
print("--------------------------------\n")

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
        # Contador para crear la diagonal secundaria
        cont = (filas - i) - 1
        val = random.randint(i, filas)
        # Agregar valores en la diagonal principal
        if i == j:
            matriz[i].append(val)
            resultado += val
        # Agregar valores en la diagonal secundaria
        elif j == cont:
            matriz[i].append(val)
            resultado += val
        else:
            matriz[i].append(0)

for i in range(filas):
    print(matriz[i])

print(f"La suma de las diagonales es: {resultado}")
