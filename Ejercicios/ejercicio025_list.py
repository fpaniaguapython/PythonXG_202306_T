#EN PYTHON TODO ES OBJECT

lista1 = list()
lista2 = []
lista3 = list((1,2,3))#A partir de una tupla
lista4 = list(range(10))#A partir de un rango

#Añadir elementos
lista3.append("Último")#Añade al final
print(lista3)#[1, 2, 3, 'Último']
lista3.insert(0, "Primero")#Añade en una posición concreta
print(lista3)#['Primero', 1, 2, 3, 'Último']

#Modificar elementos
lista3[2]="Dos" #Modifica el contenido del elemento situado en la posición 2
print(lista3)

#Eliminar elementos
lista3.remove("Dos") #Elimina el primer elemento que coincida
print(lista3)

#['Primero', 1, 3, 'Último']
elemento = lista3.pop()#Obtiene el último elemento y lo elimina de la lista
print(elemento, lista3)#'Último',['Primero', 1, 3]
elemento = lista3.pop(0)
print(elemento, lista3)#Primero [1, 3]

#Lectura de la lista
lista3 = ["Uno","Dos","Tres"]
print(lista3[1])#Dos

for elemento in lista3:
    print(elemento)

#Ordenación de listas
ciudades = ["Pontevedra","Lugo","A Coruña","Santiago","Vigo","Ourense"]
ciudades.sort() #Ordena y modifica
print(ciudades)
ciudades.reverse() #Da la vuelta a la lista
print(ciudades)

ciudades = [("Pontevedra",10),("Lugo",8),("A Coruña",9),("Santiago",10),("Vigo",7),("Ourense",8)]
print(ciudades)
ciudades.sort()
print(ciudades)

def valorar(ciudad):
    valoracion = ciudad[1]  
    return valoracion  

#ciudades.sort(key=valorar)#De menor a mayor
ciudades.sort(key=valorar, reverse=True)#De mayor a menor
print(ciudades)
print(f'La mejor ciudad para caminar por la calle es {ciudades[0][0]}')#f-string

#Representar una estructura de datos que contenga:
# Nombre de un restaurante
# Valoración de la calidad (0,10)
# Valoracion del precio (0,10)
# Valoración de la ubicación (0,10)

#Calidad*3+Precio*2+Ubicacion*1

def calificar_restaurante(restaurante):
    valoracion = restaurante[1]*3+restaurante[2]*2+restaurante[3]*1
    return valoracion

def calificar_restaurante_por_precio(restaurante):
    valoracion = restaurante[2]
    return valoracion

restaurante1 = ("Burguer King", 7, 10, 0)#21+20+0=41
restaurante2 = ("Artabra", 10, 8, 8)#30+16+8=54
restaurante3 = ("Acivro", 9, 9, 6)#27+18+6=49

restaurantes = [restaurante1, restaurante2, restaurante3]
restaurantes.sort(key=calificar_restaurante, reverse=True)#Ordena la lista
print(f'El restaurante candidato es {restaurantes[0][0]}')

#Ordenación función sorted

restaurante1 = ("Burguer King", 7, 10, 0)#21+20+0=41
restaurante2 = ("Artabra", 10, 8, 8)#30+16+8=54
restaurante3 = ("Acivro", 9, 9, 6)#27+18+6=49

restaurantes = [restaurante1, restaurante2, restaurante3]

restaurantes_ordenados = sorted(restaurantes,key=calificar_restaurante,reverse=True)#Genera una lista ordenada
print(restaurantes)
print(restaurantes_ordenados)