#referencia a self APLICA IGUAL A MÉTODOS QUE A ATRIBUTOS
#invocación a super()

#referencia a self

class Motor:
    def __init__(self) -> None:
        self.potencia = 100

    def saludar(self):
        print("Hola, soy el Motor")

    def sumar_uno_a_potencia(self):
        self.potencia+=1

    def incrementar_potencia(self):
        self.sumar_uno_a_potencia()#Invocando un método a través de self
        print(self.potencia)#Acceso al atributo a través de self

m1 = Motor()
m1.incrementar_potencia()#Invocando un método a través de la referencia de un objeto
print(m1.potencia)#Acceso al atributo a través de la referencia de un objeto

#referencia a super

class MotorElectrico(Motor):
    def saludar(self):
        super().saludar()
        print("Hola soy el MotorElectrico")
    

me = MotorElectrico()
me.saludar()