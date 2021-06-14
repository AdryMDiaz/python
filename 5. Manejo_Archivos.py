# -*- coding: utf-8 -*-
"""
Created on Sun May 30 17:38:19 2021

@author: Adry Diaz
"""
import sys

"""El director del Programa requiere poder generar una agenda 
con los datos de nombre y apellido, número de cédula y el número celular de todos los 
beneficiarios del proyecto, para poder hacerles algún seguimiento en su proceso de formación. 
Dicha agenda deberá ser almacenada en un archivo de texto en el directorio activo con el 
nombre agenda.txt. Cada beneficiario ocupará tres líneas en el archivo, una por cada campo 
(nombre y apellido, cedula, celular). Por ejemplo, el beneficiario José Castro con cédula 
18145321 y celular 3091234567 y la beneficiaria Sofía Vergara con cédula 52120318 y celular 
3109876543, quedarían así en el archivo:
    
José Castro
18145321
3091234567
Sofía Vergara
52120318
3109876543"""

#global datos
#datos = {}

"""Crear el archivo agenda.txt leyendo los datos desde el teclado (por lo menos 10 
beneficiarios)"""
"""Añadir un nuevo beneficiario en la agenda.txt, al final del archivo. No debe haber otro 
beneficiario con la misma cédula"""
def registrar():
    print("\n")
    msg = "*** REGISTRO BENEFICIARIOS ***"
    print(msg)
    print("-" * len(msg))
    espacio = "\n"
    #abrimos archivo txt para leer la información que se encuentra en él
    agenda = open("agenda.txt", "r")
    #convertimos lo que se encuentre en el archivo en una lista para evaluar cada posición
    contenido = agenda.readlines()
    try:
        cedula = input("Ingrese número de cédula: ")
    except ValueError:
        print("El valor ingresado no es correcto, por favor intente nuevamente")
        #recorremos la lista por medio de una estructura iterativa
    for i in contenido:
        #si el campo buscado se encuentra en la lista imprimimos el contenido de la posición en la que se encuentre
        if cedula in i:
            print("\nCedula {} ya se encuentra registrada en la base de datos, por favor valide nuevamente\n".format(i))
            pos=contenido.index(i)
            print("Nombre:", contenido[pos-1])
            print("Cédula:", contenido[pos])
            print("Celular:", contenido[pos+1])
            break
    #Si la cédula ingresada no se encuentra en el archivo, se pide por teclado cédula, nombre y telefono
    try:
        cedula = int(input("Ingrese número de cédula: "))
    except ValueError:
        print("El valor ingresado no es correcto, por favor intente nuevamente")
        sys.exit()
    #abrimos el archivo para ingresar información
    agenda = open("agenda.txt", "a")
    nombre = str(input("Ingrese nombre y apellido: ").title())
    try:
        telefono = int(input("Ingrese número de celular: "))
    except ValueError:
        print("El valor ingresado no es correcto, por favor intente nuevamente")
        sys.exit()
    #persona = {"nombre":nombre,"celular":telefono}
    #datos[cedula]=persona
    #escribimos en el archivo los datos ingresados por pantalla
    agenda.write("{}".format(nombre))
    agenda.write("{}".format(espacio))
    agenda.write("{}".format(cedula))
    agenda.write("{}".format(espacio))
    agenda.write("{}".format(telefono))
    agenda.write("{}".format(espacio))
    agenda.write("{}".format(espacio))
    agenda.close()

