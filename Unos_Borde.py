import os

os.system("cls")

print("--------------------------------")
print("Cargador de bordes de una matriz")
print("--------------------------------\n")

filas = int(input("Digite el numero de filas:\t"))
columnas = int(input("Digite el numero de columnas:\t"))

os.system("cls")

# Creamos una lista para usarla como matriz
mat = []

if filas != columnas:
    print("------------------------")
    print("La matriz NO es cuadrada")
    print("------------------------")
    exit()

for i in range(filas):
    # Agregamos una lista por cada fila
    mat.append([])
    for j in range(columnas):
        if i == 0 or j == 0 or i == filas-1 or j == filas-1:
            mat[i].append(1)
        else:
            mat[i].append(0)

for i in range(filas):
    print(mat[i])
