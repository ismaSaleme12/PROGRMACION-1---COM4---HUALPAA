print(" ")
print (" EJERCICIO 5 ")

nombre_completo = input(" < Ingrese su nombre completo:> ")

estado = str(" ")

legajo = int(input("< ingrese su numero de legajo: > "))

nota1 = int(input("< ingrese su primera nota: > "))
nota2 = int(input("< ingrese su segunda nota: > "))
nota3 = int(input("< ingrese su tercera nota: > "))

promedio = (nota1 + nota2 + nota3) / 3

if nota1 < 4 or nota2 < 4 or nota3 < 4:
    estado = "DESAPROBADO DIRECTO"
elif promedio < 6:
    estado = "DESAPROBADO"
elif promedio == 6 or promedio == 7:
    estado = "APROBADO CON FINAL"
elif promedio >= 8:
    estado = "PROMOCIONADO"
    
print(" ")
print(F"|ALUMNO/A: {nombre_completo}")
print(f"|LEGAJO: {legajo}")
print(f"|ESTADO ACADEMICO: {estado}")