print("CALIFICACION FINAL - ALGORITMOS")
print(" ")

#NOTA PARCIALES
print("<Ingrese sus tres calificaciones parciales>")

parcial1=float(input("parcial 1: "))
parcial2=float(input("parcial 2: "))
parcial3=float(input("parcial 3: "))

promedio_parciales=(parcial1+parcial2+parcial3)/3
porcentaje_parciales=promedio_parciales*0.55

#NOTA EXAMEN FINAL
print(" ")
print("<Ingrese la calificacion del examen final>")


examen_final=float(input("examen final: "))
porcentaje_examen=examen_final*0.30


#NOTA TRABAJO FINAL
print(" ")
print("<Ingrese la calificacion del trabajo final>")

trabajo_final=float(input("trabajo final: "))
porcentaje_trabajo=trabajo_final*0.15

#NOTA FINAL

calificacion_final=porcentaje_parciales+porcentaje_examen+porcentaje_trabajo

print(" ")
print(f"<Su calificacion final es:{round(calificacion_final,2)}")
