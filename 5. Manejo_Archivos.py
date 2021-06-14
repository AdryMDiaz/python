# -*- coding: utf-8 -*-
"""
Created on Sun May 30 17:38:19 2021

@author: Adry Diaz
"""
import sys

"""El director requiere poder generar una agenda 
con los datos de nombre y apellido, número de cédula y el número celular de todos los 
beneficiarios del proyecto, para poder hacerles algún seguimiento en su proceso de formación. 
Dicha agenda deberá ser almacenada en un archivo de texto en el directorio activo con el 
nombre agenda.txt. Cada beneficiario ocupará tres líneas en el archivo, una por cada campo 
(nombre y apellido, cedula, celular)."""

"""Crear el archivo agenda.txt leyendo los datos desde el teclado (por lo menos 10 
beneficiarios)"""
"""Añadir un nuevo beneficiario en la agenda.txt, al final del archivo. No debe haber otro 
beneficiario con la misma cédula"""
def agregar():
    espacio = "\n"
        
    msg = "\n*** INGRESO BENEFICIARIO ***"
    print(msg)
    print("-" * len(msg))
    #Leer el archivo para validar si la cédula ingresada ya existe
    agenda = open("agenda.txt", "r")
    #Convertir el contenido del archivo en lista para facilitar su recorrido, lectura e impresión
    contenido = agenda.readlines()
    #Excepción de error por si el cliente ingresa un caracter es vez de un valor entero
    try:
        cedula = input("Ingrese número de cédula: ")
        #Si el valor ingresado es un caracater en vez de un entero, el programa finalizará
    except ValueError:
        print("El valor ingresado no es correcto, por favor intente nuevamente")
        sys.exit()
        #Se recorre la lista por medio de una estructura iterativa (for)
    for i in contenido:
        #Si el campo buscado se encuentra en la lista imprimimos el contenido de la posición en la que se encuentre
        if cedula in i:
            print("\nCedula {}ya se encuentra registrada en la base de datos, por favor valide nuevamente\n".format(i))
            #Ubicar por medio del método index la posición del valor buscado
            pos=contenido.index(i)
            #Se imprime el valor de la posición -1, 0 y +1 según el valor buscado y se romperá el ciclo
            print("Nombre:", contenido[pos-1])
            print("Cédula:", contenido[pos])
            print("Celular:", contenido[pos+1])
            break
    #Si la cédula ingresada no se encuentra en el archivo, se pide por teclado cédula, nombre y telefono
    #Excepción de error por si el cliente ingresa un caracter es vez de un valor entero
    try:
        cedula = int(input("Ingrese número de cédula: "))
        #Si el valor ingresado es un caracater en vez de un entero, el programa finalizará
    except ValueError:
        print("\n¡¡El valor ingresado no es correcto, por favor intente nuevamente!!")
        sys.exit()
    #Abrimos el archivo para ingresar información por medio del método "a"
    agenda = open("agenda.txt", "a")
    #Convertimos la primera letra de cada palabra ingresada en mayúsculas por si el usuario ingresa todo en minúsculas
    nombre = str(input("Ingrese nombre y apellido: ").title())
    #Excepción de error por si el cliente ingresa un caracter es vez de un valor entero
    try:
        telefono = int(input("Ingrese número de celular: "))
        #Si el valor ingresado es un caracater en vez de un entero, el programa finalizará
    except ValueError:
        print("\n¡¡El valor ingresado no es correcto, por favor intente nuevamente!!")
        sys.exit()
    #Escribir en el archivo los datos ingresados por pantalla
    agenda.write("{}".format(nombre))
    agenda.write("{}".format(espacio))
    agenda.write("{}".format(cedula))
    agenda.write("{}".format(espacio))
    agenda.write("{}".format(telefono))
    agenda.write("{}".format(espacio))
    agenda.write("{}".format(espacio))
    #Cerrar el archivo para que pueda ser utilizado nuevamente
    agenda.close()

"""Mostrar en consola el listado completo de los beneficiarios del archivo agenda.txt.
"""
def listado():
    msg = "\n*** LISTADO COMPLETO DE BENEFICIARIOS ***"
    print(msg)
    print("-" * len(msg))
    #Leer el archivo por medio de "r"
    agenda = open("agenda.txt","r")
    #Almacenar el contenido del archivo en una variable a través de read()
    contenido = agenda.read()
    #Imprimir contenido del archivo
    print(contenido)
    #Cerrar el archivo para que pueda ser utilizado nuevamente
    agenda.close()
    
"""Mostrar en consola el listado de los beneficiarios cuyo nombre empieza por una letra 
determinada."""
def filtrado():
    msg = "\n*** LISTADO FILTRADO DE BENEFICIARIOS ***"
    print(msg)
    print("-" * len(msg))
    #Leer el archivo por medio de "r"
    agenda = open("agenda.txt", "r")
    #Convertir el contenido del archivo en lista para facilitar su recorrido, lectura e impresión
    contenido = agenda.readlines()
    #Solicitar por teclado un caracter el cual se convertirá en mayúsculas para que solo coincida con la primera letra de cada palabra
    car = input("Digite la letra por la que empiezan los beneficiarios: ").upper()
    #Se recorre la lista por medio de una estructura iterativa (for)
    for i in contenido:
        #Si el caracter buscado se encuentra en la lista imprimimos el contenido de la posición en la que se encuentre
        if car in i:
            #Ubicar por medio del método index la posición del caracter buscado
            pos = contenido.index(i)
            #Se imprime el valor de la posición -1, 0 y +1 según el valor buscado
            print("\nNombre:", contenido[pos])
            print("Cédula:", contenido[pos+1])
            print("Celular:", contenido[pos+2])
        #Cerrar el archivo para que pueda ser utilizado nuevamente
        agenda.close()

