#!/usr/bin/env python3

import sys

print(sys.path) #Path 'original'

sys.path.append('F:/borrar')#Modificando el path

print(sys.path) #Path 'modificado'

import fernando 
fernando.saludar()

sys.path.append('F:/borrar/funciones_comprimidas.zip')#Path 'modificado' de nuevo

print(sys.path) #Path 'modificado'

import funciones

funciones.f1()

