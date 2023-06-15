class Animal:
    def __init__(self, nombre, peso, fuerza) -> None:
        self.nombre = nombre
        self.peso = peso
        self.fuerza = fuerza

    #Proporciona a print que es lo que tiene mostrar
    def __str__(self):#Sobreescritura
        retorno = f"Soy {self.nombre} y peso {self.peso} kilos"
        return retorno
    
    #Proporciona una representación de tipo str de un objeto
    def __repr__(self) -> str:
        retorno = f"Soy {self.nombre} y peso {self.peso} kilos"
        return retorno
    
    #less than -> se invoca automáticamente por el sort y por serted
    def __lt__(self, other):#Responder is self es menor que other
        print(self.nombre, other.nombre)
        return self.peso<other.peso

leon = Animal("Leon",350,10)
elefante = Animal("Elefante",1500,15)
pollo = Animal("Pollo",1.7,20)

print(pollo)#Muestra lo que proporciona __str__

lista = [leon, elefante, pollo]
lista.sort(reverse=True)
print(lista)