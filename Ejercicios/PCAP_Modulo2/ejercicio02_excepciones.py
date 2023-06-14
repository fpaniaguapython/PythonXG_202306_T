'''
OJO:RESUMEN

NO SON CONCRETAS:
BaseException
Exception
ArithmeticError
LookupError
ValueError

CONCRETAS:
FloatingPointError*
ZeroDivisionError
IndexError
KeyError
TypeError
'''

lista = [1,2,3,4]

#Forma más sencilla de try-except
try:
    lista[10]
    print("OK")
except:
    print("KO")

#try-excep con tipos de error
try:
    lista[10]
    print("OK")
except IndexError:
    print("KO, IndexError")


try:
    r = 10/0
    lista[10]
    print("OK")
except IndexError:
    print("KO, IndexError")
except ZeroDivisionError:
    print("KO, error aritmético")


try:
    r = 10/0
    lista[10]
    print("OK")
except IndexError:
    print("KO, IndexError")
except ZeroDivisionError:
    print("KO, error aritmético")
except:
    print("KO, pero no sé qué ha pasado")


#try-except-finally
try:
    lista[0]
    print("OK-En el ejemplo del finally")
except IndexError:
    print("KO-En el ejemplo del finally")
finally:
    print("En el finally")


#try-except-else
try:
    lista[10]
    print("OK-En el ejemplo del else")
except IndexError:
    print("KO-En el ejemplo del else")
else:
    print("Se ejecuta si no ha habido ningún error")


#try-except-else-finally
try:
    lista[10]
    print("OK-En el ejemplo del else-finally")
except IndexError:
    print("KO-En el ejemplo del else-finally")
else:
    print("Se ejecuta si no ha habido ningún error")
finally:
    print("En el finally")


#Ejermplo de try-except con alias
try:
    print(1)
    lista[10]
    print(2)
except IndexError as ie:
    print(ie)
finally:
    print("Vamos al descanso")






try:
    a=1
except ValueError as x:
    pass
except IndexError as x:
    pass
except (ArithmeticError, FileExistsError) as x:
    pass

