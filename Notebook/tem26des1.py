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

# Lista de calificaciones de los estudiantes
calificaciones = [6, 8, 5, 7, 10, 9, 4, 3, 7, 6]

# Inicializar contadores
aprobados = 0
desaprobados = 0

# con la lista de calificaciones hago que si es ayor o igual a 7 apruebe 
for calificacion in calificaciones:
    if calificacion >= 7:
        aprobados += 1
    else:
        desaprobados += 1

# Mostrar resultados
print(f"Cantidad de estudiantes que aprobaron: {aprobados}")
print(f"Cantidad de estudiantes que desaprobaron: {desaprobados}")











