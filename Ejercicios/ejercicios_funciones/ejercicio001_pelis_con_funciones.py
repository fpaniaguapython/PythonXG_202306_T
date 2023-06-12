import requests

KEY = '95c08eba'
URL = 'http://www.omdbapi.com'

def mostrar_pelicula(pelicula):
    print("Título:",pelicula['Title'])
    print("Director:", pelicula.get("Director","No dispongo de director"))
    print("Resumen:", pelicula['Plot'])
    print("Fecha de Estreno:", pelicula['Released'])
    actores = [pelicula.strip() for pelicula in pelicula['Actors'].split(',')]
    for actor in actores:
        print("Actor:",actor)

def mostrar_pelicula_guay(pelicula):
    lista_titulares = ['Título','Director','Resumen','Fecha de Estreno','Year']
    lista_claves = ['Title','Director','Plot','Released','Año']
    mensaje_error = 'No dispongo de información'
    estructura_peli = zip(lista_titulares, lista_claves)
    for item in estructura_peli:
        print(f'{item[0]}:{pelicula.get((item[1]),mensaje_error)}')

if __name__=='__main__':
    titulo = input("Título de la película:")
    parametros = {'apikey': KEY, 't': titulo}
    r = requests.get(URL, params=parametros)
    if r.status_code==200:#200 es el código OK de HTTP
        pelicula = r.json()
        #mostrar_pelicula(pelicula)
        mostrar_pelicula_guay(pelicula)
    elif r.status_code==401:#401 es el código error Unauthorized
        print("La KEY utilizada no es válida")
    else:
        print("Ha ocurrido un error HTTP:",r.status_code)