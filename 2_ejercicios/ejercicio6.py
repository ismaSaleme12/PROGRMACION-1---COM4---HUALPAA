print(" ")
print(" EJERCICIO 6 ")

#DATOS DE LA PERSONA
nombre_completo = input(" < Ingrese su nombre completo: > ")
pin = int(123456)

#VALORES NUMERICOS (SALDOS)
saldo_inicial = 50000
saldo_final = 0

#VALORES BOOLEANOS 
intentos = 0
salir_escrito = str(" ")
salir_booleano = bool(False)

#BUCLE DE INTENTOS
while intentos != 3:
    
    #VERIFICADOR DE INTENTOS 
    print("intento: ", intentos + 1)
    pin_ingresado = int(input( "< Ingrese su PIN:  > "))
    
    if pin_ingresado != pin: #SI ES DISTINTO AL PIN
        
        print("PIN incorrecto")
        print(" ")
        intentos += 1
        continue
    
    elif pin_ingresado == pin: #SI ES IGUAL AL PIN
        
        print("PIN correcto")
        print(" ")
        
        #MONTO A RETIRAR 
        print("saldo inicial: ", saldo_inicial)
        monto_retiro = int(input("retira un monto de dinero (multiplo de 1000 - no puede superar su saldo: )"))

        #VERIFICACION DE MONTO A RETIRAR
        if monto_retiro % 1000 != 0 or monto_retiro > saldo_inicial:
            
            print("Operacion invalida")
            exit()
            
        else:
            if monto_retiro > 20000:
                
                saldo_final = saldo_inicial - (monto_retiro + (monto_retiro * 0.02))
                
            else:
                
                saldo_final = saldo_inicial - monto_retiro
                
            break   
if intentos == 3:
    
    print(" ")
    print("Ha superado la cantidad de intentos. Su tarjeta ha sido bloqueada.")
    exit()   

print(" ")
print(f"su saldo actualizado: {saldo_final}")