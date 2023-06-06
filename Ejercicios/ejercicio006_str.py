#OJO--> LAS CADENAS SON INMUTABLES

cadena1 = 'Esto es un str'
cadena2 = "Esto es un str"
cadena3 = '''Esto es un str
que almacena varias
líneas.
'''

#FUNCIÓN VS MÉTODO
#Función len
longitud = len(cadena1)#Calcula la longitud de una cadena (y de una lista, una tupla, etc...)
print(longitud)

#Métodos
titulo = "el resplandor"
print(titulo.capitalize())#Convierte la primera a mayúsculas y el resto a minúsculas. El resplandor

titulo = "La venganza de Don Mendo"
numero_veces_don = titulo.count("Don")#Calcula el número de veces que aparece un subcadena
print(numero_veces_don)

titulo_mayusculas = titulo.upper()#Convierte a mayúsculas
titulo_minusculas = titulo.lower()#Convierte a minúscula
print(titulo_mayusculas)
print(titulo_minusculas)

#El texto 'ver' aparece 1 veces
#El texto 'VER' aparece 1 veces
#No importa que el texto esté en mayúsculas o minúculas
frase = "Me gusta ver atardecer desde el balcón"
texto_a_buscar = input("Introduce el texto a buscar:")

numero_veces = frase.lower().count(texto_a_buscar.lower())

print(f'El texto \'{texto_a_buscar}\' aparece {numero_veces} veces')

#Method chaining
frase = "Me gusta ver atardecer desde el balcón"
print(frase[0:10].upper().capitalize()[3:].replace('a','@'))#gust@ v
#print(frase[0:10].upper().count("a").capitalize()[3:].replace('a','@'))#Error porque count devuelve un entero

fichero = "mismemorias.dOCx"
print(fichero.upper().endswith("DOCX"))

#Operador in
#'El regreso de la momia'
#'momia' in titulo
palabras_prohibidas = "momia vampiro Ajo clavo estaca"
palabra = input("Introduce una palabra:")
#Indicar si la palabra introducida está o no prohibida (sin importar si es mayúsculas o minúsculas)
#Solución FLORIÁN
if palabra.lower() in palabras_prohibidas.lower():
    print("La palabra está prohibida")
else:
    print("La palabra NO está prohibida")

#Solución ÓSCAR (parte de una lista de palabras prohibidas almacenadas en una cadena)
#Parte de la premisa de que todas las palabras prohibidas están en minúsculas
palabras = ["momia", "vampiro", "Ajo", "clavo", "estaca"]
palabra = input("Ingresa una palabra: ")
palabra = palabra.lower()
if palabra in palabras:
    print("La palabra está presente en la lista.")
else:
    print("La palabra no está en la lista.")