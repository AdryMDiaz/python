def registro():
    database = open("database.txt","a")
    print ("\n*** REGISTRO DE BENEFICIARIOS ***\n")
    cedula = int(input("Ingrese número de cédula: "))
    database.write(str(cedula))
    nombre = input("Ingrese nombres y apellidos: ")
    database.write(nombre)
    telefono = int(input("Ingrese número de celular: "))
    database.write(str(telefono))
    datos = "Nombre: " + nombre.upper() + "\nCedula: " + str(cedula) + "\nCelular: " + str(telefono)
    #database.write("{}\n{}\n{}\n\n".format(nombre.upper(), cedula, telefono))
    return datos

def mostrar():
    print("\n*** LISTADO DE BENEFICIARIOS ***\n")
    database = open("database.txt", "r")
    contenido = database.read()
    print(contenido)
    database.close()

def buscar():
    print("*** BUSQUEDA BENEFICIARIOS ***")
    dato = input("\nIngrese la cédula a buscar: " + "\n")
    database = open("database.txt", "r")
    contenido = database.readlines()
    for i in contenido:
        if dato == i:
            print(i, end = "")
        print(i, end = "")
    print(i, end = "")
        #contenido.close()

def opciones ():
	print ("\n")
	msg = "*** Menú de Opciones ***"
	print (msg)
	print ("-" * len (msg))
	opcmen = {1:"Registrar", 2:"Mostrar", 3:"Buscar", 4:"Eliminar", 5:"Salir"}
	for op, opm in opcmen.items():
		print("{}. {}".format(op, opm))
		
def Menu ():
	op = 0	
	while op != 5:
		opciones()
		op = int(input("\nDigite su opcion [1..5] -> "))
		if op in range(1,6):
			if op == 1:
				registro()
			elif op == 2:
				mostrar()
			elif op == 3:
				buscar()
			#elif op == 4:
				#eliminarBeneficiario()
			else:
				print ("*** Gracias ***")
		else:
			print ("Opcion no valida")
			
Menu()
print (registro())