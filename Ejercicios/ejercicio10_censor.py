import lector_palabras

palabras_prohibidas = lector_palabras.get_lines_from_file("palabras_prohibidas.txt")
#mensaje = input("Introduce un mensaje:")
mensaje = "A mi primo el Pollopera le gusta la tortilla de patatas más que a un Mameluco"
palabras_mensaje = mensaje.split()

for palabra in palabras_mensaje:
    if palabra in palabras_prohibidas:
        posicion_palabra = mensaje.index(palabra)
        print(f'La palabra {palabra} está prohibida')
        mensaje = mensaje.replace(palabra, "***")#Opción 1
        mensaje = mensaje[:posicion_palabra]+"***"+mensaje[posicion_palabra+len(palabra):]#Opción 2

print(mensaje)
        



