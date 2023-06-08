#Ejecutar previamente: pip install gTTS

from gtts import gTTS
import os

#Configuración 
language = 'es'
acento = 'es'#Ver más acentos en https://gtts.readthedocs.io/en/latest/module.html#localized-accents

nombre = input("Introduce tu nombre:")
genero = input("Introduce tu género (H/M/O):")
if genero=="H":
    mytext = f"Hola {nombre}, eres mi amo y señor y te obedeceré en todo lo que quieras"
elif genero=="M":
    mytext = f"Hola {nombre}, eres mi ama y señora y te obedeceré en todo lo que quieras"
else:
    mytext = f"Hola {nombre}, eres mi am@ y señ@r@ y te obedeceré en todo lo que quieras"

myobj = gTTS(text=mytext, lang=language, tld=acento, slow=False)
myobj.save("locucion.mp3")
os.system("start locucion.mp3")#No funciona en Linux

