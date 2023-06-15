class NombreCortoError(ValueError):
    pass

def validar(nombre):
    if len(nombre)<10:
        raise NombreCortoError("El nombre es demasiado corto")
    return True

try:
    validar("Ramón")
except NombreCortoError as ve:
    print("Error:",ve.args)#ve.args tiene una tupla con información sobre la excepción