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
    pelicula_dict = r.json()
    #Mostrar Título, Director, Sinopsis, Año de estreno, y los actores
    print(pelicula_dict.get("Director","No dispongo de director"))
    descargador_imagenes.download_image(pelicula_dict['Poster'],pelicula_dict['Title'].replace(' ','-')+".jpg")
else:
    print("Ha ocurrido un error HTTP:",r.status_code)