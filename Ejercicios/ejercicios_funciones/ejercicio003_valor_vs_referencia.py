#PASO DE PARÁMETROS POR VALOR (int, float, str, bool)
def funcion1(x):#x es local
    x=x+1
    print(x)#6

x=5 #x es global
funcion1(x)
print(x)#5

#PASO DE PARÁMETROS POR REFERENCIA (list, diccionario, 'objetos complejos')
def funcion2(y):
    y.append("f2")
    print(y)#['x1', 'x2', 'f2']

y=['x1','x2']
funcion2(y)
print(y)#['x1', 'x2', 'f2']