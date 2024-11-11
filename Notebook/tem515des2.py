# Lista de códigos de productos en el inventario
inventario = ["P001", "P002", "P003", "P004", "P005"]

def buscar_codigo(codigo, lista_inventario):
    try:
        # Busca el índice del código en la lista de inventario
        posicion = lista_inventario.index(codigo)
        print(f"El código '{codigo}' se encuentra en la posición {posicion}.")
    except ValueError:
        # Maneja el caso en que el código no está en la lista
        print(f"El código '{codigo}' no se ha encontrado en el inventario.")

# Solicita al usuario que ingrese el código de producto
codigo_usuario = input("Ingresa el código de producto que deseas buscar: ")
buscar_codigo(codigo_usuario, inventario)
