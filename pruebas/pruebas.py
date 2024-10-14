"""
# Titulo: Desafío 2
# Autor: Anthony Martinelli
# Fecha: 13/10/2024
# Descripción:
# Crea una clase `Libro` con atributos como título, género e ISBN. ¿Cómo
# podrías relacionar esta clase con la clase `Autor`?
"""

# Clase Autor
class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        print(f"\nLibros de {self.nombre}:")
        for libro in self.libros:
            print(f"- {libro.titulo}")

# Clase Libro
class Libro:
    def __init__(self, titulo, genero, isbn, autor):
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn
        self.autor = autor

    def mostrar_detalle(self):
        print(f"\nTítulo: {self.titulo}")
        print(f"Género: {self.genero}")
        print(f"ISBN: {self.isbn}")
        print(f"Autor: {self.autor.nombre}")

# Crear autores y libros
autor1 = Autor("Juan Pérez", "Mexicano")
autor2 = Autor("María García", "Española")

libro1 = Libro("La vida es un sueño", "Ficción", "1234567890", autor1)
libro2 = Libro("La casa de los espíritus", "Ficción", "9876543210", autor1)
libro3 = Libro("El amor en los tiempos del cólera", "Ficción", "1111111111", autor2)

# Agregar libros a los autores
autor1.agregar_libro(libro1)
autor1.agregar_libro(libro2)
autor2.agregar_libro(libro3)

# Mostrar libros de un autor
autor1.mostrar_libros()

# Mostrar detalles de un libro
libro1.mostrar_detalle()

# Buscar libros por autor
def buscar_libros_por_autor(autores, nombre_autor):
    for autor in autores:
        if autor.nombre == nombre_autor:
            return autor.libros
    return []

# Buscar autores por libro
def buscar_autores_por_libro(libros, titulo_libro):
    for libro in libros:
        if libro.titulo == titulo_libro:
            return libro.autor
    return None

# Crear listas de autores y libros
autores = [autor1, autor2]
libros = [libro1, libro2, libro3]

# Buscar libros por autor
libros_autor1 = buscar_libros_por_autor(autores, "Juan Pérez")
for libro in libros_autor1:
    libro.mostrar_detalle()

# Buscar autores por libro
autor_libro1 = buscar_autores_por_libro(libros, "La vida es un sueño")
if autor_libro1:
    autor_libro1.mostrar_libros()