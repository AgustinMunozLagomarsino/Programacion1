# Clase base
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def detalles(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"

# Subclase LibroEspecializado
class LibroEspecializado(Libro):
    def __init__(self, titulo, autor, campo_estudio, nivel_especializacion):
        # Llamada al constructor de la clase base para inicializar título y autor
        super().__init__(titulo, autor)
        self.campo_estudio = campo_estudio
        self.nivel_especializacion = nivel_especializacion

    def detalles(self):
        # Sobrescribimos el método detalles para incluir los nuevos atributos
        return (f"Título: {self.titulo}, Autor: {self.autor}, "
                f"Campo de estudio: {self.campo_estudio}, "
                f"Nivel de especialización: {self.nivel_especializacion}")

# Crear una instancia de LibroEspecializado
libro_especializado = LibroEspecializado(
    titulo="Introducción a la Física Cuántica", 
    autor="Dr. María López", 
    campo_estudio="Física", 
    nivel_especializacion="Intermedio"
)

# Mostrar detalles del libro especializado
print(libro_especializado.detalles())
