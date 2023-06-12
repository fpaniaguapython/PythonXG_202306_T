#pip install requests
import requests
import descargador_imagenes

KEY = '95c08eba'
URL = 'http://www.omdbapi.com'

titulo = input("Título de la película:")

#http://www.omdbapi.com/?apikey=95c08eba&t=Batman
parametros = {'apikey': KEY, 't': titulo}
r = requests.get(URL, params=parametros)
if r.status_code==200:#200 es el código OK de HTTP
    pelicula = r.json()
    #Mostrar Título, Director, Sinopsis, Año de estreno, y los actores
    print(pelicula['Title'])
    print(pelicula.get("Director","No dispongo de director"))
    print(pelicula['Plot'])
    print(pelicula['Released'])
    #Para batman, actores -> 'Michael Keaton, Jack Nicholson, Kim Basinger'
    #strip, elimina los espacios de los extremos
    #lstrip, rstrip, eliminar los espacios de la izquierda o de la derecha
    actores = [pelicula.strip() for pelicula in pelicula['Actors'].split(',')]
    #Después de la conversión, actores -> ['Michael Keaton', 'Jack Nicholson', 'Kim Basinger']
    for actor in actores:
        print("Actor:",actor)
    descargador_imagenes.download_image(pelicula['Poster'],pelicula['Title'].replace(' ','-')+".jpg")
elif r.status_code==401:#401 es el código error Unauthorized
    print("La KEY utilizada no es válida")
else:
    print("Ha ocurrido un error HTTP:",r.status_code)