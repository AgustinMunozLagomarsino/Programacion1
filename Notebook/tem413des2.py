class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.libros = []  # Lista para almacenar los libros del autor

    def agregar_libro(self, libro):
        """Método para agregar un libro a la lista de libros del autor."""
        self.libros.append(libro)

    def mostrar_libros(self):
        """Método para mostrar los libros escritos por el autor."""
        if self.libros:
            print(f"Libros escritos por {self.nombre}:")
            for libro in self.libros:
                print(f"- {libro}")
        else:
            print(f"{self.nombre} no tiene libros registrados.")

# Ejemplo de uso:
autor = Autor("Gabriel García Márquez", "Colombiana")
autor.agregar_libro("Cien años de soledad")
autor.agregar_libro("El amor en los tiempos del cólera")

autor.mostrar_libros()