"""Mostrar en consola el listado completo de los beneficiarios del archivo agenda.txt.
"""
"""Mostrar en consola el listado de los beneficiarios cuyo nombre empieza por una letra 
determinada."""
def mostrar():
    print("\n")
    msg = "*** SUBMENÚ MOSTRAR ****"
    print(msg)
    print("-" * len(msg))
    print("1. Mostrar todos los registros\n2. Mostrar segun filtro\n3. Volver al menú anterior\n")
    opc = int(input("Ingrese su opcion: "))
        
    if opc == 1:
        print("\n")
        msg = "*** LISTADO COMPLETO DE BENEFICIARIOS ***"
        print(msg)
        print("-" * len(msg))
        #leemos el archivo
        agenda = open("agenda.txt","r")
        #almacenamos todo el contenido del archivo en una variable
        contenido = agenda.read()
        print(contenido)
        agenda.close()
    elif opc == 2:
        #leemos el archivo
        agenda = open("agenda.txt", "r")
        #utilizamos readlines para convertir el contenido del archivo en una lista
        contenido = agenda.readlines()
        #solicitamos el caracter a buscar y lo pasamos a mayúsculas para que coincida con la primera letra de cada nombre
        car = input("Ingrese caracter de búsqueda: ").upper()
        #recorremos todo el archivo
        for i in contenido:
            #si el caracter se encuentra en el archivo imprime el contenido de la posición.
            if car in i:
                print("\n")
                msg = "*** LISTADO DE BENEFICIARIOS ***"
                print(msg)
                print("-" * len(msg))
                pos = contenido.index(i)
                print("\nNombre:", contenido[pos])
                print("Cédula:", contenido[pos+1])
                print("Celular:", contenido[pos+2])
            agenda.close()

"""Buscar en el archivo agenda.txt el número celular de un beneficiario, dados su nombre 
y apellido"""                        
def buscar():
    print("\n")
    msg = "*** BÚSQUEDA BENEFICIARIOS ***"
    print(msg)
    print("-" * len(msg))
    print("*** Por favor ingrese nombre y apellido a buscar, la primera letra del nombre y apellido deben estar en mayúsculas. Ej: Pepito Perez\n")
    agenda = open("agenda.txt", "r")
    #si el campo buscado se encuentra en la lista imprimimos el contenido de la posición en la que se encuentre
    contenido = agenda.readlines()
    nombre = input("Ingrese nombre: ")
    for i in contenido:
        if nombre in i:
            pos = contenido.index(i)
            print("\n")
            msg = "*** LISTADO DE BENEFICIARIOS ***"
            print(msg)
            print("-" * len(msg))
            print("\nNombre:", contenido[pos])
            print("Cédula:", contenido[pos+1])
            print("Celular:", contenido[pos+2])
    agenda.close()

"""Borrar un beneficiario de la agenda.txt dado su número de cédula"""        
def eliminar():
    print("\n")
    msg = "*** ELIMINAR BENEFICIARIOS ***"
    print(msg)
    print("-" * len(msg))
    #abrimos el archivo en modo lectura y escritura
    agenda = open("agenda.txt", "r+")
    contenido = agenda.readlines()
    #Mueve el puntero hacia el byte indicado
    agenda.seek(0)
    try:
        cedula = input("Ingrese número de cédula que desea borrar: ")
        pos = contenido.index(cedula +"\n")
        nombre = contenido[pos-1]
        telefono = contenido[pos+1]
        resp = input("\nEsta seguro que desea eliminar al beneficiario con cedula {}. (s-->si, n-->no): ".format(cedula))
        if resp == "s":
            for i in contenido:
                if cedula not in i and nombre not in i and telefono not in i:
                    agenda.write(i)
            agenda.truncate()
            print ("\nLa cédula {} ha sido eliminada satisfactoriamente".format(cedula))
        elif resp == "n":
            opciones()
        else:
            print("\nLa opción digitada no es correcta, intente nuevamente")
    except ValueError:
        print("\nLa cédula ingresada no se encuentra en la base de datos, por favor valide nuevamente")
    agenda.close()

"""Presentar un menú con las diferentes opciones solicitadas para que el usuario pueda 
decidir qué proceso desea realizar"""		
def opciones ():
	print ("\n")
	msg = "*** MENÚ DE OPCIONES ***"
	print (msg)
	print ("-" * len (msg))
	opcmen = {1:"REGISTRAR", 2:"MOSTRAR", 3:"BUSCAR", 4:"ELIMINAR", 5:"SALIR"}
	for op, opm in opcmen.items():
		print("{}. {}".format(op, opm))
		
def Menu ():
    op = 0        
    while op != 5:
        opciones()
        op = int(input("\nDigite su opcion [1..5] -> "))
        if op in range(1,6):
            if op == 1:
                registrar()
            elif op == 2:
                mostrar()
            elif op == 3:
                buscar()
            elif op == 4:
                eliminar()
            else:
                print ("\n*** Gracias ***")
        else:
            print ("\nOpcion no valida")
			
Menu()
