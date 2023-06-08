i=0
while i<10:#Del 0 al 9
    print(i, end="-")
    i+=1

print();i=0
while i<10:#Del 0 al 4
    print(i, end="-")
    i+=1
    if i==5:
        break

print();i=0
while i<10:#Del 0 al 9
    print(i, end="-")
    i+=1
else:#Se ejecuta si el bucle deja de cumplir la condición
    print("else del while")

i=0
while i<10:#Del 0 al 4
    print(i, end="-")
    i+=1
    if i==5:
        break
else:#No se ejecutar porque se sale mediante un break
    print("else del while")
