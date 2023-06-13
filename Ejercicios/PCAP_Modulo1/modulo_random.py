import random

#Por defecto, al semilla depende del reloj
n1 = random.random()#float en el rango [0,1)
print(n1)

random.seed(1726)#A partir de aquí, la secuencia de números siempre es la misma
print(random.random())
print(random.random())
print(random.random())
print(random.random())
print(random.random())

random.seed()#Asigna una semilla de generación del pseudoaleatorio en función del reloj
n2 = random.randint(50,55)#Entero en el rango [50,55] (ambos incluidos)
print(n2)

#range(10); range(5,15); rango(10,100,2)
n3 = random.randrange(5)#[0,5)
print(n3)
n3 = random.randrange(5,15)#[5,15)
print(n3)
n3 = random.randrange(5,15,3)#[5,15), pero solo 5, 8, 11, 14 (de 3 en 3)
print(n3)

lista = ['Metallica','Rosalía','Bad Bunny','Extremoduro']
elegido = random.choice(lista)#Elige uno de la lista
print(elegido)

lista = ['Metallica','Rosalía','Bad Bunny','Extremoduro']
elegidos = random.sample(lista, 2)#Una lista con dos elementos no repetidos
print(elegidos)
