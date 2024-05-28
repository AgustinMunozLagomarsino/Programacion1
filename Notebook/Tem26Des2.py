# Solicitar las calificaciones al usuario, separadas por comas
calificaciones_str = input("Ingresa todas tus calificaciones, separadas por comas: ")

# Convertir la cadena de entrada en una lista de números flotantes
calificaciones = [float(nota) for nota in calificaciones_str.split(',')]

# Calcular el promedio de las calificaciones
promedio = sum(calificaciones) / len(calificaciones)

# Imprimir el promedio
print(f"El promedio de tus calificaciones es: {promedio:.2f}")