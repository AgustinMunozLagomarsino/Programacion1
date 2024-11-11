def buscar_libros_por_autor(nombre_autor, archivo="libros.txt"):
    try:
        with open(archivo, "r") as f:
            libros_encontrados = []
            
            for linea in f:
                linea = linea.strip()  # Eliminar espacios en blanco y saltos de línea
                if "-" in linea:
                    titulo, autor = linea.split(" - ")
                    autor = autor.strip()
                    
                    # Si el autor coincide, agrega el título del libro a la lista
                    if autor.lower() == nombre_autor.lower():
                        libros_encontrados.append(titulo.strip())
            
            # Mostrar resultados según si se encontraron libros o no
            if libros_encontrados:
                print(f"Libros de {nombre_autor}:")
                for libro in libros_encontrados:
                    print(f"- {libro}")
            else:
                print(f"No se encontraron libros para el autor '{nombre_autor}'.")

    except FileNotFoundError:
        print(f"El archivo '{archivo}' no fue encontrado.")

# Ejemplo de uso
nombre_autor = input("Ingrese el nombre del autor: ")
buscar_libros_por_autor(nombre_autor)
