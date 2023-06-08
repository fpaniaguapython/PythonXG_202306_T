#Lectura de un fichero SIN utilizar with (al estilo tradicional)
fichero_palabras = open("palabras_prohibidas.txt", mode="r", encoding="utf-8")

#datos = fichero_palabras.read()#Lee el fichero completo

#datos = fichero_palabras.read(10)#Lee los 10 primeros caracteres del fichero
#datos = fichero_palabras.read(4)#Lee los 4 caracteres siguientes a los 10 anteriores

#datos = fichero_palabras.readline()#Lee una línea (incluye el salto de línea)
#datos = fichero_palabras.readline().replace('\n','')#Lee una línea y elimina el salto de línea

datos = fichero_palabras.readlines()#Lee todas líneas y las almacena una lista, incluye los saltos de línea
print(datos)

datos_limpios = [dato.replace('\n','') for dato in datos]#Limpiamos los elementos de la lista eliminado los \n
print(datos_limpios)

fichero_palabras.close()