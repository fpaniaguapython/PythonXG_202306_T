#Suma números enteros pares
#Tenemos que ASEGURARNOS de que los parámetros son NÚMEROS ENTEROS 
#Tenemos que ASEGURARNOS de que los parámetros son NÚMEROS PARES
def sumar(s1 : int, s2 : int):
    if not isinstance(s1, int) or not isinstance(s2, int):
        raise TypeError("Los parámetros deben ser enteros")
    if s1%2!=0 or s2%2!=0:
        raise ValueError("Los parámetros deben ser números pares")
    return s1 + s2


try:
    sumar(4,8)
    sumar(4,9)
    sumar(4,8.8)
    sumar(4,True)
except (TypeError, ValueError) as error:
    print(error)

#sumar(4,"Siete") - Provoca un error porque + no admite int y str