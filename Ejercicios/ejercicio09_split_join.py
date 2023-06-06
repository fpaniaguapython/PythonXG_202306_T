#SPLIT
titulo = "El regreso de la momia"
palabras = titulo.split()#El separador por defecto es el espacio
print(palabras)#['El', 'regreso', 'de', 'la', 'momia']

ticket = "2023$06$06$19$14"
partes = ticket.split("$")
print(partes)

ticket = "2021$-01$-08$-10$-12"
partes = ticket.split("$-")
print(partes)

#JOIN
lista_inicial = ['2023', '06', '06', '19', '14']
separador = "@@"
trama = separador.join(lista_inicial)
print(trama)