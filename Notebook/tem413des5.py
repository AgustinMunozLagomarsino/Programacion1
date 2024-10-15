class Autor:
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre      # Atributo privado
        self.__nacionalidad = nacionalidad  # Atributo privado
        self.__libros = []  # Atributo privado para almacenar los libros del autor

    # Getter para 'nombre'
    @property
    def nombre(self):
        return self.__nombre

    # Getter para 'nacionalidad'
    @property
    def nacionalidad(self):
        return self.__nacionalidad

    def agregar_libro(self, libro):
        """Método para agregar un libro a la lista de libros del autor."""
        self.__libros.append(libro)

    def obtener_libros(self):
        """Método para obtener una lista de los libros del autor."""
        return self.__libros.copy()  # Devuelve una copia para evitar modificaciones externas

    def contar_libros(self):
        """Método para obtener el número de libros del autor."""
        return len(self.__libros)  # Devuelve la cantidad de libros escritos por el autor

def autor_con_mas_libros(lista_autores):
    """Función que recibe una lista de objetos Autor y devuelve el autor que ha escrito más libros."""
    if not lista_autores:
        return None  # Si la lista está vacía, devuelve None
    
    # Inicializar el autor con más libros como el primero de la lista
    autor_max = lista_autores[0]
    
    # Recorrer los autores para encontrar el que tiene más libros
    for autor in lista_autores[1:]:
        if autor.contar_libros() > autor_max.contar_libros():
            autor_max = autor
    
    return autor_max

# Creando varios autores
autor1 = Autor("Gabriel García Márquez", "Colombiana")
autor2 = Autor("Isabel Allende", "Chilena")
autor3 = Autor("Mario Vargas Llosa", "Peruana")

# Agregando libros a los autores
autor1.agregar_libro("Cien años de soledad")
autor1.agregar_libro("El amor en los tiempos del cólera")

autor2.agregar_libro("La casa de los espíritus")
autor2.agregar_libro("Paula")
autor2.agregar_libro("Eva Luna")

autor3.agregar_libro("La ciudad y los perros")

# Lista de autores
lista_autores = [autor1, autor2, autor3]

# Obtener el autor con más libros
autor_mas_libros = autor_con_mas_libros(lista_autores)

if autor_mas_libros:
    print(f"El autor con más libros es {autor_mas_libros.nombre}, con {autor_mas_libros.contar_libros()} libros.")
else:
    print("La lista de autores está vacía.")
