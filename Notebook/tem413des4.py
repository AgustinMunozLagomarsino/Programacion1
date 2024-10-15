class Autor:
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre      # Atributo privado
        self.__nacionalidad = nacionalidad  # Atributo privado
        self.__libros = []  # Atributo privado para almacenar los libros del autor

    # Getter para 'nombre'
    @property
    def nombre(self):
        return self.__nombre

    # Setter para 'nombre'
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    # Getter para 'nacionalidad'
    @property
    def nacionalidad(self):
        return self.__nacionalidad

    # Setter para 'nacionalidad'
    @nacionalidad.setter
    def nacionalidad(self, nueva_nacionalidad):
        self.__nacionalidad = nueva_nacionalidad

    def agregar_libro(self, libro):
        """Método para agregar un libro a la lista de libros del autor."""
        self.__libros.append(libro)

    def obtener_libros(self):
        """Método para obtener una lista de los libros del autor."""
        return self.__libros.copy()  # Devuelve una copia para evitar modificaciones externas

    def mostrar_libros(self):
        """Método para mostrar los libros escritos por el autor."""
        if self.__libros:
            print(f"Libros escritos por {self.nombre}:")
            for libro in self.__libros:
                print(f"- {libro}")
        else:
            print(f"{self.nombre} no tiene libros registrados.")

# Función que devuelve la lista de títulos de libros del autor
def obtener_titulos_autor(autor):
    """Función que recibe un objeto Autor y devuelve la lista de títulos de libros escritos por él."""
    return autor.obtener_libros()  # Accede a la lista a través del método 'obtener_libros'
    
# Ejemplo de uso:
autor = Autor("Gabriel García Márquez", "Colombiana")
autor.agregar_libro("Cien años de soledad")
autor.agregar_libro("El amor en los tiempos del cólera")

# Obtener la lista de libros del autor mediante la función
lista_libros = obtener_titulos_autor(autor)
print(lista_libros)
