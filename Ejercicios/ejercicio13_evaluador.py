from config import MAYORIA_EDAD

nombre="Roberto"
edad=30
altura=180
japones=True
ruso=False

#Mayor de edad, medir más de 150, hablar japonés y/o ruso
#El nombre no puede contener la letra a

#Solución de Tamara
if (edad>=18 and altura>150 and (japones or ruso) and "a" not in nombre):
    print("Contratado")
else:
    print("No cumple los requisitos")


#Solución de Tamara con CONSTANTES
ALTURA_MINIMA = 150
LETRA_PROHIBIDA = 'a'

if (edad>=MAYORIA_EDAD and altura>ALTURA_MINIMA and (japones or ruso) and LETRA_PROHIBIDA not in nombre):
    print("Contratado")
else:
    print("No cumple los requisitos")

numero_meses = 18

#Solución legible XXL
mayor_edad = edad>=MAYORIA_EDAD
altura_suficiente = altura>ALTURA_MINIMA
conoce_idioma = (japones or ruso)
no_contiene_letra_prohibida = LETRA_PROHIBIDA not in nombre

if mayor_edad and altura_suficiente and conoce_idioma and no_contiene_letra_prohibida:
    print("Contratado")
else:
    print("No cumple los requisitos")  