def eliminar_duplicados(lista):
    # Utiliza un conjunto para eliminar duplicados y luego convierte de nuevo a lista
    lista_sin_duplicados = list(set(lista))
    return lista_sin_duplicados

# Lista de números con duplicados
lista_numeros = [3, 5, 2, 3, 8, 5, 6, 2, 9, 8, 10, 6]

# Muestra la lista original
print("Lista original:", lista_numeros)

# Elimina duplicados y muestra la lista sin duplicados
lista_sin_duplicados = eliminar_duplicados(lista_numeros)
print("Lista sin duplicados:", lista_sin_duplicados)
