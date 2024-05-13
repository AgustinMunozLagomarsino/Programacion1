#objetos
productos = {"banana":20,"manzana":8,"pera":12}
#
print("Selecciona un producto:")
for i, opcion in enumerate(productos, start=1):
    print(f"{i}.{opcion}")
#
producto_elegido= input("Ingrese el producto que desea:")

# Verificar si la opción ingresada es válida
print(vars(productos, __dict__ ))
if producto_elegido.isdigit() and 1 <= int(producto_elegido) <= len(productos):
    lista=enumerate(productos, start=1)
    print(lista[1])
    #producto_seleccionado = lista[int(producto_elegido) - 1]
    #print(f"Elegiste: {producto_seleccionado}")
else:
    print("Opción inválida. Por favor, ingresa un número válido correspondiente a uno de los productos.")

