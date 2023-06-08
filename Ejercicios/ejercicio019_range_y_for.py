range(10) #0,9
range(0,10) #0,9
range(0,10,1) #0,9 de 1 en 1
range(0,10,2) #0,9 de 2 en 2

for i in range(0,10,2):
    print(i,end="-")
print()

lista = ["Fernando","Francisco","Alberte"]

for nombre in lista:
    print(nombre)

tupla = ("Fernando","Francisco","Alberte")

#Recorrer la tupla con un for mostrando los nombres 
#convertidos a mayúsculas.
for nombre in tupla:
    print(nombre.upper())
else:
    print("else del for")#Se ejecuta porque se termina el bucle


#Recorrer la tupla con un for mostrando los nombres 
#convertidos a mayúsculas.
#Si el nombre que estamos procesando contiene la letra 'i' 
#   mostramos el nombre y hacemos un break
for nombre in tupla:
    print(nombre.upper())#Solo mostrará FERNANDO Y FRANCISCO
    if 'i' in nombre:
        break
    #if nombre.count("i"):break#Alternativa de Javier
    #if nombre.find("i")>=0:break#Alternativa con find
else:
    print("else del for")#No se ejecuta porque se hace break

