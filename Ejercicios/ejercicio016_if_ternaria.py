#Notación 'normal'
edad = 35
if edad>40:
    salario = 20_000
else:
    salario = 18_000

#Notación 'ternaria'
edad = 35
salario = 20_000 if edad>40 else 18_000

#Notación 'normal'
nombre = "Atlántico"
#Asignar el valor a tipo
#Si el nombre es Atlántico tipo es 'Océano', de lo contrario el tipo es 'Mar'
tipo = "Océano" if nombre == "Atlántico" else "Mar"
print(tipo)