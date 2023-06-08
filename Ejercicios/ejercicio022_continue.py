#Sabe Japonés; Movilidad; 24x7; Python 
fina = ("Fina", False, True, False, 0.4)
fernando = ("Fernando", True, True, False, 0.4)
daniel_sama = ("Daniel", True, True, True, 1)
florian = ("Florián", True, True, True, 0.8)

candidatos = (fina, fernando, daniel_sama, florian)

for candidato in candidatos:
    print(f"Evaluando Japonés de {candidato[0]}")
    if candidato[1]==False:
        continue #Cuando una condición no se cumple, pasa al siguiente elemento de la tupla
    print(f"Evaluando Movilidad de {candidato[0]}")
    if candidato[2]==False:
        continue
    print(f"Evaluando 24x7 de {candidato[0]}")
    if candidato[3]==False:
        continue
    print(f"Evaluando Python de {candidato[0]}")
    if candidato[4]<0.5:
        continue
    print(f"Candidato {candidato[0]} aceptado")
    break #Una vez encontrado un candidato, deja de evaluar al resto