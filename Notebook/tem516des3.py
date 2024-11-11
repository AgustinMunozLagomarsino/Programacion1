# Función de búsqueda binaria para encontrar un estudiante en una lista ordenada
def buscar_estudiante(lista_estudiantes, nombre_buscado):
    inicio = 0
    fin = len(lista_estudiantes) - 1
    
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista_estudiantes[medio] == nombre_buscado:
            return medio  # Retorna el índice si se encuentra el estudiante
        elif lista_estudiantes[medio] < nombre_buscado:
            inicio = medio + 1
        else:
            fin = medio - 1
    
    return None  # Retorna None si no se encuentra el estudiante

# Lista ordenada alfabéticamente con los nombres de los estudiantes
lista_estudiantes = ["Ana", "Carlos", "Daniel", "Esteban", "Fernanda", "Juan", "Laura", "María", "Pedro", "Sofía"]

# Nombre del estudiante a buscar
nombre_buscado = "Juan"

# Buscar el nombre en la lista
resultado = buscar_estudiante(lista_estudiantes, nombre_buscado)

if resultado is not None:
    print(f"El estudiante {nombre_buscado} se encuentra en el índice {resultado}.")
else:
    print(f"El estudiante {nombre_buscado} no está en la lista.")
