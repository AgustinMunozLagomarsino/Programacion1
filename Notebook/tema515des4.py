# Definición del nodo de un árbol binario
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Función para insertar un valor en el árbol de búsqueda binaria
def insertar(nodo, valor):
    # Si el árbol está vacío, crea un nuevo nodo raíz
    if nodo is None:
        return Nodo(valor)
    # Si el valor es menor, se inserta en el subárbol izquierdo
    elif valor < nodo.valor:
        nodo.izquierda = insertar(nodo.izquierda, valor)
    # Si el valor es mayor, se inserta en el subárbol derecho
    else:
        nodo.derecha = insertar(nodo.derecha, valor)
    return nodo

# Función para construir el árbol de búsqueda binaria a partir de un conjunto de valores
def construir_abb(valores):
    raiz = None
    for valor in valores:
        raiz = insertar(raiz, valor)
    return raiz

# Función para buscar un número en el árbol de búsqueda binaria
def buscar(nodo, numero):
    # Si el nodo es None, el número no está en el árbol
    if nodo is None:
        return False
    # Si el valor del nodo es el número buscado, devuelve True
    if nodo.valor == numero:
        return True
    # Si el número es menor, busca en el subárbol izquierdo
    elif numero < nodo.valor:
        return buscar(nodo.izquierda, numero)
    # Si el número es mayor, busca en el subárbol derecho
    else:
        return buscar(nodo.derecha, numero)

# Ejemplo de uso
valores = {20, 10, 30, 5, 15, 25, 35}
raiz = construir_abb(valores)

# Búsqueda de un número en el árbol
numero_a_buscar = 15
encontrado = buscar(raiz, numero_a_buscar)
print(f"El número {numero_a_buscar} {'existe' if encontrado else 'no existe'} en el árbol.")
