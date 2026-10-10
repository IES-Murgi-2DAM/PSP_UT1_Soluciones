from functools import reduce

numeros = [2, 3, 4, 5]

resultado = reduce(lambda a, b: a * b, numeros)
print(resultado)  # Salida: 120