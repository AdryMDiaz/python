# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 19:49:30 2021

@author: Adry Diaz
"""

"""Dos empresas productoras de elementos para el hogar se encuentran en una 
competenciapara ver cual es la más productiva. La primera empresa es Acme la
segunda es IndustriasWayne. Estás empresas tienen robots que reciben los
materiales en bandas transportadoras. Sin embargo, el manejo y programación de
la línea de producción es lo importante. La empresa más productiva le dará un
bono a sus empleados. En el concurso se va a generar una secuencia de
caracteres las cuales indicaran lo siguiente A o W dependiendo cuál lleve la
delantera en puntaje y E si van empatadas. Es decir, si Acme va ganando se
imprime una A por el contrario se impirme una W. Si van empatadas se imprime E.
Se debe contabilizar cual empresa va a la delantera de acuerdo a la solicitud
de un número variable de productos"""

"""set de datos:
    Acme: ROYITQ
    Wayne: TPIURY
    consurso: RPQUUOOTYTUURQYPQ"""

pc = []
ca = []
cw = []

#Inicializar variables
cont_a = 0
cont_w = 0
seguir = True
#Solicitar información por teclado
acme = str(input("Ingrese los productos de Acme: ")).upper()
wayne = str(input("Ingrese los productos de Wayne: ").upper())
concurso = str(input("Ingrese los productos solicitados por el concurso: ").upper())
#convertir las cadenas ingresadas en lista para hacer su recorrido más fácil
pa = list(acme)
pw = list(wayne)
co = list(concurso)
"""Se recorre la lista del concurso posición por posición y cada posición se
almacena en una variable para compararl contra las listas de cada industria"""
for i in co:
    pos = co.index(i)
    c = co[pos]
    """Recorre cada lista de productos de Acme evaluando si c está en esa lista,
    si está, activará el contador y añadirá ese resultado a otra lista que
    permitirá evaluar cual empresa va ganando"""
    for i in pa:
        if c in i:
            cont_a =+ 1
            ca.append(cont_a)
    """Recorre cada lista de productos de Wayne evaluando si c está en esa 
    lista, si está, activará el contador y añadirá ese resultado a otra
    lista que permitirá evaluar cual empresa va ganando"""
    for j in pw:
        if c in j:
            cont_w =+ 1
            cw.append(cont_w)
    """Por medio de una condicional se evalúa el tamaño de ambas listas
        generadas anteriormente, si Acme va ganando se asigna una A, si Wayne
        va ganando se asinga una W y si ambas van empatadas se asigna una E"""        
    if len(ca) > len(cw):
        sal = "A"
    elif len(ca) < len(cw):
        sal = "W"
    else:
        sal = "E"
    #Se adiciona cada resultado a una lista final que guarta el resultado
    pc.append(sal)
    #Se convierte la lista en cadena
    strpc ="".join(pc)
print(strpc)