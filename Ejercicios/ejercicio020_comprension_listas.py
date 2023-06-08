#Insertar en la lista2 los números de la lista1 multiplicados * 2
lista1 = [1, 3, 5, 8]

'''lista2 = list()#Crea una lista vacía
for numero in lista1:
    lista2.append(numero*2)'''

lista2 = [numero*2 for numero in lista1]

print(lista2)

#Insertar en la lista lista_nombres_mayusculas los nombre de lista_nombres convertidos a mayúsculas
lista_nombres = ["Julio","Ricardo","Susana","Isabel"]

'''lista_nombres_mayusculas = []#Crea una lista vacía
for nombre in lista_nombres:
    lista_nombres_mayusculas.append(nombre.upper())'''

lista_nombres_mayusculas = [nombre.upper() for nombre in lista_nombres]

print(lista_nombres_mayusculas)

#Insertar en la lista lista_nombres_mayusculas los nombre de lista_nombres 
#convertidos a mayúsculas y sustituyendo las letras 'a' por '@' 
lista_nombres = ["Julio","Ricardo","Susana","Isabel"]
#["JULIO","RIC@RDO","SUS@N@","IS@BEL"]
lista_nombres_convertidos = [nombre.upper().replace('A','@') for nombre in lista_nombres]
print(lista_nombres_convertidos)

