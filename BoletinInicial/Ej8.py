from datetime import datetime

class Coche:
    def __init__(self, marca, modelo, anyo):
        self.marca = marca
        self.modelo = modelo
        self.anyo = anyo

    def descripcion(self):
        return f"{self.marca} {self.modelo} ({self.anyo})"

    def es_antiguo(self):
        return self.anyo < datetime.now().year - 10

coche = Coche("Seat", "León", 2015)
print(coche.descripcion())
print(coche.es_antiguo())