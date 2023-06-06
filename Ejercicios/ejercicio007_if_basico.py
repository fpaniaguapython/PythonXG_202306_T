edad = input("Introduce tu edad:")#input SIEMPRE devuelve un str
edad = int(edad)

if (edad>=18):
    print("Enhorabuena")
    print("Eres mayor de edad")
else:
    print("Lo siento")
    print("Eres menor de edad")