# -*- coding: utf-8 -*-
"""
Created on Sat May 15 10:01:37 2021

@author: Adry Diaz
"""

#En una de sus salidas de campo, ha registrado un par de temperaturas diarias (máxima, mínima) para todos los días que 
#permanecieron en campo. Dadas las condiciones del terreno donde se encontraban, no era 
#posible tener temperaturas menores de 5 grados ni mayores de 35 grados, que se consideraron 
#errores, pero igual se registraron para su estudio posterior. La pareja de temperaturas (0,0) 
#indicará que se han terminado los datos de la salida de campo.

import sys
            
print ("=======================================")
print ("==SISTEMA DE REGISTRO DE TEMPERATURAS==")
print ("============SALIDA DE CAMPO============")
print ("=======================================")

print ("\x1b[1;31m" + "\n***Importante***" + "\x1b[0m")
print ("\x1b[1;31m" + "===================" + "\x1b[0m")
print ("Por favor relacione las temperaturas máximas y mínimas con sus respectivos días, registradas en la salida de campo")
print ("\x1b[1;33m" + "Para finalizar la relación de temperaturas por favor digite el valor cero (0) en temperatura máxima y temperatura mínima" + "\x1b[0m")

#Declarar listas de temperaturas máximas, mínimas, días
#Definir error mínimo y máximo de temperatura
temp_max = []
temp_min = []
dias = []
temp_error_min = float(5)
temp_error_max = float(35)

print ("\n============================")
print ("==REGISTRO DE TEMPERATURAS==")
print ("============================")
#Inicializar las listas hasta que en temp1 y en temp2 se registre cero (0)
#Por medio de una estructura iterativa leer desde el teclado todos los datos registrados en la salida de campo
while True:
    try:
        temp1 = float(input("Introduzca la temperatura máxima: "))
        temp2 = float(input("Introduzca la temperatura mínima: "))
        if temp2 > temp1:
            print ("La temperatura mínima es superior a la máxima, intente nuevamente")
            sys.exit()
        if temp1 != 0 or temp2 != 0:
            temp_max.append(temp1)
            temp_min.append(temp2)
            dias.append(int(input("Introduzca el número de día: ")))
        elif temp1 == 0 and temp2 == 0:
            fin = input("Desea finalizar el registro de temperaturas?" + "\x1b[1;31m" + " digite (s--> si, n--> no): " + "\x1b[0m")
            if fin == "s":
                break
            elif fin == "n":
                continue
            else:
                #Si el usuario digita una opción diferente a s-->si o n-->no
                print ("El valor ingresado no corresponde a las opciones válidas," + "\x1b[1;31m" + " por favor digite s--> si, n--> no" + "\x1b[0m" + ", por favor intente nuevamente")
                sys.exit()
    except ValueError:
        print ("El valor ingresado es incorrecto, intente nuevamente")
        sys.exit()                  
            
#Mostrar temperaturas relacionadas en pantalla
print ("\x1b[1;36m" + "\nTemperaturas registradas" + "\x1b[0m")
print ("\x1b[1;36m" + "========================" + "\x1b[0m")
for dia, temp1, temp2 in zip(dias, temp_max, temp_min):
    print ("Dia {}. temp_max: {} grados. temp_min: {} grados".format(dia, temp1, temp2))

#Mostrar en consola el número total de días que duró la salida de campo
total_dias = len(dias)
print ("\n==========================================================")
print ("Número total de días que duró la salida de campo: " + str(total_dias) + " día(s)")
print ("==========================================================")

#Mostrar en consola cuantos días en total se tuvieron temperaturas con error, de los cuales 
#se debe informar cuántos fueron por temperaturas menores de 5 grados, cuántos fueron 
#por temperaturas mayores de 35 grados y cuántos por ambos errores
print ("\x1b[1;36m" + "\nDías con temperaturas menores a 5 grados" + "\x1b[0m")
print ("\x1b[1;36m" + "========================================" + "\x1b[0m")
def total_min(temp2):
    count = 0
    for dia, temp2, temp1 in zip (dias, temp_min, temp_max):
        if temp2 < temp_error_min and temp1 < temp_error_max:
            count += 1
            print ("Dia {}. temp_min {} grados".format(dia, temp2))
    return count
print ("\nDías con temperaturas menores a 5 grados: ", total_min(temp2), " día(s)")
        
