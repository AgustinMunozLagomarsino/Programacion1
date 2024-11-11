# Función de ordenamiento por selección para ordenar estudiantes por su promedio (de mayor a menor)
def ordenar_por_promedio(estudiantes):
    # Recorremos la lista para ubicar los estudiantes con el promedio más alto primero
    for i in range(len(estudiantes)):
        # Suponemos que el primer elemento no ordenado es el máximo
        max_idx = i
        for j in range(i + 1, len(estudiantes)):
            if estudiantes[j][1] > estudiantes[max_idx][1]:  # Comparar promedios
                max_idx = j
        # Intercambiamos el estudiante con el promedio más alto encontrado con el actual
        estudiantes[i], estudiantes[max_idx] = estudiantes[max_idx], estudiantes[i]

# Lista de estudiantes y sus promedios
estudiantes = [
    ("Ana", 8),
    ("Carlos", 9),
    ("Daniel", 7),
    ("Esteban", 9.5),
    ("Fernanda", 8.8),
    ("Juan", 7.9),
    ("Laura", 12),
    ("María", 10),
    ("Pedro", 11),
    ("Sofía", 2)
]

# Ordenar la lista de estudiantes por promedio (de mayor a menor)
ordenar_por_promedio(estudiantes)

# Mostrar la lista ordenada
print("Estudiantes ordenados por promedio (de mayor a menor):")
for estudiante, promedio in estudiantes:
    print(f"{estudiante}: {promedio}")
