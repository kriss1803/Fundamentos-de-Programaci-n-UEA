#Función para buscar el valor en la matriz
def buscar_valor(matriz, valor_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_buscado:
                return f"El valor {valor_buscado} se encuentra en la posición ({i}, {j})."
    return f"El valor {valor_buscado} no se encuentra en la matriz."

# Matriz 3x3
matriz = [
    [10, 18, 27],
    [3, 12, 42],
    [79, 6, 51]
]

# Valor a buscar en la matriz
valor_buscado = int(input("Introduzca el valor a buscar en la matriz: "))

# Llamar a la función y mostrar el resultado
resultado = buscar_valor(matriz, valor_buscado)
print(resultado)