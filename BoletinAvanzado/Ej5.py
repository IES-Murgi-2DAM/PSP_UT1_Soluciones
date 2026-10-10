import time

def medir_tiempo(funcion):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        print(f"{funcion.__name__} tardó {fin - inicio:.4f} segundos")
        return resultado
    return wrapper

@medir_tiempo
def funcion_lenta():
    time.sleep(1)
    print("¡Acabó!")

funcion_lenta()
# Imprime: "funcion_lenta tardó 1.0012 segundos"