def evaluar(valor, numero):#Hace eco del valor
    print("Evaluando",numero)
    return valor

if evaluar(False,1) and evaluar(True, 2):#No evalua 2, porque 1 es False
    print("OK")
else:
    print("KO")

if evaluar(True,3) or evaluar(False, 4):#No evalua 4, porque 1 es True
    print("OK")
else:
    print("KO")