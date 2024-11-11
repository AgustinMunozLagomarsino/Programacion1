# Definición del nodo de un árbol binario
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Función para encontrar el valor máximo en un recorrido postorden
def maximo_postorden(nodo):
    if nodo is None:
        return float('-inf')  # Si el nodo es None, devolvemos el menor valor posible
    
    # Llamada recursiva para el subárbol izquierdo y derecho
    max_izquierda = maximo_postorden(nodo.izquierda)
    max_derecha = maximo_postorden(nodo.derecha)
    
    # El máximo es el mayor entre el valor del nodo actual y los valores máximos de sus subárboles
    return max(nodo.valor, max_izquierda, max_derecha)

# Construcción de un árbol binario de ejemplo
raiz = Nodo(1)
raiz.izquierda = Nodo(15)
raiz.derecha = Nodo(3)
raiz.izquierda.izquierda = Nodo(4)
raiz.izquierda.derecha = Nodo(50)
raiz.derecha.izquierda = Nodo(6)
raiz.derecha.derecha = Nodo(7)

# Encontrar el valor máximo en el árbol
resultado = maximo_postorden(raiz)
print("El valor máximo en el árbol es:", resultado)
