numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
frase = "aprende python en la fp"
cadena = "hola mundo"

# Lista con los cuadrados de los números pares
cuadrados_pares = [x**2 for x in numeros if x % 2 == 0]
print(cuadrados_pares)

# Lista con las longitudes de cada palabra de una frase
longitudes_palabras = [len(palabra) for palabra in frase.split()]
print(longitudes_palabras)

# Lista con los caracteres en mayúsculas de una cadena
mayusculas = [caracter.upper() for caracter in cadena if caracter.isalpha()]
print(mayusculas)