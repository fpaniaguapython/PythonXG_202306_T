frase = "Me gusta ver atardecer desde el balcón"

trozo = frase[0:8:1]
print(trozo)#'Me gusta'
trozo = frase[0:8:2]
print(trozo)#'M ut'
trozo = frase[0:8]#step por defecto es 1
print(trozo)#'Me gusta'
trozo = frase[:8]#inicio por defecto es 0
print(trozo)#'Me gusta'
trozo = frase[:]#Desde el primero hasta el último de 1 en 1
print(trozo)#Me gusta ver atardecer desde el balcón

fichero = "imagen.jpg"
nombre = fichero[:6]
extension = fichero[7:]
print(nombre)#imagen
print(extension)#jpg
fichero = "imagen.jpeg"
extension = fichero[-4:]
print(extension)#jpeg

linea = "amazonas\n"
linea_limpia = linea[:-1]
print(linea_limpia)#amazonas

palabra = "minotauro"
print(palabra[::-1])#oruatonim

