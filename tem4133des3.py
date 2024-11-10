# Clase base Libro
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def informacion(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"

# Subclase LibroDigital que hereda de Libro y añade atributos específicos
class LibroDigital(Libro):
    def __init__(self, titulo, autor, formato, tamaño_archivo):
        # Llamada al constructor de la clase base para inicializar titulo y autor
        super().__init__(titulo, autor)
        self.formato = formato
        self.tamaño_archivo = tamaño_archivo

    def informacion(self):
        # Extiende el método informacion para incluir formato y tamaño del archivo
        return (f"{super().informacion()}, Formato: {self.formato}, "
                f"Tamaño del archivo: {self.tamaño_archivo} MB")

# Subclase EBook que sobrescribe el método informacion para mostrar enlaces de descarga
class EBook(LibroDigital):
    def __init__(self, titulo, autor, formato, tamaño_archivo, enlace_descarga):
        # Llamada al constructor de la clase LibroDigital
        super().__init__(titulo, autor, formato, tamaño_archivo)
        self.enlace_descarga = enlace_descarga

    def informacion(self):
        # Sobrescribe el método informacion para incluir enlace de descarga
        return (f"{super().informacion()}, Enlace de descarga: {self.enlace_descarga}")

# Ejemplo de uso
ebook = EBook("1984", "George Orwell", "EPUB", 1.2, "https://descarga-1984.com")
print(ebook.informacion())
