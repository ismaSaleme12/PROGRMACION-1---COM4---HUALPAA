print(" ")
print(" EJERCICIO 7 ")

nombre_completo = input(" < Ingrese su nombre completo:> ")
edad = int(input("< ingrese su edad: > "))
años_experiencia = int(input("< ingrese sus años de experiencia manejando: > "))

if edad < 18:
    
    print("NO PUEDE CONDUCIR")
    
elif edad >= 18 and años_experiencia < 1:
    
    categoria_licencia = "PRINCIPIANTE"
    
elif edad >= 21 and 1 < años_experiencia < 5:
    
    categoria_licencia = " CONDUCTOR INTERMEDIO"
    
elif edad >= 30 and años_experiencia > 10:
    
    categoria_licencia = "CONDUCTOR PROFESIONAL"
    
else:
    
    categoria_licencia = "CONDUCTOR ESTANDAR"
    
    
print(" ")
print( "|DATOS DE USUARIO")
print(F"|NOMBRE: {nombre_completo}")
print(f"|EDAD: {edad}")
print(f"|AÑOS DE EXPERIENCIA MANEJANDO: {años_experiencia}")
print(f"|CATEGORIA DE LICENCIA: {categoria_licencia}")