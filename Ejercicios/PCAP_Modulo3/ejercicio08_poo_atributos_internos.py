class Animal:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

class Mamifero(Animal):
    pass

class Carnivoro:
    pass

class Felino(Mamifero, Carnivoro):
    pass

leopardo = Felino("Julio")

print(Felino.__name__)#Felino
print(Felino.__module__)#__main__ o el nombre del módulo
print(Felino.__bases__)#(<class '__main__.Mamifero'>, <class '__main__.Carnivoro'>)