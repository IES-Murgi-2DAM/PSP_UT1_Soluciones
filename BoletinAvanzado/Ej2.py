import os
import random

CARPETA_FICHEROS = "ficheros"
RUTA_NOTAS = os.path.join(CARPETA_FICHEROS, "notas.txt")


def generar_fichero_notas(cantidad=5):
    os.makedirs(CARPETA_FICHEROS, exist_ok=True)
    with open(RUTA_NOTAS, "w") as fichero:
        for _ in range(cantidad):
            nota = random.randint(0, 10)
            fichero.write(f"{nota}\n")


def leer_notas():
    with open(RUTA_NOTAS, "r") as fichero:
        return [int(linea.strip()) for linea in fichero]


def calcular_media(notas):
    return sum(notas) / len(notas)


def guardar_media(media):
    with open(RUTA_NOTAS, "a") as fichero:
        fichero.write(f"Media: {media}\n")


def mostrar_fichero():
    with open(RUTA_NOTAS, "r") as fichero:
        for linea in fichero:
            print(linea.strip())


def main():
    generar_fichero_notas()
    notas = leer_notas()
    guardar_media(calcular_media(notas))
    mostrar_fichero()


if __name__ == "__main__":
    main()
