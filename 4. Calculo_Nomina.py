# -*- coding: utf-8 -*-
"""
Created on Sat May 22 13:04:25 2021

@author: Adry Diaz
"""
"""
El departamento de Talento Humano, a raíz de la participación en 
un proyecto muy especial, requiere poder procesar la nómina de docentes contratados por 
horas. Para tal efecto ha establecido los siguientes lineamientos:
    - La nómina será procesada semanalmente, digitando por cada docente las horas 
    trabajadas en la semana y el valor establecido por hora.
    - A todos los docentes que trabajen más de 40 horas en la semana, se les reconocerán 
    como horas extras y se pagarán a un valor de 1,5 de la hora normal.
    - Al salario bruto obtenido en el punto anterior se le calculará el 9% para los parafiscales.
    - Para cada docente se le calcularán provisiones para prima de servicio 8.33%, cesantías
    8.33%, intereses de cesantía 1.0% y vacaciones 4.17%.
    - A cada uno se le descontará el aporte de 4% para salud y el 4% para pensión.
"""

names = []
hours = []
values = []
weeks = []

"""
Los cálculos de sueldo bruto, descuentos, sueldo neto y provisiones, deberán ser 
realizados a través de funciones o procedimientos y serán llamados en el programa 
principal
"""
def dctoParafiscal(salary):
    if salary == 0:
        return 0
    else:
        dctoParafiscales = round(salary * 0.09, 2)
        return dctoParafiscales
    
def dctoSalud(salary):
    if salary == 0:
        return 0
    else:
        dctoSalud = round(salary * 0.04, 2)
        return dctoSalud
    
def dctoPension(salary):
    if salary == 0:
        return 0
    else:
        dctoPension = round(salary * 0.04, 2)
        return dctoPension

def provPrima(salary):
    if salary == 0:
        return 0
    else:
        provPrima = round(salary * 0.0833, 2)
        return provPrima

def provCesantias(salary):
    if salary == 0:
        return 0
    else:
        provCesantias = round(salary * 0.0833, 2)
        return provCesantias

def provInt(salary):
    if salary == 0:
        return 0
    else:
        provInt = round(provCesantias * 0.01, 2)
        return provInt
    
def provVacaciones(salary):
    if salary == 0:
        return 0
    else:
        provVacaciones = round(salary * 0.0417, 2)
        return provVacaciones

def imprimir(name, hour, value, salary_n, extra, salary, week):
    print ("\x1b[1;34m" + "\nRELACION DE PAGOS. DOCENTE. {} SEMANA {}".format(name, week) + "\x1b[0m")
    print ("\x1b[1;34m" + "=============================================================" + "\x1b[0m")
    print ("\x1b[1;31m" + "Semana: {}".format(week) + "\x1b[0m" + "\nNombres y Apellidos: {} \nHoras Laboradas: {} \nValor Hora $: {}".format(name, hour, value) + "\x1b[1;31m" + "\nValor H. Normal $: {}:".format(salary_n) + "\nValor H. Extra $: {}:".format(extra) +"\nSalario Bruto $: {}:".format(salary) + "\x1b[0m")
    print ("Dcto Parafiscal $: {} \nDcto Salud $: {} \nDcto Pension $: {} \nTotal Dctos $: {}".format(dctoParafiscal(salary), dctoSalud(salary), dctoPension(salary), (dctoParafiscal(salary) + dctoSalud(salary) + dctoPension(salary))))
    print ("\x1b[1;31m" + "Salario Neto $: {}".format(salary-(dctoParafiscal(salary) + dctoSalud(salary) + dctoPension(salary)))+ "\x1b[0m")
    print ("Prima de Servicios $: {} \nCesantías $: {} \nInt. Cesantías $: {} \nVacaciones $: {}".format(provPrima(salary), provCesantias(salary), provInt(salary), provVacaciones(salary)))
    
def principal():
    #Leer desde el teclado los datos de nombre, horas trabajadas y valor hora, por cada 
    #docente del proyecto
    while True:
        name = input ("Ingrese el nombres y Apellidos del docente: ")
        if name != "*":
            weeks.append(int(input("Ingrese el número de semana laborada: ")))
            names.append(name.upper())
            hours.append(float(input("Ingrese el total de horas laboradas por el docente semana: ")))
            values.append(float(input("Ingrese el valor normal de la hora laborada semana: ")))
        if name == "*":
            break
    #A todos los docentes que trabajen más de 40 horas en la semana, se les reconocerán como horas extras y se pagarán a un valor de 1,5 de la hora normal
    for name, hour, value, week in zip(names, hours, values, weeks):
        if hour > 40:
            salary_n = (40 * value)
            extra = (hour-40) * (value * 1.5)
            salary = salary_n + extra
        else:
            salary_n = hour * value
            extra = 0
            salary = salary_n
        #mostrar en consola el sueldo bruto.
        #mostrar en consola los descuentos por parafiscales, salud y pensión.
        #mostrar en consola el sueldo neto a pagar.
        #mostrar en consola las provisiones hechas para prima, cesantías, intereses de cesantía y vacaciones
        imprimir(name, hour, value, salary_n, extra, salary, week)
            
principal()
