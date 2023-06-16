def x():
    raise Exception("Mensaje del error","Segundo mensaje", 3)

try:
    x()
except Exception as ex:
    #Contiene una tupla con los parámetros enviados al constructor de la exception
    print(ex.args)#('Mensaje del error', 'Segundo mensaje', 3)
