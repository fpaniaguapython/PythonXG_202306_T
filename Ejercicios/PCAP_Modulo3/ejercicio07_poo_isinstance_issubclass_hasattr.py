class Animal:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

class Mamifero(Animal):
    pass

class Felino(Mamifero):
    pass


leon = Felino("Leoncio")
#isinstance
#Indica si un OBJETO es instancia de una CLASE
print(isinstance(leon,Felino))#True
print(isinstance(leon,Mamifero))#True
print(isinstance(leon,Animal))#True

#issubclass
#Indica si una CLASE deriva de otra CLASE
print(issubclass(Felino,Mamifero))#True
print(issubclass(Mamifero,Felino))#False
print(issubclass(Felino,Animal))#True

#hasattr 
#Indica si un objeto tiene un determinado atributo
print(hasattr(leon,"nombre"))#True
print(hasattr(leon,"apellidos"))#True

#setattr
#Asignar un valor a un atributo
print("Antes:",leon.nombre)
setattr(leon,"nombre","Simba")
print("Después:",leon.nombre)
#Equivale a:
leon.nombre="Leoncio"
