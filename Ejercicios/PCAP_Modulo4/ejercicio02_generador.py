import random

#Generador a través de una función 
def dame_numero_aleatorio():
    for i in range(100):
        aleatorio = random.random()
        yield aleatorio

for numero in dame_numero_aleatorio():
    print(numero)

#Generador a través de una 'comprensión de listas'
lista = ['Primavera','Verano','Otoño','Invierno']

lista_mayusculas = [estacion.upper() for estacion in lista]
print(lista_mayusculas)#EN ESTE MOMENTO TEN DOS LISTAS COMPLETAS

generador_mayusculas = (estacion.upper() for estacion in lista)
print(generador_mayusculas)#<generator object <genexpr> at 0x000001EAFC038040>
for estacion_mayusculas in generador_mayusculas:
    print(estacion_mayusculas)