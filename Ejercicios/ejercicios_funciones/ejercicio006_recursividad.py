#4!=4*3*2*1
#3!=3*2*1

#4!=4*3! - El factorial de 4 es 4 * el factorial de 3
#3!=3*2! - El factorial de 3 es 3 * el factorial de 2
#2!=2*1! - El factorial de 2 es 2 * el factorial de 1
#1!=1
def factorial(numero):
    if numero>1:
        resultado = numero * factorial(numero-1)
    else:
        resultado = 1
    return resultado

r = factorial(999)#Si calculamos con 1000 o más -> RecursionError (Stack Overflow en otros lenguajes) 
print(r)