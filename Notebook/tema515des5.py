# Definición del nodo del árbol de expresiones
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Función para verificar si un carácter es un operador
def es_operador(c):
    return c in {'+', '-', '*', '/'}

# Función para obtener la precedencia de un operador
def precedencia(op):
    if op in {'+', '-'}:
        return 1
    if op in {'*', '/'}:
        return 2
    return 0

# Función para construir el árbol de expresiones a partir de una expresión infija
def construir_arbol_expresion(expresion):
    valores = []
    operadores = []
    
    i = 0
    while i < len(expresion):
        # Ignoramos los espacios
        if expresion[i] == ' ':
            i += 1
            continue
        
        # Si el carácter es un número, lo convertimos en un nodo y lo agregamos a la pila de valores
        elif expresion[i].isdigit():
            num = 0
            while i < len(expresion) and expresion[i].isdigit():
                num = num * 10 + int(expresion[i])
                i += 1
            valores.append(Nodo(num))
            i -= 1  # Ajustamos el índice para evitar saltarnos caracteres
        
        # Si el carácter es un operador
        elif es_operador(expresion[i]):
            while (operadores and precedencia(operadores[-1]) >= precedencia(expresion[i])):
                # Procesamos el operador anterior con mayor o igual precedencia
                op = operadores.pop()
                derecho = valores.pop()
                izquierdo = valores.pop()
                nodo = Nodo(op)
                nodo.izquierda = izquierdo
                nodo.derecha = derecho
                valores.append(nodo)
            # Agregamos el operador actual a la pila de operadores
            operadores.append(expresion[i])
        
        i += 1
    
    # Procesamos los operadores restantes
    while operadores:
        op = operadores.pop()
        derecho = valores.pop()
        izquierdo = valores.pop()
        nodo = Nodo(op)
        nodo.izquierda = izquierdo
        nodo.derecha = derecho
        valores.append(nodo)
    
    # El último valor en la pila es la raíz del árbol de expresiones
    return valores[-1]

# Función para evaluar el árbol de expresiones
def evaluar_arbol(nodo):
    # Si el nodo es un número, devolvemos su valor
    if not es_operador(nodo.valor):
        return nodo.valor
    
    # Si el nodo es un operador, evaluamos los subárboles izquierdo y derecho
    izquierdo_valor = evaluar_arbol(nodo.izquierda)
    derecho_valor = evaluar_arbol(nodo.derecha)
    
    # Aplicamos el operador correspondiente
    if nodo.valor == '+':
        return izquierdo_valor + derecho_valor
    elif nodo.valor == '-':
        return izquierdo_valor - derecho_valor
    elif nodo.valor == '*':
        return izquierdo_valor * derecho_valor
    elif nodo.valor == '/':
        return izquierdo_valor / derecho_valor

# Prueba del programa con la expresión "5 + 3 * 4"
expresion = "5 + 3 * 4"
arbol_expresion = construir_arbol_expresion(expresion)
resultado = evaluar_arbol(arbol_expresion)
print("El resultado de la expresión es:", resultado)
