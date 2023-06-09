diccionario1 = {}  # Diccionario vacío
diccionario2 = dict()  # Diccionario vacío

diccionario = {1: "Uno", 0: "Cero", "Python": 1990, 3: "Tres", 8: "Ocho"}

# Acceso a los elementos
print(diccionario[3])  # Tres
print(diccionario['Python'])  # 1990
# print(diccionario['Java'])#KeyError

print(diccionario.get('Python'))  # Python
print(diccionario.get('Java'))  # None
print(diccionario.get('Java', "No tengo información"))  # No tengo información

# Modificación
diccionario[1] = 'One'
# {1: 'One', 0: 'Cero', 'Python': 1990, 3: 'Tres', 8: 'Ocho'}
print(diccionario)

# Eliminación y obtención
valor = diccionario.pop(1)
print(valor)  # One
print(diccionario)  # {0: 'Cero', 'Python': 1990, 3: 'Tres', 8: 'Ocho'}

elemento = diccionario.popitem()  # El último
print(elemento)  # (8, 'Ocho')
print(diccionario)  # {0: 'Cero', 'Python': 1990, 3: 'Tres'}

# Recorrer un diccionario

for clave in diccionario.keys():
    print(clave)

for value in diccionario.values():
    print(value)

for clave, valor in diccionario.items():
    print(clave, valor)


equipo_futbol1 = {"Real Madrid": ["Modric", "Alaba", "Vicius"],
                  "Compostela": ["Jugador1", "Jugador2", "Jugador3"]}

print(equipo_futbol1['Real Madrid'][1])

equipo_futbol2 = {"Real Madrid": {"Estadio": "Santiago Bernabeu", "Presupuesto": 10_000_000},
                  "Compostela": {"Estadio": "Verónica Boquete de San Lázaro", "Presupuesto": 5_000_000}}

print(equipo_futbol2['Real Madrid']['Estadio'])
print(equipo_futbol2['Compostela']['Presupuesto'])

# Crear un diccionario que tenga la siguiente información de una película:
# Título: El resplandor
# Sinopsis: La película relata la historia de Jack Torrance
# Director: Stanley Kubrick
# Año de estreno: 1980

pelicula = {
    'Título': 'Sexto Sentido',
    'Sinopsis': 'Psicólogo ayuda a niño que ve personas muerta',
    'Director': 'M. Night Shyamalan',
    'Año de estreno': 1999
}

print(pelicula['Título'])
print(pelicula.get('Director'))