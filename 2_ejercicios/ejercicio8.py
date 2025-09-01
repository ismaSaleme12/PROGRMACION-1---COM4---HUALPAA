print("")
print(" EJERCICIO 8 ")

nombre_completo = input(" < Ingrese su nombre completo:> ")

cantidad_productos = int(input("< ingrese la cantidad de productos comprados: > "))

monto_total = float(input("< ingrese el monto total de la compra: > "))

if cantidad_productos < 0 or monto_total < 0:
    
    print(" ")
    print("ERROR: La cantidad de productos y/o el monto total no pueden ser negativos.")
    exit()


medio_de_pago = str(input("< ingrese el medio de pago: <1> efectivo / <2> debito / <3> credito / <4> mercado pago: "))

if medio_de_pago not in ["1", "2", "3", "4"]:
    
    print(" ")
    print("Opcion invalida. Debe ingresar 1, 2, 3 o 4")
    exit()


if medio_de_pago == "1":
    
    medio_de_pago_escrito = "Efectivo"
    descuento_o_recargo = "15% de descuento por pago con efectivo"
    monto_final = monto_total - (monto_total * 0.15)
    
elif medio_de_pago == "2":
    
    
    medio_de_pago_escrito = "Debito"
    descuento_o_recargo = "10% de descuento por pago con debito"
    monto_final = monto_total - (monto_total * 0.10)
    
elif medio_de_pago == "3":
    
    medio_de_pago_escrito = "Credito"
    descuento_o_recargo = "5% de recargo por pago con credito"
    monto_final = monto_total + (monto_total * 0.05)
    
elif medio_de_pago == "4":
    
    medio_de_pago_escrito = "Mercado pago"
    
    if monto_total > 10000:
        
        descuento_o_recargo = "20% de descuento por pago con mercado pago y un total de  $10000"
        monto_final = monto_total - (monto_total * 0.20)



if cantidad_productos > 10: 
    monto_final -= monto_final * 0.05
    
    
print(" ")
print(F"|MONTO INICIAL: ${monto_total}")
print(F"|MONTO FINAL (DESCUENTOS O RECARGOS): ${monto_final}")
print(f"|DESCUENTOS/RECARGOS APLICADOS: {descuento_o_recargo}")