#Función de ordenamiento Bubble Sort
def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    return fila


def ordenar_fila_matriz(matriz, indice_fila):
    # Mostrar la matriz original
    print("Matriz original:")
    for fila in matriz:
        print(fila)

    # Ordenar la fila específica usando Bubble Sort
    matriz[indice_fila] = bubble_sort(matriz[indice_fila])

    # Mostrar la matriz con la fila ordenada
    print("\nMatriz con la fila", indice_fila, "ordenada:")
    for fila in matriz:
        print(fila)


# Matriz 3x3
matriz = [
    [18, 10, 27],
    [3, 42, 12],
    [79, 6, 51]
]

# Índice de la fila que desea ordenar
indice_fila = int(input("Introduzca la fila a ordenar: "))

# Llamar a la función para ordenar la fila
ordenar_fila_matriz(matriz, indice_fila)