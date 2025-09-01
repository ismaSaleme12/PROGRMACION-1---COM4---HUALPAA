print(" ")
print(" EJERCICIO 2 ")

nombre_completo = input(" < Ingrese su nombre completo:> ")

dni = int(input("< ingrese su dni: > "))

# validaciond de numeros de dni
if dni < 1000000 or dni > 99999999 or len(str(dni)) < 7:
    
    print(" ")
    print("DNI invalido. Debe tener entre 7 y 8 digitos")
    exit()

edad = int(input("< ingrese su edad: > "))

obra_social = str(input("< ¿Tiene obra social? si/no:>")).lower()

prioridad = str(input("< 1 = emergencia, 2 = urgencia, 3 = control:>")).lower()
    
    
# Asignacion de turno
if prioridad == "1":
    
    print("Inmediatamente a la guardia")
    exit()
    
elif prioridad == "2":
    
    if obra_social == "si":
        turno_asignado = "Turno en menos de 24hs"
    elif obra_social == "no":
        turno_asignado = "Turno en 48hs"
        
elif prioridad == "3":
    
    if edad > 65:
        turno_asignado = "Turno preferencial en 72hs"
    else:
        turno_asignado = "Turno normal en 7 dias"
        
print(" ")
print(F"|PACIENTE: {nombre_completo}")
print(f"|DNI: {dni}")
print(f"|EDAD: {edad}")
print(f"|PRIORIDAD: {prioridad}")
print(f"|TURNO ASIGNADO: {turno_asignado}")