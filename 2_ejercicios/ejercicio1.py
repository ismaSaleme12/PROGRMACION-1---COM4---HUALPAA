print(" ")
nombre_apellido = input(" < Ingrese su nombre y apellido: > ")

edad = int(input("< ingrese su edad: > "))

promedio = float(input("< ingrese su promedio: > "))

ingresos = float(input("< ingrese sus ingresos mensuales: >"))

if promedio < 6:
    beca = "RECHAZADO. No cumple con los requisitos"
elif promedio >= 6:
    
    if ingresos < 300000:
        
        beca = "ACEPTADO. Beca completa"
        
    elif 300000 >= ingresos <= 600000:
        
        beca = "ACEPTADO. Beca del 50%"
        
    elif ingresos > 600000:
        
        beca = "RECHAZADO. No cumple con los requisitos"

print(F"|ALUMNO/A: {nombre_apellido}")
print(f"|EDAD: {edad}") 
print(f"|PROMEDIO: {promedio}")
print(f"|INGRESOS: {ingresos}") 
print(f"|RESULTADO: {beca}")