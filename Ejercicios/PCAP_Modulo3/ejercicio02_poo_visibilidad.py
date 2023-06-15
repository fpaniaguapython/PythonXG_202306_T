class CuentaBancaria:
    def __init__(self, numero, saldo) -> None:
        self.numero = numero
        self.__saldo = saldo #__ transforma el nombre del atributo en _NombreClase__nombreatributo

    #### INI DE LA ENCAPSULACIÓN
    #MÉTODO DE ACCESO - GETTER
    def get_saldo(self):
        return self.__saldo
    
    #MÉTODO DE ACCESO - SETTER
    def set_saldo(self, nuevo_saldo):
        if nuevo_saldo<0:
            raise ValueError("El nuevo saldo no puede ser negativo")
        self.__saldo = nuevo_saldo
    #### FIN DE LA ENCAPSULACIÓN

    def calcular(self):
        self.__metodo_oculto()

    def __metodo_oculto(self):#__ oculto o privado
        pass

c1 = CuentaBancaria("2834823243234",100)
#c1.__saldo = c1.__saldo - 120 #ERROR
c1.set_saldo(c1.get_saldo() - 120)
print(c1.get_saldo())

