#TUPLA ES INMUTABLE

tupla1 = ()#Tupla vacía
tupla2 = tuple()#Tupla vacía
tupla3 = tuple([1,2,3])#Tupla con los elementos de la lista
tupla4 = (1,2,3)#Tupla con los números 1, 2 y 3
#tupla5 = (1)#Asigna un entero
tupla5 = (1,)#Crea una tupla con un único elemento OJO A LA COMA

print(type(tupla1))
print(type(tupla2))
print(type(tupla3))
print(type(tupla4))
print(type(tupla5))

#No se puede agregar
#No se puede eliminar
#No se puede modificar

tupla = ([1,2],[3,4],[5,6])
#tupla[0]=[7,8]#¡ERROR!
tupla[0][1]=8 #Se puede modificar el contenido de los elementos de la tupla
print(tupla)