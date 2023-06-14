'''
clase vs (objeto o instancia)
tractor vs (manolo)

constructor -> se llama __init__; siempre recibe self como primer argumento;

métodos -> Cada una de las acciones que puede realizar un objeto de una clase; todos los métodos reciben un primer argumento self

instanciar -> Crear una instancia o un objeto a partir de llamar a la clase (en este ejemplo Tractor) pasando los valores que espera el constructor

solo puede haber un __init__ (constructor)
'''
class Tractor:
    def __init__(self, _nombre, _color, _marca):#Constructor
        self.nombre = _nombre
        self.color = _color
        self.marca = _marca
        self.combustible = 0
        self.posicion = [5,5]

    #Definición del método
    def arrancar(self):
        print(f"Soy {self.nombre} y estoy arrancando...")

    #Definición del método
    def desplazar(self, delta_x, delta_y):
        if self.combustible>0:
            print(f"Soy {self.nombre} y esta es mi posición actual:{self.posicion}")
            self.posicion = [self.posicion[0] + delta_x, self.posicion[1] + delta_y]
            print(f"Soy {self.nombre} y esta es mi posición después de desplazarme:{self.posicion}")
        else:
            print(f"Soy {self.nombre} y no tengo combustible")

    #Definición del método
    def repostar(self, litros : int):
        print(f'Soy {self.nombre} y estoy repostando {litros} litros de gasoil agrícola')
        self.combustible+=litros


tractor1 = Tractor("Manoliño", "Amarillo", "John Deere")#Instanciar un Tractor 
tractor1.arrancar()#Invocación a un método
tractor1.desplazar(1,1)#Invocación a un método
tractor1.repostar(3)#Invocación a un método
tractor1.desplazar(1,1)#Invocación a un método

