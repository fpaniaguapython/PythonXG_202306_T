#Numéricos
edad = 41 #Entero, base decimal
altura = 1.72 #Float, base decimal

numero_octal = 0o12347 #Octal, entero
numero_hexadecimal = 0x34DF1 #Hexadecimal, entero
numero_binario = 0b10101 #Binario, entero

numeros_con_decimales = 1.72 #Float
numeros_con_decimales = 1. #Float
numeros_con_decimales = .72 #Float
numeros_con_decimales = 5e3 #Float
numeros_con_decimales = 5E3 #Float
numeros_con_decimales = 5e-3 #Float

#Otros tipos
logico = True #True(1) o False(0)
cadena = "Cadena de caracteres" #str

#Conversión de tipos:
#float(), int(), str() y bool()
print(float(3))#3.0
print(str(3))#'3'
print(bool(1))#True
print(bool(3))#True
print(bool(0))#False
print(bool(-2))#True

print(str(3.5))#'3.5'
print(int(3.8))#3 (elimina los decimales)
print(bool(3.8))#True

print(int(True))#1
print(float(False))#0.0
print(str(True))#'True'

print(int("3"))#3
#print(int("t"))#Error
#print(int("0xFF1100"))#Error
#print(int("Tres"))#Error
#print(int("3.4"))#Error
print(float("3.4"))#3.4







