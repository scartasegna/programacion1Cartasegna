#!/usr/bin/python3
#coding: utf-8

#El imput se hace que se pida ingreso del usuario
import random
import sys

def crearNumeroSecreto(inicio,fin):
    ran = random.randrange(inicio,fin)
    
    return ran

#Elegimos un numero secreto
inicio = input("Inicio del rango:")
fin = input("Fin del rango:")

try:
    inicioInt = int(inicio)
    finInt = int(fin)
except ValueError:
    print("El inicio y fin  del rango debe ser enteros")
    sys.exit()
    

numeroSecreto = crearNumeroSecreto(inicioInt,finInt)
adivino = False
intentos = 0
errorNumero = 0
while (not adivino):    
    try:
        eleccion = input("Elija un numero entre {} y {}: ".format(inicio,fin))
        intentos += 1
        eleccionInt = int(eleccion)
        if eleccionInt < numeroSecreto:
            print("Menor")
        elif eleccionInt > numeroSecreto:
            print("Mayor")
        else:
            adivino = True
    except ValueError:
          print("El numero a adivinar debe ser un entero")
          errorNumero += 1
    if errorNumero == 10:
        break
    
if errorNumero < 1:
    print("Adivinaste el numero secreto {} en {} intentos".format(numeroSecreto,intentos))
else:
    print("Fin ejecucion por error en eleccion de numero (10 veces)")

