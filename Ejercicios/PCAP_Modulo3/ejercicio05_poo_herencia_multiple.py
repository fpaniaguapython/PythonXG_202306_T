class Vehiculo(object):
    def __init__(self, nombre) -> None:
        self.nombre = nombre
    def arrancar(self):
        print(f"Arrancando Vehiculo:{self.nombre}")
    def saludar(self):
        pass

class Automovil(Vehiculo):
    def arrancar(self):
        print(f"Arrancando Automovil:{self.nombre}")
    def rodar(self):
        pass

class Embarcacion(Vehiculo):
    def arrancar(self):
        print(f"Arrancando Embarcacion:{self.nombre}")
    def navegar(self):
        pass

#HERENCIA MÚLTIPLE
class Anfibio(Automovil, Embarcacion):
    def arrancar(self):
        print(f"Arrancando Anfibio:{self.nombre}")
    def arrastrar(self):
        pass

anf = Anfibio("Anfibio1")
anf.arrastrar()
anf.navegar()
anf.rodar()
anf.saludar()

#Problema del diamante (resolución en la búsqueda de métodos en herencias múltiples)
anf.arrancar()