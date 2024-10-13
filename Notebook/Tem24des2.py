# Programa para leer 5 calificaciones y calcular el promedio

# Lista para almacenar las calificaciones
calificaciones = []

# Ciclo para ingresar 5 calificaciones
for i in range(5):
    # Solicitar al usuario una calificación y convertirla en float
    calificacion = float(input(f"Ingrese la calificación {i+1}: "))
    calificaciones.append(calificacion)

# Calcular el promedio
promedio = sum(calificaciones) / len(calificaciones)

# Mostrar el promedio
print(f"El promedio de las calificaciones es: {promedio}")
