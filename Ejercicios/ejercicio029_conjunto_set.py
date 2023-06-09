diccionario = {} #Genera un diccionario vacío

conjunto = {1,2,3}#set de 3 elementos
conjunto = set()#set vacío
conjunto = set([1,2,3])#Transformación de lista a conjunto
conjunto = set((1,2,3))#Transformación de tupla a conjunto

#No admite duplicados
#No tiene orden
frutas_invierno = {'Limón','Naranja','Limón','Uva'}
print(frutas_invierno)

frutas_verano = {'Sandía','Melón','Ciruela','Naranja'}
print(frutas_verano)

print(frutas_invierno.isdisjoint(frutas_verano))#False

print(frutas_invierno.intersection(frutas_verano))#{'Naranja'}

print(frutas_invierno.difference(frutas_verano))#{'Uva', 'Limón'}
print(frutas_verano.difference(frutas_invierno))#{'Sandía', 'Ciruela', 'Melón'}


#Halexa
base_conocimiento = [
    ("Tienes dime hora".lower(),"Son las 18:52"),
    ("Dime como se hace la tortilla de patatas".lower(),"Pela las patatas, pica la cebolla..."),
    ("Qué tiempo hace".lower(),"Está lloviendo"),
    ("Dime la capital de Francia".lower(),"París"),
    ("Cuál es la capital de Alemania".lower(),"Berlín")
]

pregunta = input("¿Qué quieres saber?")
elementos_pregunta = set(pregunta.lower().split())

intersecciones_max = 0
for conocimiento in base_conocimiento:
    elementos_conocimiento = set(conocimiento[0].split())
    intersecciones_actuales = len(elementos_pregunta.intersection(elementos_conocimiento))
    if intersecciones_actuales > intersecciones_max:
        mejor_respuesta = conocimiento[1]
        intersecciones_max = intersecciones_actuales

if intersecciones_max>0:
    print(mejor_respuesta)
else:
    print("No entiendo la pregunta")