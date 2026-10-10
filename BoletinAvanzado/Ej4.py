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

if __name__ == "__main__":
    cuenta1 = CuentaBancaria("Juan", 1000)
    cuenta2 = CuentaBancaria("Ana", 500)

    print(cuenta1)
    print(cuenta2)

    cuenta1.ingresar(200)
    cuenta2.retirar(100)

    print(cuenta1)
    print(cuenta2)

    # Comparación de cuentas
    cuenta3 = CuentaBancaria("Juan", 1200)
    print(f"Cuenta1 es igual a Cuenta3: {cuenta1 == cuenta3}")