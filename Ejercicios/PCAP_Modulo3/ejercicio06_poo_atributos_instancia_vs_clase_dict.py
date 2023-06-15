class CuentaBancaria:
    credito_preconcedido = 800 #Atributo o variable de clase. Compartidos por todas las instancias.
    def __init__(self, numero, saldo) -> None:
        self.numero = numero #Atributo o variable de instancia u objeto
        self.__saldo = saldo
        
cuenta_tamara = CuentaBancaria("2834823243234",100)
cuenta_ruben = CuentaBancaria("384378423", 800)
cuenta_alberte = CuentaBancaria("324842378234", 300)

print(CuentaBancaria.credito_preconcedido)

#Atributo __dict__ aplicado a un objeto
#proporciona sus atributos de instancia y sus valores, incluidos los ocultos. IGNORA LOS ATRIBUTOS DE CLASE
print(cuenta_tamara.__dict__)
#Atributo __dict__ aplicado a una clase
#proporciona los atributos de clase, __module__, __init__, y algunos más
print(CuentaBancaria.__dict__)