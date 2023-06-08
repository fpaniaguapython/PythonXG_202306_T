import random

numero_secreto = random.randint(1,6)
print(numero_secreto)
#Pedir al usuario un número hasta que adivine cuál es el número secreto.
#Utilizar while
#Sólo dispone de 3 intentos
INTENTOS_MAXIMOS = 3
numero = int(input("Dame otro numero:"))
intentos=1
while (numero != numero_secreto):
    print("No has acertado")
    if intentos==INTENTOS_MAXIMOS:
         print("Eres un fraude como adivino")
         break
    numero = int(input("Dame otro numero:"))
    intentos+=1
else:
     print("Muy bien, has acertado el número secreto")
