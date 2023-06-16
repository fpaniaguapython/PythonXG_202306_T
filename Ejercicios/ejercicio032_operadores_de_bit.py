'''
Operadores de bit
& -> and
| -> or
^ -> xor - or exclusivo
'''
#10 - '0b1010'
#13 - '0b1101'

print(10 & 13)#8  - '0b1000'
print(10 | 13)#15 - '0b1111'
print(10 ^ 13)#7  - '0b0111'

def Verdadero():
    print("Verdadero")
    return True

def Falso():
    print("Falso")
    return False

#print(Verdadero() and Falso())#Verdadero,Falso - False
#print(Falso() and Verdadero())#Falso - False
#print(Falso() & Verdadero())#Falso,Verdadero - False

#print(Verdadero() or Falso())#Verdadero - True
#print(Verdadero() | Falso())#Verdadero,Falso - True

#print(Verdadero() ^ Verdadero())#Verdadero,Verdadero - False
#print(Verdadero() ^ Falso())#Verdadero,Falso - True

#Cada bit significa el estado de un conmutador 
#estado = 0b00101#Estado 3 en ON
estado = 0b01001#Estado 3 en OFF
mascara_estado_3 = 0b00100
estado3 =  estado & mascara_estado_3
if estado3==0:
    print("Estado 3 está en OFF")

#DESPLAZAMIENTO DE BITS
print(8>>1)#Desplazamiento de una posición hacia la derecha -> División entre 2
print(8>>2)#Desplazamiento de dos posiciones hacia la derecha -> División entre 4
print(8<<1)#Desplazamiento de una posición hacia la izquierda -> Multiplicando por 2
print(8<<2)#Desplazamiento de dos posiciones hacia la izquierda -> Multiplicando por 4





