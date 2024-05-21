#Supón que estás analizando las calificaciones de los estudiantes y quieres
#saber cuántos aprobaron y cuántos desaprobaron. Se considera que una calificación de 7 o 
#superior es aprobatoria y cualquier calificación menor a 7 es desaprobatoria.
#Utiliza lo que aprendiste sobre bucles y condicionales para resolver este problema.
# Agustin Muñoz 

calificación_alumnos=0
#ingresar calificaciones 
calificación_alumnos=int(input("ingrese calificacion del estudiante:"))
if calificación_alumnos >= 1 and calificación_alumnos <= 7:
    print("Desaprobado!") 
elif calificación_alumnos >= 8 and calificación_alumnos <= 12:
    print("Aprobado")
else: print("fuera de rango")
#del 1 al 7 = desaprobado y del 7 al 12 = aprobado 
