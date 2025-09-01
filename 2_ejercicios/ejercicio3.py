print(" ")
print(" EJERCICIO 3 ")

nombre_completo = input(" < Ingrese su nombre completo:> ")

cuit = (input("< ingrese su cuit: > "))

ingresos = int(input("< ingrese sus ingresos mensuales: > "))

antiguedad_laboral = int(input("< ingrese su antiguedad laboral (en años): > "))

historial_crediticio = str(input("< Historial crediticio: <1> bueno / <2> malo / <3> regular /")).lower()


#condicionales de ingresos
if historial_crediticio not in ["1", "2", "3"]:
    
    print(" ")
    print("Opcion invalida. Debe ingresar 1, 2 o 3")
    exit()
    
elif ingresos < 200000:
    
    print(" ")
    print("Prestamo RECHAZADO.")
    exit()
    
elif ingresos >= 200000 and antiguedad_laboral < 2:

    monto_aprobado = 500000
    
elif ingresos >= 200000 and antiguedad_laboral >= 2:

    if historial_crediticio == "1":
        
        monto_aprobado = 3000000
        
    elif historial_crediticio == "3":
        
        monto_aprobado = 1000000
        
print(" ")
print(F"|CLIENTE: {nombre_completo}")
print(f"|CUIT: {cuit[0] + cuit[1] + "-" + cuit[2] + cuit[3] + cuit[4] + cuit[5] + cuit[6] + cuit[7] + cuit[8] + "-" + cuit[9]}")
print(f"|INGRESOS: {ingresos}")
print(f"|ANTIGUEDAD LABORAL: {antiguedad_laboral}")
print(f"|HISTORIAL CREDITICIO: {historial_crediticio}")
print(f"|MONTO APROBADO: {monto_aprobado}")