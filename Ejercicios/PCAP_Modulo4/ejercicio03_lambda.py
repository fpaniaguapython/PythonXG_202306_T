#Lambda nivel 1
f1 = lambda : 2
print(f1())#2

#Lambda nivel 2
f2 = lambda x : x*2
print(f2(4))#8

#Lambda nivel 3
f3 = lambda x, y : x+y
print(f3(2,3))#5

#sorted 'tradicional'
stock = [('Cama',50),('Mesa',20),('Sillas',100),('Cabecero',0)]

def cuantificador(mueble):
    return mueble[1]
print(sorted(stock,key=cuantificador))

#sorted 'lambda'
stock = [('Cama',50),('Mesa',20),('Sillas',100),('Cabecero',0)]
print(sorted(stock,key=lambda mueble : mueble[1]))

#filter 'tradicional'
stock = [('Cama',50),('Mesa',20),('Sillas',100),('Cabecero',0)]
def tiene_stock_positivo(mueble):
    return mueble[1]>0
stock_positivo = filter(tiene_stock_positivo, stock)
for item in stock_positivo:#stock_positivo es un generador iterable
    print(item)

#filter 'lambda'
stock = [('Cama',50),('Mesa',20),('Sillas',100),('Cabecero',0)]
stock_positivo = filter(lambda mueble : mueble[1]>0, stock)
for item in stock_positivo:#stock_positivo es un generador iterable
    print(item)

#map 'tradicional'
def duplicar_stock(mueble):
    return (mueble[0],mueble[1]*2)
stock = [('Cama',50),('Mesa',20),('Sillas',100),('Cabecero',0)]

resultado = map(duplicar_stock, stock)
for r in resultado:
    print(r)

#map 'lambda'
stock = [('Cama',50),('Mesa',20),('Sillas',100),('Cabecero',0)]

resultado = map(lambda mueble : (mueble[0],mueble[1]*2), stock)
for r in resultado:
    print(r)