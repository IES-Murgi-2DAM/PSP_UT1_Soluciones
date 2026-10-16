class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Ingresado: {cantidad}. Nuevo saldo: {self.saldo}")
        else:
            print("La cantidad a ingresar debe ser positiva.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retirado: {cantidad}. Nuevo saldo: {self.saldo}")
        else:
            raise SaldoInsuficienteError(f"Saldo insuficiente: tienes ${self.saldo} €, intentas retirar ${cantidad} €")

    def __str__(self) -> str:
        return f"Titular: {self.titular} - Saldo: {self.saldo} €"

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, CuentaBancaria):
            return False
        return self.titular == value.titular and self.saldo == value.saldo

class SaldoInsuficienteError(Exception):
    pass

# main
if __name__ == "__main__":
    c = CuentaBancaria("Bob", 100)
    try:
        c.retirar(200)
    except SaldoInsuficienteError as e:
        print(e) # Imprime: "Saldo insuficiente: tienes $100 €, intentas retirar $200 €"