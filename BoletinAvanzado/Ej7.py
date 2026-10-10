from Ej4 import CuentaBancaria, SaldoInsuficienteError

# He modificado la clase CuentaBancaria para que lance una excepción personalizada SaldoInsuficienteError cuando se
# intente retirar más dinero del que hay en la cuenta.

# main
if __name__ == "__main__":
    c = CuentaBancaria("Bob", 100)
    try:
        c.retirar(200)
    except SaldoInsuficienteError as e:
        print(e) # Imprime: "Saldo insuficiente: tienes $100 €, intentas retirar $200 €"