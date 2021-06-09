# -*- coding: utf-8 -*-
"""
Created on Tue May  4 20:44:22 2021

@author: Adry Diaz
"""

"""El dueño de una tienda de artículos de ropa le ha solicitado a usted como programador, que le 
desarrolle un algoritmo que le permita calcular el valor a pagar de cada cliente que hace compras en su tienda

Hacer una prueba a lápiz del algoritmo para los dos siguientes casos:

Caso 1: el cliente compra 1 pantalón de hombre código 123 por valor de $45000, una 
camisa manga corta código 345 por valor de $35000 y por último una camiseta Polo 
código 456 por valor de $27000.

Caso 2: el cliente compra 3 camisetas cuello redondo por valor de $12000 cada una, 
2 pares de medias tobilleras por valor de $3000 cada par."""

valor, cant, total, contar = 0,0,0,0
seguir = True

print("*** BIENVENIDO A SU SISTEMA DE FACTURACION ***,\n")
print("*** Menú Inicial ***\n")
print ("*** Si el artículo NO posee código referencia, por favor digite 0 ***\n")

#Mediante una estructura iterativa establecemos un ciclo por cada referencia que se ingrese
while seguir:
    ref = int(input("Ingrese el código de referencia del artículo: "))
    #Mediante una estructura condicional evaluamos las referencias que se encuentren en stock
    if ref == 123:
        desc = print ("Pantalón de Hombre")
    elif ref == 345:
            desc = print("Camisa manga corta")
    elif ref == 456:
        desc = print("Camiseta tipo polo")
    elif ref == 0:
        desc = input("Ingrese la descripcion del artículo: ")
    else:
        print ("El código de referencia digitado no existe en el catálogo de artículos de la tienda, por favor verifique nuevamente")
        break            
    valor = int(input("Ingrese el valor del artículo: "))
    cant = int(input("Ingrese la cantidad comprada: "))
    subTotal = valor * cant
    total = total + subTotal
    contar = contar + 1
    print ("Desea facturar otro artículo: (s-si, n-no) ")
    resp = input()
    if resp == "n":
        seguir = False
        print ("El valor total a pagar por el cliente es: ", total)