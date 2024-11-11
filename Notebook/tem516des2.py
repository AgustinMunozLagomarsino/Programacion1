# Función para buscar una calificación en la matriz de calificaciones
def buscar_calificacion(matriz_calificaciones, calificacion_buscada):
    for i, fila in enumerate(matriz_calificaciones):
        for j, calificacion in enumerate(fila):
            if calificacion == calificacion_buscada:
                return (i, j)  # Retorna una tupla con el índice del estudiante y la materia
    return None  # Retorna None si no se encuentra la calificación

# Ejemplo de matriz de calificaciones
# Cada fila representa a un estudiante y cada columna representa una materia
matriz_calificaciones = [
    [85, 90, 78],  # Estudiante 0
    [92, 88, 79],  # Estudiante 1
    [75, 85, 80],  # Estudiante 2
    [89, 91, 92]   # Estudiante 3
]

# Calificación a buscar
calificacion_buscada = 79

# Buscar la calificación en la matriz
resultado = buscar_calificacion(matriz_calificaciones, calificacion_buscada)

if resultado:
    estudiante, materia = resultado
    print(f"La calificación {calificacion_buscada} se encuentra en el estudiante {estudiante}, materia {materia}.")
else:
    print(f"La calificación {calificacion_buscada} no se encuentra en la matriz.")
