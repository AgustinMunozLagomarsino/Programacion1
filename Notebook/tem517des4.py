def mostrar_prestamos(archivo="prestamos.txt"):
    """Lee y muestra todos los registros de préstamos."""
    try:
        with open(archivo, "r") as f:
            prestamos = f.readlines()
            
            if not prestamos:
                print("No hay registros de préstamos.")
                return None

            print("Registros de préstamos:")
            for i, linea in enumerate(prestamos, start=1):
                print(f"{i}. {linea.strip()}")
            
            return prestamos

    except FileNotFoundError:
        print(f"El archivo '{archivo}' no fue encontrado.")
        return None


def eliminar_prestamo(archivo="prestamos.txt"):
    """Elimina un registro de préstamo seleccionado por el usuario."""
    prestamos = mostrar_prestamos(archivo)
    
    if prestamos is None:
        return

    try:
        seleccion = int(input("Ingrese el número del préstamo que desea eliminar: "))
        
        if 1 <= seleccion <= len(prestamos):
            prestamos.pop(seleccion - 1)  # Eliminar el préstamo seleccionado

            # Guardar el archivo actualizado sin el préstamo eliminado
            with open(archivo, "w") as f:
                for prestamo in prestamos:
                    f.write(prestamo)
            
            print("El registro de préstamo ha sido eliminado correctamente.")
        else:
            print("Selección inválida. Por favor, ingrese un número válido.")
    
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")

# Ejemplo de uso
eliminar_prestamo()
