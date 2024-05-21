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
