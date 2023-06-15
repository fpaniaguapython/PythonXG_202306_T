#HERENCIA también conocida como EXTENSIÓN

#Clase base o superclase o clase padre
class Vehiculo(object):
    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def arrancar(self):
        print(f"Arrancando Vehiculo:{self.nombre}")

#Clase derivada o subclase o clase hija
class Automovil(Vehiculo):
    def __init__(self, nombre, numero_ruedas) -> None:
        super().__init__(nombre)
        self.numero_ruedas = numero_ruedas

auto = Automovil('Troncomóvil')#Construyendo una instancia de AutomovilElectrico y asignando la referencia a ae
auto.arrancar()

#POLIMORFISMO
print(isinstance(auto, Automovil))#Juan Pedre dice True
print(isinstance(auto, Vehiculo))#Francisco dice True


#Clase derivada o subclase o clase hija
class Embarcacion(Vehiculo):
    def __init__(self, nombre, eslora) -> None:
        #super().__init__(nombre)#Llamada al constructor de la clase base a partir de la instancia
        Vehiculo.__init__(self, nombre)#Llamada al constructor de la clase base a partir de la clase
        self.eslora = eslora
