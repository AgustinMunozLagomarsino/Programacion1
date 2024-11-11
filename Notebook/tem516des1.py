from collections import deque

# Definición del nodo del árbol
class NodoGrado:
    def __init__(self, grado, estudiantes=None):
        self.grado = grado                  # Nombre o número del grado
        self.estudiantes = estudiantes or [] # Lista de estudiantes en ese grado
        self.hijos = []                     # Hijos de este nodo, representan los grados inferiores

# Función para hacer un recorrido por niveles y mostrar los estudiantes de cada grado
def recorrido_por_niveles(raiz):
    if not raiz:
        return
    
    # Usamos una cola para el recorrido por niveles (BFS)
    cola = deque([raiz])
    
    while cola:
        # Sacamos el nodo actual de la cola
        nodo_actual = cola.popleft()
        
        # Mostramos el grado y los estudiantes en él
        print(f"Grado {nodo_actual.grado}: {', '.join(nodo_actual.estudiantes)}")
        
        # Agregamos los hijos del nodo actual a la cola
        for hijo in nodo_actual.hijos:
            cola.append(hijo)

# Ejemplo de creación del árbol de grupos de estudiantes
# Crear los nodos de cada grado
grado_12 = NodoGrado(12, ["Juan", "María", "Pedro"])
grado_11 = NodoGrado(11, ["Ana", "Luis", "Carla"])
grado_10 = NodoGrado(10, ["Sofía", "Miguel", "Javier"])
grado_9 = NodoGrado(9, ["Raúl", "Elena", "Laura"])

# Construir el árbol, cada grado inferior como hijo del grado superior
grado_12.hijos = [grado_11]
grado_11.hijos = [grado_10]
grado_10.hijos = [grado_9]

# Realizar el recorrido por niveles e imprimir los estudiantes de cada grado
print("Recorrido por niveles de los estudiantes en cada grado:")
recorrido_por_niveles(grado_12)
