MODO_DEBUG = True

def log(f):
    def funcion_interna():
        if MODO_DEBUG:
            print("Ejecutando la función:", f.__name__)
        f()
    return funcion_interna

@log
def saludar():
    print("Hola")

@log
def despedir():
    print("Adios")

saludar()
despedir()