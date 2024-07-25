#Desafío 2: Mejora del Cálculo del Promedio
#Toma el ejemplo del cálculo del promedio de calificaciones y mejóralo. En lugar de pedir las calificaciones una por una, modifica el código para pedir todas las calificaciones al mismo tiempo (el estudiante puede ingresar las calificaciones separadas por comas) y luego calcular el promedio.
# Solicitar las calificaciones al usuario, separadas por comas para mejorar su uso 
calificaciones_str = input("Ingresa todas tus calificaciones, separadas por comas: ")

# Convertir la cadena de entrada en una lista de números flotantes para poder utilizar números
calificaciones = [float(nota) for nota in calificaciones_str.split(',')]

# Calcular el promedio de las calificaciones dividiendo 
promedio = sum(calificaciones) / len(calificaciones)

# Imprimir el promedio con un fstring 
print(f"El promedio de tus calificaciones es: {promedio:.2f}")
