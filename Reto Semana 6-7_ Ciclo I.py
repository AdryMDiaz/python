# -*- coding: utf-8 -*-
"""
Created on Sun May 30 17:38:19 2021

@author: Adry Diaz
"""

global diccBeneficiario
diccBeneficiario = {}

def registrarBeneficiario():
    print("*** Registro de Beneficiarios ***")
    idBeneficiario = int(input("Ingrese número de cédula del beneficiario: "))
    nombreBeneficiario = input("Ingrese nombre y apellido del beneficiario: ")
    #celBeneficiario = int(input("Ingrese número de celular del beneficiario: "))
    diccBeneficiario[idBeneficiario] = nombreBeneficiario
    
def listarBeneficiario():
	print("*** Listado de Beneficiarios ****")
	for num, cli in diccBeneficiario.items():
		print ("{}\n{}".format(num, cli))
		
def buscarBeneficiario():
	print("*** Buscar Beneficiario ***")
	idB = int(input("Ingrese el número de cédula del beneficiario: "))
	if diccBeneficiario.get(idB, 0) == 0:
		print ("Beneficirio no existe en la base de datos")
	else:
		print ("{}\n{}".format(idB, diccBeneficiario[idB]))
        
def eliminarBeneficiario():
    idB = int(input("Ingrese el número de cédula del beneficiario que desea eliminar: "))
    if diccBeneficiario.pop(idB, 0) == 0:
        print ("Beneficiario no existe en la base de datos")
    else:
        print("Beneficiario eliminado de la base de datos")
        diccBeneficiario.update(diccBeneficiario)
		
def opciones ():
	print ("\n")
	msg = "*** Menú de Opciones ***"
	print (msg)
	print ("-" * len (msg))
	opcmen = {1:"Registrar Beneficiarios", 2:"Listar Beneficiarios", 3:"Buscar Beneficiarios", 4:"Eliminar Beneficiarios", 5:"Salir"}
	for op, opm in opcmen.items():
		print("{}. {}".format(op, opm))
		
def Menu ():
	op = 0	
	while op != 5:
		opciones()
		op = int(input("Digite su opcion [1..5] -> "))
		if op in range(1,6):
			if op == 1:
				registrarBeneficiario()
			elif op == 2:
				listarBeneficiario()
			elif op == 3:
				buscarBeneficiario()
			elif op == 4:
				eliminarBeneficiario()
			else:
				print ("*** Gracias ***")
		else:
			print ("Opcion no valida")
			
Menu()