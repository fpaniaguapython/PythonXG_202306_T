def funcion1():
    x = 5#Ámbito local
    print(x)#5

x = 8 #Ámbito global
funcion1()
print(x)#8


def funcion2(x):#Ámbito local
    x=x+1
    print(x)#9

x = 8 #Ámbito global
funcion2(x)
print(x)#8

def funcion3():
    '''
    x=x+1 #ERROR porque intenta leer la x local en el incremento
    print(x)
    '''
    global x #Quiero que utilices la x global y no crees una nueva variable local
    x=x+1
    print(x)#2

x = 1 #Ámbito global
funcion3()
print(x)#2


def funcion_definicion():
    global numero
    numero = 3 #Creando una variable global desde un ámbito local

funcion_definicion()
print(numero)