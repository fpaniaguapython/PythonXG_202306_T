#base nunca puede ser 0
def calcular_importe(base : int):
    assert base!=0, "La base no puede 0"
    print("Calculando importe...")

'''
#NORMALMENTE NO SE TRATAN LOS assert
try:
    calcular_importe(0)
except AssertionError as ae:
    print("Assertion Error:", ae)
'''