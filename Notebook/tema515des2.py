# Definición del nodo de un árbol binario
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Función para realizar un recorrido en inorden y calcular la suma de los valores
def suma_inorden(nodo):
    if nodo is None:
        return 0
    # Llamada recursiva para el subárbol izquierdo, luego el nodo y finalmente el subárbol derecho
    return suma_inorden(nodo.izquierda) + nodo.valor + suma_inorden(nodo.derecha)

# Construcción del árbol binario de ejemplo
raiz = Nodo(1)
raiz.izquierda = Nodo(2)
raiz.derecha = Nodo(3)
raiz.izquierda.izquierda = Nodo(4)
raiz.izquierda.derecha = Nodo(5)
raiz.derecha.izquierda = Nodo(6)
raiz.derecha.derecha = Nodo(7)

# Cálculo de la suma de los valores del árbol en recorrido inorden
resultado = suma_inorden(raiz)
print("La suma de todos los valores en el árbol es:", resultado)
