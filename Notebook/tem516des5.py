class NodoEstudiante:
    def __init__(self, nombre, promedio):
        self.nombre = nombre
        self.promedio = promedio
        self.izquierda = None
        self.derecha = None


class ArbolPromedios:
    def __init__(self):
        self.raiz = None

    def insertar(self, nombre, promedio):
        """Inserta un nuevo nodo en el árbol de búsqueda binario."""
        nuevo_nodo = NodoEstudiante(nombre, promedio)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            self._insertar_recursivo(self.raiz, nuevo_nodo)

    def _insertar_recursivo(self, actual, nuevo_nodo):
        """Función recursiva para insertar un nodo en el lugar correcto."""
        if nuevo_nodo.promedio < actual.promedio:
            if actual.izquierda is None:
                actual.izquierda = nuevo_nodo
            else:
                self._insertar_recursivo(actual.izquierda, nuevo_nodo)
        else:
            if actual.derecha is None:
                actual.derecha = nuevo_nodo
            else:
                self._insertar_recursivo(actual.derecha, nuevo_nodo)

    def recorrido_inorden(self):
        """Realiza un recorrido inorden y devuelve los estudiantes en orden ascendente de promedio."""
        estudiantes_ordenados = []
        self._recorrido_inorden_recursivo(self.raiz, estudiantes_ordenados)
        return estudiantes_ordenados

    def _recorrido_inorden_recursivo(self, nodo, lista):
        """Función recursiva para el recorrido inorden."""
        if nodo is not None:
            self._recorrido_inorden_recursivo(nodo.izquierda, lista)
            lista.append((nodo.nombre, nodo.promedio))  # Guardamos el nombre y promedio del estudiante
            self._recorrido_inorden_recursivo(nodo.derecha, lista)


# Crear una instancia del árbol
arbol = ArbolPromedios()

# Agregar estudiantes y sus promedios al árbol
estudiantes = [
    ("Ana", 8),
    ("Luis", 9),
    ("Carla", 7),
    ("Pedro", 8),
    ("Marta", 10)
]

for nombre, promedio in estudiantes:
    arbol.insertar(nombre, promedio)

# Obtener el listado de estudiantes en orden ascendente de promedio
estudiantes_ordenados = arbol.recorrido_inorden()
print("Estudiantes en orden ascendente de rendimiento académico:")
for nombre, promedio in estudiantes_ordenados:
    print(f"{nombre}: {promedio}")
