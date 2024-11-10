# Clase base Autor
class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def biografia(self):
        return f"{self.nombre} es un autor de {self.nacionalidad}."

# Subclase Poeta que hereda de Autor y agrega el atributo tipo_de_poesia
class Poeta(Autor):
    def __init__(self, nombre, nacionalidad, tipo_de_poesia):
        # Llamada al constructor de la clase base para inicializar nombre y nacionalidad
        super().__init__(nombre, nacionalidad)
        self.tipo_de_poesia = tipo_de_poesia

    def biografia(self):
        # Extiende el método biografia para incluir el tipo de poesía
        return (f"{super().biografia()} Especializado en poesía {self.tipo_de_poesia}.")

# Ejemplo de uso
poeta = Poeta("Pablo Neruda", "Chile", "lírica")
print(poeta.biografia())