"""Buscar en el archivo agenda.txt el número celular de un beneficiario, dados su nombre 
y apellido"""                        
def buscar():
    msg = "\n*** BÚSQUEDA DE BENEFICIARIOS ***"
    print(msg)
    print("-" * len(msg))
    #Leer el archivo por medio de "r"
    agenda = open("agenda.txt", "r")
    #Convertir el contenido del archivo en lista para facilitar su recorrido, lectura e impresión
    contenido = agenda.readlines()
    #Solicitar por teclado el nombre y apellido a buscar, convertimos la primera letra en mayúscula, por si el usuario ingrea todo en minúsculas
    nombre = input("Digite el nombre y apellido del beneficiario a buscar: ").little()
    #Se recorre la lista por medio de una estructura iterativa (for)
    for i in contenido:
        #Si el nombre buscado se encuentra en la lista imprimimos el contenido de la posición en la que se encuentre
        if nombre in i:
            #Ubicar por medio del método index la posición del caracter buscado
            pos = contenido.index(i)
            #Se imprime el valor de la posición -1, 0 y +1 según el valor buscado
            print("\nNombre:", contenido[pos])
            print("Cédula:", contenido[pos+1])
            print("Celular:", contenido[pos+2])
    #Cerrar el archivo para que pueda ser utilizado nuevamente
    agenda.close()

"""Borrar un beneficiario de la agenda.txt dado su número de cédula"""        
def eliminar():
    msg = "*** ELIMINAR BENEFICIARIOS ***"
    print(msg)
    print("-" * len(msg))
    #Abrir el archivo en modo lectura y escritura
    agenda = open("agenda.txt", "r+")
    #Convertir el contenido del archivo en lista para facilitar su recorrido, lectura e impresión
    contenido = agenda.readlines()
    #Mueve el puntero hacia el byte indicado
    agenda.seek(0)
    #Excepción de error por si el cliente ingresa una cédula que no existe dentro del archivo
    try:
        cedula = input("Ingrese número de cédula que desea borrar: ")
        #Ubicar por medio del método index la posición del caracter buscado se adiciona "\n" porque aunque en el archivo no se ven los espacios, hacen parte del texto
        pos = contenido.index(cedula +"\n")
        #Ubicar nombre y telefono de la cédula buscada
        nombre = contenido[pos-1]
        telefono = contenido[pos+1]
        #Confirmar si el usuario desea o no borrar el registro
        resp = input("\nEsta seguro que desea eliminar al beneficiario con cedula {}. (s-->si, n-->no): ".format(cedula))
        #Si la respuesta es "s"
        if resp == "s":
            #Se recorre la lista por medio de una estructura iterativa (for)
            for i in contenido:
                #Si la cédula, nombre y telefono buscado NO se encuentran en la lista
                if cedula not in i and nombre not in i and telefono not in i:
                    #Se imprime cada registro del archivo que NO coincida con lo que estamos buscando
                    agenda.write(i)
            #Eliminamos los registros que SI coincidan con lo que estamos buscanco
            agenda.truncate()
            print ("\n¡¡La cédula {} ha sido eliminada satisfactoriamente!!".format(cedula))
            #Si la respuesta es "n" se retornará al menú de opciones inicial
        elif resp == "n":
            opciones()
        else:
            #Si la opción no es ni "s" ni "n" se le indicará al usuario
            print("\n¡¡La opción digitada no es correcta, intente nuevamente!!")
    #Si la cédula no se encuentra en el archivo
    except ValueError:
        print("\n¡¡La cédula ingresada no se encuentra en la base de datos, por favor valide nuevamente!!\n")
    #Cerrar el archivo para que pueda ser utilizado nuevamente
    agenda.close()

"""Presentar un menú con las diferentes opciones solicitadas para que el usuario pueda 
decidir qué proceso desea realizar"""		
def opciones ():
    msg = "\n*** MENU PRINCIPAL ***"
    print(msg)
    print("-" * len(msg))
    #Se utiliza un diccionario para crear el menú usuando clave:argumento ej: 1:opcion
    opcmen = {1:"VER LISTADO COMPLETO", 2:"VER LISTADO FILTRADO", 3:"AGREGAR BENEFICIARIO", 4:"BUSCAR BENEFICIARIO", 5:"BORRAR BENEFICIARIO", 6:"SALIR"}
    for op, opm in opcmen.items():
        print("{}. {}".format(op, opm))
		
def Menu ():
    op = 0        
    while op != 6:
        opciones()
        op = int(input("Digite su opcion [1..6] -> "))
        if op in range(1,7):
            if op == 1:
                listado()
            elif op == 2:
                filtrado()
            elif op == 3:
                agregar()
            elif op == 4:
                buscar()
            elif op == 5:
                eliminar()
            elif op == 6:
                print ("\n*** ¡¡Hasta Pronto!! ***")
        else:
            print ("\nOpcion no valida")
			
Menu()
