class CuentaBancaria:
    tipo_interes = 10
    def __init__(self) -> None:
        self.saldo = 10

cuenta = CuentaBancaria()

print(hasattr(cuenta,'saldo'))#True
print(hasattr(cuenta,'tipo_interes'))#True

print(hasattr(CuentaBancaria,'saldo'))#False
print(hasattr(CuentaBancaria,'tipo_interes'))#True
