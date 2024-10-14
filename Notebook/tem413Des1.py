class Libro:
    def __init__(self, titulo, autor, isbn):
        # Atributos privados
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
    
    # Métodos getter para los atributos
    def get_titulo(self):
        return self.__titulo
    
    def get_autor(self):
        return self.__autor
    
    def get_isbn(self):
        return self.__isbn
    
    # Métodos setter para los atributos
    def set_titulo(self, titulo):
        self.__titulo = titulo
    
    def set_autor(self, autor):
        self.__autor = autor
    
    def set_isbn(self, isbn):
        self.__isbn = isbn

# Ejemplo de uso:
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "978-3-16-148410-0")
print(libro1.get_titulo(), libro1.get_autor(), libro1.get_isbn())
