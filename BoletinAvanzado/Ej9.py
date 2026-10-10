import csv

# Esta función lee un archivo CSV y devuelve una lista de diccionarios, donde cada diccioanrio representa una fila y las
# claves del diccionario son los nombres de las columnas.
def leer_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        lector = csv.DictReader(csvfile)
        return [linea for linea in lector]

# Sin usar la librería csv, podemos leer un archivo CSV y devolver una lista de diccionarios de la siguiente manera:
def leer_csv_sin_libreria(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lineas = f.readlines()
        encabezados = lineas[0].strip().split(',')
        lista = []
        for linea in lineas[1:]:
            valores = linea.strip().split(',')
            row = {encabezado: valor for encabezado, valor in zip(encabezados, valores)}
            lista.append(row)
        return lista

if __name__ == "__main__":
    nombre_archivo = "ficheros/datos.csv"  # Asegúrate de que este archivo exista y tenga el formato correcto
    resultado = leer_csv(nombre_archivo)
    for fila in resultado:
        print(fila)

    otro_resultado = leer_csv_sin_libreria(nombre_archivo)
    for fila in otro_resultado:
        print(fila)