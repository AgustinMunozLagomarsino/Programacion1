# Clase base Escritor
class Escritor:
    def __init__(self, nombre, genero_literario):
        self.nombre = nombre
        self.genero_literario = genero_literario

    def escribir(self):
        return f"{self.nombre} está escribiendo una obra de {self.genero_literario}."

# Clase base Academico
class Academico:
    def __init__(self, especialidad, institucion):
        self.especialidad = especialidad
        self.institucion = institucion

    def investigar(self):
        return f"{self.especialidad} es la especialidad en la que investiga en {self.institucion}."

# Clase derivada EscritorAcademico que hereda de Escritor y Academico
class EscritorAcademico(Escritor, Academico):
    def __init__(self, nombre, genero_literario, especialidad, institucion):
        # Inicializamos ambas clases base
        super().__init__(nombre, genero_literario)
        Academico.__init__(self, especialidad, institucion)

    def publicar_articulo(self, titulo_articulo):
        return (f"{self.nombre} ha publicado un artículo titulado '{titulo_articulo}' en el área de "
                f"{self.especialidad} en {self.institucion}.")

# Ejemplo de uso
escritor_academico = EscritorAcademico("Julio Cortázar", "Ensayo", "Literatura Comparada", "Universidad de Buenos Aires")
print(escritor_academico.escribir())               # Método de Escritor
print(escritor_academico.investigar())             # Método de Academico
print(escritor_academico.publicar_articulo("Análisis literario de Borges y su influencia"))
