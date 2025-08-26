print("PRESTAMO BANCARIO")
print(" ")

monto_prestamo=float(input("-Ingrese el monto del prestamo: "))

monto_devolver= monto_prestamo * (1.02)**12

print(f"<MONTO TOTAL A DEVOLVER>: ${round(monto_devolver,2)} ")
print(f"<CUOTA MENSUAL A PAGAR>: ${round(monto_devolver/12,2)} ")