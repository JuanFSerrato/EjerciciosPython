import os
import random

os.system("cls")

print("----------------------------------")
print("Suma de las columnas de una matriz")
print("----------------------------------\n")

filas = int(input("Digite el numero de filas:\t"))
columnas = int(input("Digite el numero de columnas:\t"))

os.system("cls")

# Creamos dos listas para usarlas como matrices
matriz = []
suma = []

if filas != columnas:
    print("------------------------")
    print("La matriz NO es cuadrada")
    print("------------------------")
    exit()

for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        val = random.randint(i, filas)
        matriz[i].append(val)

auxiliar = 0
suma_mayor = 0

for i in range(filas):
    resultado = 0
    for j in range(columnas):
        resultado += matriz[j][i]
        if resultado > auxiliar:
            auxiliar = resultado
            suma_mayor = i + 1
    suma.append(resultado)

for i in range(filas):
    print(matriz[i])

print(suma)
print(f"La columna con la suma mayor es la numero: {suma_mayor}")
