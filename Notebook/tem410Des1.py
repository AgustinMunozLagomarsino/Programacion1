# Inicializar datos de la biblioteca
libros = []
usuarios = []
prestamos = []
multas = []

# Función para registrar un nuevo libro
def registrar_libro(nombre, escritor, tipo, cantidad, id_libro):
    nuevo_libro = {
        "Nombre": nombre,
        "Autor": escritor,
        "Género": tipo,
        "Stock": cantidad,
        "ID": id_libro
    }
    libros.append(nuevo_libro)
    print(f"Libro '{nombre}' registrado con éxito.")

# Función para registrar un nuevo usuario
def registrar_usuario(nombre_usuario, id_usuario):
    nuevo_usuario = {
        "Nombre": nombre_usuario,
        "ID": id_usuario
    }
    usuarios.append(nuevo_usuario)
    print(f"Usuario '{nombre_usuario}' registrado con éxito.")

# Función para gestionar un préstamo
def registrar_prestamo(id_libro, id_usuario, fecha_inicio, fecha_fin, id_prestamo):
    usuario = next((u for u in usuarios if u["ID"] == id_usuario), None)
    if not usuario:
        print("Error: Usuario no encontrado.")
        return

    libro = next((l for l in libros if l["ID"] == id_libro), None)
    if not libro:
        print("Error: Libro no encontrado.")
        return

    if libro["Stock"] < 1:
        print("Error: Sin stock disponible.")
        return

    nuevo_prestamo = {
        "ID Prestamo": id_prestamo,
        "ID Libro": id_libro,
        "ID Usuario": id_usuario,
        "Fecha Inicio": fecha_inicio,
        "Fecha Fin": fecha_fin
    }
    prestamos.append(nuevo_prestamo)
    print(f"Préstamo registrado: '{libro['Nombre']}' para '{usuario['Nombre']}'.")

# Función para registrar una multa
def registrar_multa(id_prestamo, monto_multa):
    prestamo = next((p for p in prestamos if p["ID Prestamo"] == id_prestamo), None)
    if not prestamo:
        print("Error: Préstamo no encontrado.")
        return

    nueva_multa = {
        "ID Prestamo": id_prestamo,
        "Monto": monto_multa,
        "ID Usuario": prestamo["ID Usuario"]
    }
    multas.append(nueva_multa)
    print(f"Multa de {monto_multa} pesos añadida al usuario con ID {prestamo['ID Usuario']}.")

# Función para eliminar un libro
def eliminar_libro(id_libro):
    libro = next((l for l in libros if l["ID"] == id_libro), None)
    if not libro:
        print("Error: Libro no encontrado.")
        return

    if libro["Stock"] > 1:
        libro["Stock"] -= 1
        print(f"Un ejemplar de '{libro['Nombre']}' eliminado. Quedan {libro['Stock']}.")
    else:
        prestamos_asociados = [p for p in prestamos if p["ID Libro"] == id_libro]
        if prestamos_asociados:
            print("Error: Hay préstamos pendientes, no se puede eliminar el libro.")
        else:
            libros.remove(libro)
            print(f"Libro '{libro['Nombre']}' eliminado.")

# Función para eliminar un usuario
def eliminar_usuario(id_usuario):
    usuario = next((u for u in usuarios if u["ID"] == id_usuario), None)
    if not usuario:
        print("Error: Usuario no encontrado.")
        return

    prestamos_activos = [p for p in prestamos if p["ID Usuario"] == id_usuario]
    if prestamos_activos:
        print("Error: El usuario tiene préstamos pendientes.")
    else:
        usuarios.remove(usuario)
        print(f"Usuario '{usuario['Nombre']}' eliminado.")

# Función para eliminar un préstamo
def eliminar_prestamo(id_prestamo):
    prestamo = next((p for p in prestamos if p["ID Prestamo"] == id_prestamo), None)
    if not prestamo:
        print("Error: Préstamo no encontrado.")
        return

    prestamos.remove(prestamo)
    print(f"Préstamo con ID '{id_prestamo}' eliminado.")

# Función para eliminar una multa
def eliminar_multa(id_prestamo):
    multa = next((m for m in multas if m["ID Prestamo"] == id_prestamo), None)
    if not multa:
        print("Error: Multa no encontrada.")
        return

    multas.remove(multa)
    print(f"Multa asociada al préstamo con ID '{id_prestamo}' eliminada.")

# Ejemplos 
registrar_libro("El Señor de los anillos", "J. R. R. Tolkien", "Clásico", 15, 501)
registrar_libro("Pedro picapiedra ", "Agustin Muñiz", "Fantasia", 50000, 902)
registrar_usuario("Domingo Muñoz", 201)
registrar_prestamo(501, 201, "2024-05-01", "2024-05-15", 301)
registrar_multa(301, 4000)

# Mostrar datos actuales
print("\nLibros en el sistema:")
for libro in libros:
    print(f"Libro: {libro['Nombre']}, Stock: {libro['Stock']}, ID: {libro['ID']}")

print("\nUsuarios registrados:")
for usuario in usuarios:
    print(f"Nombre: {usuario['Nombre']}, ID: {usuario['ID']}")

print("\nPréstamos actuales:")
for prestamo in prestamos:
    print(f"ID Préstamo: {prestamo['ID Prestamo']}, ID Libro: {prestamo['ID Libro']}, ID Usuario: {prestamo['ID Usuario']}")

print("\nMultas actuales:")
for multa in multas:
    print(f"ID Préstamo: {multa['ID Prestamo']}, Monto: {multa['Monto']}, ID Usuario: {multa['ID Usuario']}")

# Eliminar elementos
eliminar_libro(501)
eliminar_prestamo(301)
eliminar_usuario(201)
eliminar_multa(301)

# Mostrar datos tras eliminar
print("\nLibros después de eliminar:")
for libro in libros:
    print(f"Libro: {libro['Nombre']}, Stock: {libro['Stock']}, ID: {libro['ID']}")

print("\nUsuarios después de eliminar:")
for usuario in usuarios:
    print(f"Nombre: {usuario['Nombre']}, ID: {usuario['ID']}")

print("\nPréstamos después de eliminar:")
for prestamo in prestamos:
    print(f"ID Préstamo: {prestamo['ID Prestamo']}, ID Libro: {prestamo['ID Libro']}, ID Usuario: {prestamo['ID Usuario']}")

print("\nMultas después de eliminar:")
for multa in multas:
    print(f"ID Préstamo: {multa['ID Prestamo']}, Monto: {multa['Monto']}, ID Usuario: {multa['ID Usuario']}")
