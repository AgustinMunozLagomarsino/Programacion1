import datetime

# Función para agregar un registro de préstamo al archivo prestamos.txt
def agregar_prestamo(nombre_libro, nombre_prestatario):
    # Obtener la fecha actual en formato "dd-mm-yyyy"
    fecha_prestamo = datetime.datetime.now().strftime("%d-%m-%Y")
    
    # Abrir el archivo en modo append (agregar) para no sobrescribir el contenido existente
    with open("prestamos.txt", "a") as archivo:
        # Formatear el registro de préstamo
        registro = f"Libro: {nombre_libro}, Prestatario: {nombre_prestatario}, Fecha: {fecha_prestamo}\n"
        # Escribir el registro en el archivo
        archivo.write(registro)
    
    print("Registro de préstamo agregado exitosamente.")

# Solicitar información del usuario para el registro de préstamo
nombre_libro = input("Ingrese el nombre del libro: ")
nombre_prestatario = input("Ingrese el nombre del prestatario: ")

# Agregar el registro de préstamo al archivo
agregar_prestamo(nombre_libro, nombre_prestatario)