print ("\x1b[1;36m" + "\nDías con temperaturas mayores a 35 grados" + "\x1b[0m")
print ("\x1b[1;36m" + "=========================================" + "\x1b[0m")
def total_max(temp1):
    count = 0
    for dia, temp1, temp2 in zip (dias, temp_max, temp_min):
        if temp1 > temp_error_max and temp2 > temp_error_min:
            count += 1
            print ("Día {}. temp_max: {} grados".format(dia, temp1))
    return count
print ("\nDías con temperaturas mayores a 35 grados: ", total_max(temp1), " día(s)")
        
print ("\x1b[1;36m" + "\nDías con temperaturas menores a 5 grados y mayores a 35 grados" + "\x1b[0m")
print ("\x1b[1;36m" + "==============================================================" + "\x1b[0m")
def total_error(temp1, temp2):
    count = 0
    for dia, temp1, temp2 in zip (dias, temp_max, temp_min):
        if temp1 > temp_error_max and temp2 < temp_error_min:
            count += 1
            print ("Día {}. temp_max: {} grados. temp_min: {} grados".format(dia, temp1, temp2))
    return count
print ("\nDías con temperaturas menores a 5 grados y mayores a 35 grados: {} día(s)".format(total_error(temp1, temp2)))

print ("\x1b[1;36m" + "\nDías totales con temperaturas con error" + "\x1b[0m")
print ("\x1b[1;36m" + "=======================================" + "\x1b[0m")
def total_temp(temp1, temp2):
    count = 0
    for dia, temp1, temp2 in zip (dias, temp_max, temp_min):
        if temp1 > temp_error_max or temp2 < temp_error_min:
            count += 1
    return count
print ("Días totales con temperaturas menores a 5 grados y/o mayores a 35 grados: {} día(s)".format(total_temp(temp1, temp2)))

#Mostrar en consola la temperatura media mínima y máxima, sin tener en cuenta los días en que se reportaron errores
print ("\x1b[1;36m" + "\nDías Sin Errores" + "\x1b[0m")
print ("\x1b[1;36m" + "===========================================" + "\x1b[0m")
for dia, temp1, temp2, indice in zip(dias, temp_max, temp_min, range(0, total_dias)):
    if temp1 < temp_error_max and temp2 > temp_error_min:
        print ("Día {}. temp_max: {} grados. temp_min: {} grados.".format(dia, temp1, temp2))
        
print ("\x1b[1;36m" + "\nTemperatura media máxima" + "\x1b[0m")
print ("\x1b[1;36m" + "==========================" + "\x1b[0m")
def media_temp_max(temp1, temp2):
    temp_media_max = []
    count = 0
    for dia, temp1, temp2 in zip(dias, temp_max, temp_min):
        if temp1 < temp_error_max and temp2 > temp_error_min:
            temp_media_max.append(temp1)
            count += 1        
    return sum(temp_media_max)/float(len(temp_media_max))
if temp1 == 0 and temp2 == 0:
    print ("No se ingresaron datos, por favor valide nuevamente")
else:
    print("La temperatura media máxima fue de {} grados".format(media_temp_max(temp1, temp2)))

print ("\x1b[1;36m" + "\nTemperatura mínima mínima" + "\x1b[0m")
print ("\x1b[1;36m" + "==========================" + "\x1b[0m")
def media_temp_min(temp1, temp2):
    temp_media_min = []
    count = 0
    for dia, temp1, temp2 in zip(dias, temp_max, temp_min):
        if temp1 < temp_error_max and temp2 > temp_error_min:
            temp_media_min.append(temp2)
            count += 1
    return sum(temp_media_min)/float(len(temp_media_min))
if temp1 == 0 and temp2 == 0:
    print ("No se ingresaron datos, por favor valide nuevamente")
else:
    print("La temperatura media mínima fue de {} grados".format(media_temp_min(temp1, temp2)))

#Mostrar en consola el porcentaje de días que se reportaron errores respecto del total de días reportados
try:
    print ("\n==============================================================================")
    print ("Porcentaje de días con errores con respecto al total de días en campo: ", round(((total_temp(temp1, temp2) / total_dias) * 100),2), "%")
    print ("==============================================================================")
except ZeroDivisionError:
    print("No se ingresaron datos, por favor valide nuevamente")
