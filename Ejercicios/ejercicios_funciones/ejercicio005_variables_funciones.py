def dame_numero():
    return 11

resultado = dame_numero()
print(resultado)#11

resultado = dame_numero
print(resultado)#<function dame_numero at 0x00000162C5BCA020>
x = resultado()
print(x)


def saludador_ingles():
    return 'hello'

def saludador_castellano():
    return 'hola'


def get_generador_saludo(idioma):
    if idioma=='ingles':
        return saludador_ingles
    else:
        return saludador_castellano
    

saludador = get_generador_saludo('castellano')#Proporciona la función 'saludador_castellano'
print(saludador())#hola

saludador = get_generador_saludo('castellano')#Proporciona la función 'saludador_ingles'
print(saludador())#hello