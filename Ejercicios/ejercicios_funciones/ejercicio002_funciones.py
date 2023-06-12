#Función sin parámetros ni retorno
def saludar():
    print("Hola")

saludar()

#Función con parámetros y sin retorno
def escribir_numero(numero):
    print(numero)

escribir_numero(5)
escribir_numero(numero=5)

#Función sin parámetros y con retorno
def dime_la_hora():
    return '17:41'

resultado = dime_la_hora()
print(resultado)

#Función con parámetros y con retorno
def calcular_el_doble(numero : int) -> int:
    return numero*2

resultado = calcular_el_doble(4)
resultado = calcular_el_doble(numero=4)
resultado = calcular_el_doble("Palabra") #Funciona, ya que el tipo es una sugerencia
print(resultado)


#Funciones con varios parámetros
def escribir_numero_coloreado(numero, color):
    pass

escribir_numero_coloreado(3,'Verde')#Argumentos posicionales
escribir_numero_coloreado(numero=3,color='Verde')#Argumentos nominales
escribir_numero_coloreado(color='Verde',numero=3)#Argumentos nominales

def calcular_trayectoria(longitud, radio, masa, potencia, 
                         angulo_inclinacion, direccion_viento):
    pass

calcular_trayectoria(1000, 50, 30, 1200, 32, 18.19)
calcular_trayectoria(longitud=1000, radio=50, masa=30, potencia=1200, 
                     angulo_inclinacion=32, direccion_viento=18.19)

#Funciones con varios parámetros
def escribir_texto_coloreado(texto, color='Rojo'):
    print(f'{texto} en color {color}')

escribir_texto_coloreado("Película")
escribir_texto_coloreado("Película", "Verde")


def escribir_texto_coloreado(texto="Texto genérico", color='Rojo'):
    print(f'{texto} en color {color}')

escribir_texto_coloreado()
escribir_texto_coloreado("Película")
escribir_texto_coloreado("Película", "Verde")


#def escribir_texto_coloreado(texto="Texto genérico", color):#ERROR

def escribir_coloreado_formateado(texto, color='Rojo', formato='negrita'):
    pass

escribir_coloreado_formateado("Margarita")
escribir_coloreado_formateado("Margarita","Verde")#Tendría el mismo efecto que la línea siguiente
escribir_coloreado_formateado("Margarita",color="Verde")
escribir_coloreado_formateado("Margarita",color="Verde",formato='cursiva')
escribir_coloreado_formateado("Margarita",formato='cursiva',color="Verde")
escribir_coloreado_formateado("Margarita",formato='cursiva')
escribir_coloreado_formateado(formato = 'cursiva', texto="Margarita")

#*datos es una tupla que admite un número indeterminado de parámetros separados por coma 
def mostrar_datos(*datos):
    print(type(datos))
    print(datos)

mostrar_datos(3)
mostrar_datos(3,8)
mostrar_datos(3,8,"Amalia")
mostrar_datos(3,8,"Amalia","Aurelio",True)

def mostrar_datos(*datos, factor):
    print(type(datos))
    print(datos)

mostrar_datos(3,4,factor=5)

#**El nombre 'kwargs' (podría ser cualquier otro, kwargs es una convención) recibe un diccionario
def calcular_valores(**kwargs):
    print(type(kwargs))
    print(kwargs)

calcular_valores(nombre="Fernando",rol='Instructor',altura=170)

def calcular_valores(configuracion, **kwargs):
    print(type(kwargs))
    print(kwargs)

calcular_valores(configuracion="Estricta", nombre="Fernando",rol='Instructor',altura=170)



#Retorno múltiple
def calcular_el_doble_y_el_tiple(numero):
    doble = numero * 2
    triple = numero * 3
    return doble, triple #Devuelve una tupla

resultado = calcular_el_doble_y_el_tiple(3)
print(resultado)