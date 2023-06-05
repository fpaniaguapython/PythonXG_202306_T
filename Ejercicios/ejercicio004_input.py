nombre = input("Introduce tu nombre:") #input SIEMPRE devuelve un str 
print("Te llamas",nombre)

'''
Solicitar al usuario su nombre, la localidad de residencia y la dirección de correo electrónico
Mostrar los datos de la siguiente manera:
Te llamas Fernando, vives en Alcorcón y tu dirección de correo es fernando.paniagua@gmail.com
'''
nombre = input("Introduce tu nombre:")
localidad = input("Introduce la localidad en la que resides:")
email = input("Introduce tu dirección de correo electrónico:")
print("Te llamas",nombre,", vives en",localidad,"y tu dirección es",email)#Te llamas Fernando , vives en Alcorcón y tu dirección es fernando.paniagua@gmail.com
print("Te llamas",nombre,", vives en",localidad,"y tu dirección es",email, sep="")#Te llamasFernando, vives enAlcorcóny tu dirección esf@gmail.com
print("Te llamas ",nombre,", vives en ",localidad," y tu dirección es ",email, sep="")#Te llamas Fernando, vives en Alcorcón y tu dirección es fernando@gmail.com
#Usando f-string
print(f"Te llamas {nombre}, vives en {localidad} y tu dirección es {email}")