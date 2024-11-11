# Definición del nodo de un árbol binario
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Función para realizar un recorrido en preorden
def preorden(nodo):
    if nodo is not None:
        print(nodo.valor, end=' ')
        preorden(nodo.izquierda)
        preorden(nodo.derecha)

# Construcción del árbol binario
raiz = Nodo(1)
raiz.izquierda = Nodo(2)
raiz.derecha = Nodo(3)
raiz.izquierda.izquierda = Nodo(4)
raiz.izquierda.derecha = Nodo(5)
raiz.derecha.izquierda = Nodo(6)
raiz.derecha.derecha = Nodo(7)

# Llamada a la función de recorrido en preorden
preorden(raiz)
