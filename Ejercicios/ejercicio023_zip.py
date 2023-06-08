#HACIENDO ZIP DE TRES ESTRUCTURAS DEL MISMO TAMAÑO
nombres = ("Zaragoza", "Murcia", "Alcorcón")
poblaciones = [666_880, 447_182, 169_502]
provincia = ["Zaragoza", "Murcia", "Madrid"]

ciudades = zip(nombres, poblaciones, provincia)
lista_ciudades = list(ciudades)
print(lista_ciudades)

#HACIENDO ZIP DE TRES ESTRUCTURAS DE DISTINTO TAMAÑO
nombres = ("Zaragoza", "Murcia", "Alcorcón")
poblaciones = [666_880, 447_182]
provincia = ["Zaragoza", "Murcia", "Madrid"]

ciudades = zip(nombres, poblaciones, provincia)
lista_ciudades = list(ciudades)
print(lista_ciudades)

#HACIENDO ZIP DE TRES ESTRUCTURAS DE DISTINTO TAMAÑO CON ERROR
nombres = ("Zaragoza", "Murcia", "Alcorcón")
poblaciones = [666_880, 447_182]
provincia = ["Zaragoza", "Murcia", "Madrid"]

ciudades = zip(nombres, poblaciones, provincia, strict=True)
lista_ciudades = list(ciudades)
print(lista_ciudades)

