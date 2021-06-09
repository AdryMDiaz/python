# -*- coding: utf-8 -*-
"""
Created on Fri May  7 18:23:51 2021

@author: Adry Diaz
"""

#Diseñar un esquema de porcentajes de ayuda (descuento sobre la matrícula) para sus nuevos estudiantes
#Cada estudiante deberá dar sus datos personales (nombres, apellidos, edad en años, salario mínimo mensual de ingreso familiar)
#El estudiante presentará un examen de aptitud académica y razonamiento, que será calificado en números de 0 a 100 y se ingresará el resultado por pantalla

#El calculo del porcentaje de apoyo será según los siguientes criterios
#Si la edad está en el rango: 
#de 15 a 18 años dar 25%, 
#de 19 a 21 años dar 15% y 
#de 22 a 25 años dar 10%, 
#para mayores de 25 no dar ningún apoyo por edad

#Si el ingreso familiar:
#es inferior o igual a un salario mínimo dar 30%, 
#si es mayor a un salario mínimo e inferior o igual a 2 salarios mínimos dar 20%, 
#si es mayor a dos salarios mínimos e inferior o igual a 3 salarios mínimos dar 10%, 
#si es mayor a tres salarios mínimos e inferior o igual a 4 salarios mínimos dar 5%, 
#para ingresos superiores no dar ningún apoyo por ingreso familiar

#Si su puntaje de ingreso:
#es mayor o igual a 80 y menor de 86 dar 30%, 
#si es mayor o igual a 86 y menor de 91 dar 35%, 
#si es mayor o igual a 91 y menor de 96 dar 40%, y 
#si es mayor o igual a 96 dar 45%. 
#Para puntajes menores de ochenta, no hay apoyo por puntaje de examen

#Los apoyos recibidos por edad, por ingreso familiar y por puntaje de examen se deben sumar para dar el porcentaje total de apoyo que recibirá el beneficiario, es decir, el porcentaje de descuento sobre el valor de la matrícula

print ("===================================================================")
print ("=============================BIENVENIDO============================")
print ("ESQUEMA DE PORCENTAJES PARA AYUDAS ACADÉMICAS - NUEVOS ESTUDIANTES")
print ("====================DESCUENTO SOBRE LA MATRICULA===================")
print ("===================================================================")

#Leer desde el teclado el nombre y apellido del candidato, su edad entera en años, y el número decimal de salarios mínimos mensuales de su ingreso familiar
name = input("Por favor ingrese nombres y apellidos del estudiante: ")
age = int(input("Por favor ingrese la edad en años del estudiante: "))
smlv = int(908526) #Salario básico para el año 2021 en Colombia
ingreso = int(input("Por favor ingrese el valor total mensual del ingreso familiar del estudiante. Ej:(1200000): "))
test = int(input("Por favor ingrese el puntaje obtenido por el estudiante en el examen de aptitud académica y razonamiento: "))
salario = round((ingreso / smlv),1)

print ()

#Definición de porcentajes asignados por edad
if age >= 15 and age <= 18:
    per_age = 0.25
elif age >= 19 and age <= 21:
    per_age = 0.15
elif age >= 22 and age <= 25:
    per_age = 0.10
else: 
    per_age = 0.0

#Definición de porcentajes asignados por ingreso familiar definido en salarios mínimos
if salario <= 1.0:
    per_sal = 0.3
elif salario > 1.0 and salario <= 2.0:
    per_sal = 0.2
elif salario > 2.0 and salario <= 3.0:
    per_sal = 0.1
elif salario > 3.0 and salario <= 4.0:
    per_sal = 0.05
else:
    persal = 0.0

#Definición de porcentajes asignados por puntaje en el examen de aptitud académica
if test >= 80 and test < 86:
    per_test = 0.30
elif test >= 86 and test < 91:
    per_test = 0.35
elif test >= 91 and test < 96:
    per_test = 0.40
elif test >= 96:
    per_test = 0.45
else:
    per_test = 0.0

#Calcular el valor total de descuento del candidato según los criterios antes definidos
per_total = round(((per_age + per_sal + per_test) * 100),2)

#Mostrar en consola el nombre y apellido del beneficiario, 
#el descuento recibido por edad, el recibido por el ingreso familiar, 
#el recibido por el puntaje del examen y el descuento total que recibirá sobre el valor de la matrícula
print ("\n=============================")
print ("RELACION DE APOYOS RECIBIDOS")
print ("=============================")
print ("\nEl valor total del descuento sobre la matricula para el estudiante " + str(name) + " con " + str(age) + " años de edad y " + str(salario) + " salarios minimos es: " + str(per_total) + "%")
print ("\nEl apoyo recibido por edad es de: ", (per_age * 100), "%")
print ("\nEl apoyo recibido por ingreso familiar de acuerdo al salario minímo mensual es de: ", (per_sal * 100), "%")
print ("\nEl apoyo recibido de acuerdo al puntaje obtenido en la prueba de aptitud académica y razonamiento es: ", (per_test * 100), "%")