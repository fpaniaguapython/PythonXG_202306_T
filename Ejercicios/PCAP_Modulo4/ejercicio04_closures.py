#Modo básico
def funcion_externa():
    def funcion_interna():
        print("Hola")
    return funcion_interna

f1 = funcion_externa()#Va a devolver la función interna
f1()#Ejecutamos la función interna

#Modo menos básico
def funcion_externa(numero):
    def funcion_interna():
        print(numero)
    return funcion_interna

numero = 10
f2 = funcion_externa(numero)#Va a devolver la función interna
numero = 12
f2()#Ejecutamos la función interna

#Modo menos-menos básico
def funcion_externa(numero):
    def funcion_interna(multiplicador):
        print(numero*multiplicador)
    return funcion_interna

numero = 10
f3 = funcion_externa(numero)#Va a devolver la función interna
numero = 12
f3(2)#Ejecutamos la función interna