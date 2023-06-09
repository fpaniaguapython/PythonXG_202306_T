#max y min - aplican tanto a listas como a tuplas

lista = [3,8,-4,5]
print(max(lista))

lista = ["Zamora","Teclado","Agua"]
print(min(lista))

def valorar(ciudad):
    valoracion = ciudad[1]  
    return valoracion

ciudades = [("Pontevedra",6),("Lugo",5),("A Coruña",9),("Santiago",10),("Vigo",7),("Ourense",8)]

print(max(ciudades, key=valorar))  
print(min(ciudades, key=valorar))  

