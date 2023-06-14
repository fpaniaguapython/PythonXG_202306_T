def cuantificador(elemento):
    return elemento[1]#Cantidad invertida en la empresa

#sort - es un método
lista1 = [3, 8 ,0, 15, 1]
lista1.sort()#Ordena la lista
print(lista1)


#sorted - es una función
lista1 = [3, 8 ,0, 15, 1]
lista2 = sorted(lista1)#Generar una copia de lista ordenada
print(lista1)
print(lista2)

#sort - con una lista con una estructura compleja
cartera = [('BBVA',10_000),('TELEFÓNICA',5_000),('ACS',7000)]
cartera.sort()
print(cartera)
cartera.sort(key=cuantificador)
print(cartera)
cartera.sort(key=cuantificador, reverse=True)
print(cartera)