class Autor:
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre      # Atributo privado
        self.__nacionalidad = nacionalidad  # Atributo privado
        self.libros = []  # Lista para almacenar los libros del autor

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

# Usando los getters
print(autor.nombre)          # Gabriel García Márquez
print(autor.nacionalidad)    # Colombiana

# Cambiando los atributos usando los setters
autor.nombre = "Isabel Allende"
autor.nacionalidad = "Chilena"

# Verificando el cambio
print(autor.nombre)          # Isabel Allende
print(autor.nacionalidad)    # Chilena

# Agregando libros
autor.agregar_libro("La casa de los espíritus")
autor.agregar_libro("Paula")

# Mostrando los libros
autor.mostrar_libros()
