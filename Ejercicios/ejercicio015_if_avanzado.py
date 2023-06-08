edad = 60
salario = 10_000
altura = 175
if edad>65:
    print("Más de 65")
elif edad>18:
    print("Más de 18")
elif edad>5:
    print("Más de 5")
else:#Siempre es opcional
    print("No sé")


if edad>18:
    print("Eres mayor de 18")
    if edad>65:
        print("Eres mayor de 65")
    else:
        print("No eres mayor de 65")
else:
    print("Tu edad no es mayor de 18")

miedad = 31

#Estructura if 'normal'
if edad>10:
    print("OK")
    print("MAYOR DE 10")
    a=8 #Esta sentencia no tiene significado

#Estructura if 'compacta'
if edad>10:print("OK");print("MAYOR DE 10");a=8