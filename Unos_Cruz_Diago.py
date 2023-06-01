import os

os.system("cls")

print("----------------------------------------------")
print("Cargador de la cruz y diagonales de una matriz")
print("----------------------------------------------\n")

filas = int(input("Digite el numero de filas:\t"))
columnas = int(input("Digite el numero de columnas:\t"))

os.system("cls")

matriz = []

if filas != columnas:
    print("------------------------")
    print("La matriz NO es cuadrada")
    print("------------------------")
    exit()

cruz = (filas - 1) // 2

cruz_par = (filas + 1) // 2

par_impar = filas % 2

for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        diagonal_secundaria = (filas - i) - 1
        if par_impar == 0:
            # Diagonal principal
            if i == j:
                matriz[i].append(1)
            elif j == diagonal_secundaria:
                matriz[i].append(1)
            elif cruz == j:
                matriz[i].append(1)
            elif cruz == i:
                matriz[i].append(1)
            elif cruz_par == i:
                matriz[i].append(1)
            elif cruz_par == j:
                matriz[i].append(1)
            else:
                matriz[i].append(0)
        else:
            # Diagonal principal
            if i == j:
                matriz[i].append(1)
            elif j == diagonal_secundaria:
                matriz[i].append(1)
            elif cruz == j:
                matriz[i].append(1)
            elif cruz == i:
                matriz[i].append(1)
            else:
                matriz[i].append(0)

for i in range(filas):
    print(matriz[i])
