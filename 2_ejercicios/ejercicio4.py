print(" ")
print(" EJERCICIO 4 ")

nombre_completo = input(" < Ingrese su nombre completo:> ")

edad = int(input("< ingrese su edad: > "))

ingresos = int(input("< ingrese sus ingresos anuales: > "))

if ingresos < 500000:
    impuestos = 0
elif ingresos >= 500000 and ingresos < 2000000:
    impuestos = ingresos * 0.10
elif ingresos >= 2000000 and ingresos < 5000000:
    impuestos = ingresos * 0.20
elif ingresos >= 5000000:
    impuestos = ingresos * 0.35
elif edad > 65:
    impuestos = ingresos - (ingresos * 0.5)
    
    
print(" ")
print(F"|NOMBRE: {nombre_completo}")
print(f"|EDAD: {edad}")
print(f"|INGRESOS: {ingresos}")
print(f"|IMPUESTOS A PAGAR: {impuestos}")