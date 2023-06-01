import os
import random

os.system("cls")

print("----------------------")
print("Promedio de una matriz")
print("----------------------\n")

filas = int(input("Digite el numero de filas:\t"))
columnas = int(input("Digite el numero de columnas:\t"))

os.system("cls")

# Creamos una lista para usarla como matriz
matriz = []

resultado = 0

for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        val = random.randint(i, filas)
        matriz[i].append(val)
        resultado += val

for i in range(filas):
    print(matriz[i])

promedio = resultado / (filas * columnas)

print(f"El promedio es: {promedio}")
