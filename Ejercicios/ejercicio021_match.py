#0: OK; 1: EN MARCHA; 2: PARADO; 3: AVERIADO
estado = 3

match estado:
    case 0:
        print("OK")
    case 1:
        print("EN MARCHA")
    case 2:
        print("PARADO")
    case 3:
        print("AVERIADO")
    case _:#case other:
        print("DESCONOCIDO")

#FERNANDO: 46; JUAN: 58; TAMARA: 25; AMALIA: 35
nombre = input("Introduce un nombre:")

match nombre.upper():
    case "FERNANDO":
        print(46)
    case "JUAN":
        print(58)
    case "TAMARA":
        print(25)
    case "AMALIA":
        print(35)
    case other:
        print("Desconocido")