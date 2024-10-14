# Inicialización de listas vacías para tiendas, artículos, personal y registros de ventas
lista_tiendas = []
lista_productos = []
lista_empleados = []
lista_transacciones = []

# Función para registrar una nueva tienda
def registrar_tienda(nombre, ubicacion):
    tienda = {
        "nombre": nombre,
        "ubicacion": ubicacion,
        "inventario": [],
        "equipo": []
    }
    lista_tiendas.append(tienda)

# Función para registrar un nuevo producto
def registrar_producto(nombre, precio, stock):
    producto = {
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }
    lista_productos.append(producto)

# Función para registrar un nuevo empleado
def registrar_empleado(nombre, puesto):
    empleado = {
        "nombre": nombre,
        "puesto": puesto
    }
    lista_empleados.append(empleado)

# Función para asignar productos a una tienda
def asignar_producto_a_tienda(nombre_tienda, nombre_producto):
    tienda = next((t for t in lista_tiendas if t["nombre"] == nombre_tienda), None)
    if tienda is None:
        print("Error: Tienda no encontrada.")
        return

    producto = next((p for p in lista_productos if p["nombre"] == nombre_producto), None)
    if producto is None:
        print("Error: Producto no encontrado.")
        return

    tienda["inventario"].append(producto)

# Función para asignar empleados a una tienda
def asignar_empleado_a_tienda(nombre_tienda, nombre_empleado):
    tienda = next((t for t in lista_tiendas if t["nombre"] == nombre_tienda), None)
    if tienda is None:
        print("Error: Tienda no encontrada.")
        return

    empleado = next((e for e in lista_empleados if e["nombre"] == nombre_empleado), None)
    if empleado is None:
        print("Error: Empleado no encontrado.")
        return

    tienda["equipo"].append(empleado)

# Función para registrar una transacción de venta
def registrar_transaccion(nombre_tienda, nombre_producto, cantidad, nombre_empleado):
    tienda = next((t for t in lista_tiendas if t["nombre"] == nombre_tienda), None)
    if tienda is None:
        print("Error: Tienda no encontrada.")
        return

    producto = next((p for p in lista_productos if p["nombre"] == nombre_producto), None)
    if producto is None:
        print("Error: Producto no encontrado.")
        return

    empleado = next((e for e in lista_empleados if e["nombre"] == nombre_empleado), None)
    if empleado is None:
        print("Error: Empleado no encontrado.")
        return

    transaccion = {
        "tienda": nombre_tienda,
        "producto": nombre_producto,
        "cantidad": cantidad,
        "empleado": nombre_empleado
    }
    lista_transacciones.append(transaccion)

# Funciones para mostrar los registros
def listar_tiendas():
    print("\nListado de Tiendas:")
    for tienda in lista_tiendas:
        print(f"Tienda: {tienda['nombre']} - Dirección: {tienda['ubicacion']}")

def listar_productos():
    print("\nListado de Productos:")
    for producto in lista_productos:
        print(f"Producto: {producto['nombre']} - Precio: {producto['precio']} - En Stock: {producto['stock']}")

def listar_empleados():
    print("\nListado de Empleados:")
    for empleado in lista_empleados:
        print(f"Empleado: {empleado['nombre']} - Puesto: {empleado['puesto']}")

def listar_transacciones():
    print("\nRegistro de Transacciones:")
    for transaccion in lista_transacciones:
        print(f"Tienda: {transaccion['tienda']} - Producto: {transaccion['producto']} - Cantidad: {transaccion['cantidad']} - Atendido por: {transaccion['empleado']}")




# Ejemplos de uso
registrar_tienda("Supermax", "Calle Primavera, Lima")
registrar_tienda("MegaStore", "Avenida Sol, Cusco")
registrar_tienda("Comercial Andina", "Calle Central, Arequipa")

registrar_producto("Laptop Dell", 18000, 40)
registrar_producto("iPhone 13", 9000, 80)
registrar_producto("Samsung Galaxy Tab", 10000, 35)
registrar_producto("Xbox Series X", 11000, 25)
registrar_producto("Smart TV Sony", 27000, 10)

registrar_empleado("Pedro Ruiz", "Supervisor")
registrar_empleado("Lucía Valdez", "Cajero")
registrar_empleado("Roberto Mendoza", "Encargado de almacén")
registrar_empleado("Sofía Estrada", "Supervisor")
registrar_empleado("Elena Quintana", "Vendedor")

asignar_producto_a_tienda("Supermax", "Laptop Dell")
asignar_producto_a_tienda("Supermax", "iPhone 13")
asignar_producto_a_tienda("MegaStore", "Xbox Series X")
asignar_producto_a_tienda("MegaStore", "Smart TV Sony")
asignar_producto_a_tienda("Comercial Andina", "Samsung Galaxy Tab")
asignar_producto_a_tienda("Comercial Andina", "iPhone 13")

asignar_empleado_a_tienda("Supermax", "Pedro Ruiz")
asignar_empleado_a_tienda("Supermax", "Lucía Valdez")
asignar_empleado_a_tienda("MegaStore", "Sofía Estrada")
asignar_empleado_a_tienda("MegaStore", "Elena Quintana")
asignar_empleado_a_tienda("Comercial Andina", "Roberto Mendoza")
asignar_empleado_a_tienda("Comercial Andina", "Pedro Ruiz")

registrar_transaccion("Supermax", "Laptop Dell", 3, "Pedro Ruiz")
registrar_transaccion("Supermax", "iPhone 13", 7, "Lucía Valdez")
registrar_transaccion("MegaStore", "Xbox Series X", 5, "Sofía Estrada")
registrar_transaccion("Comercial Andina", "Samsung Galaxy Tab", 4, "Roberto Mendoza")
registrar_transaccion("Comercial Andina", "iPhone 13", 6, "Pedro Ruiz")

listar_tiendas()
listar_productos()
listar_empleados()
listar_transacciones()
print("este trabajo fue realizado con ayuda de Anthony martinelli")