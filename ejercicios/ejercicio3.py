print("<VIAJE EN AUTO>")

print(" ")

distancia_km=int(input("-Ingresa la distancia en km: "))
precio_nafta=int(input("-Ingresa el precio de la nafta por litro: "))

litros_nafta=(distancia_km*8)/100
costo_viaje=(litros_nafta*precio_nafta)
horas_viaje=(distancia_km)/90

print(" ")

print(f"-Se necesitan {round(litros_nafta)} litros de nafta para el viaje")

print(f"-El costo total del viaje sera de ${round(costo_viaje,2)}")

print(f"-Si la velociad promedio es de 90km/h, el viaje duarara {round(horas_viaje)} horas")