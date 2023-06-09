import time

PAUSA = 5

def f1():
    print("Empezando F1")
    time.sleep(PAUSA)
    print("Fin de F1")

def f2():
    print("Empezando F2")
    time.sleep(PAUSA)
    print("Fin de F2")

def f3():
    print("Empezando F3")
    time.sleep(PAUSA)
    print("Fin de F3")

cola = []

cola.insert(0,f2)#[f2]
cola.insert(0,f3)#[f3,f2]
cola.insert(0,f1)#[f1,f3,f2]

while len(cola)>0:
    print("ESTADO DE LA COLA:",cola)
    cola.pop()()