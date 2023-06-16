def astericador(f):
    def funcion_interna():
        print("******")
        f()
        print("******")
    return funcion_interna

@astericador
def saludar():
    print("Hola")

saludar()