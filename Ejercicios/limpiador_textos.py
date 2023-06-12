def limpiar_texto(texto, str_letras_a_eliminar, caracter_sustitucion):
    for letra in str_letras_a_eliminar:
        texto = texto.replace(letra, caracter_sustitucion)
    return texto

if __name__=='__main__':
    print("LIMPIADOR TEXTOS")
    nombre_fichero = "sp$ide/rman:2020*.jpg"#sp-ide-rman-2020-.jpg
    nombre_fichero = limpiar_texto(nombre_fichero, ":ñ/$*", "-")
    print(nombre_fichero)