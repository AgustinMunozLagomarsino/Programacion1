# Clase Escritor
class Escritor:
    def __init__(self, nombre, pais, nacimiento, resumen):
        # Inicializa con nombre, país de origen, fecha de nacimiento y un resumen.
        self.nombre = nombre
        self.pais = pais
        self.nacimiento = nacimiento
        self.resumen = resumen
        self.obras = []  # Almacena las obras del escritor
        self.distinciones = []  # Guarda premios o distinciones

    def agregar_obra(self, obra):
        # Añade una obra a la lista del escritor.
        self.obras.append(obra)

    def mostrar_obras(self):
        # Muestra todas las obras.
        print(f"\nObras de {self.nombre}:")
        for obra in self.obras:
            print(f"- {obra.titulo}")

    def eliminar_obra(self, titulo_obra):
        # Elimina una obra por su título.
        self.obras = [obra for obra in self.obras if obra.titulo != titulo_obra]

    def agregar_distincion(self, premio):
        # Añade un premio o distinción.
        self.distinciones.append(premio)

    def mostrar_distinciones(self):
        # Muestra los premios obtenidos.
        print(f"\nPremios obtenidos por {self.nombre}:")
        for premio in self.distinciones:
            print(f"- {premio}")

    def mostrar_resumen(self):
        # Muestra el resumen o biografía del escritor.
        print(f"\nResumen de {self.nombre}: {self.resumen}")

    def mostrar_info_completa(self):
        # Muestra toda la información del escritor.
        print(f"\nInformación sobre {self.nombre}:")
        print(f"Nombre: {self.nombre}")
        print(f"País: {self.pais}")
        print(f"Fecha de nacimiento: {self.nacimiento}")
        self.mostrar_resumen()
        self.mostrar_obras()
        self.mostrar_distinciones()

# Clase Obra
class Obra:
    def __init__(self, titulo, categoria, codigo, escritor):
        # Inicializa una obra con título, categoría, código y su autor.
        self.titulo = titulo
        self.categoria = categoria
        self.codigo = codigo
        self.escritor = escritor

    def mostrar_detalles(self):
        # Muestra los detalles de la obra.
        print(f"\nTítulo: {self.titulo}")
        print(f"Categoría: {self.categoria}")
        print(f"Código: {self.codigo}")
        print(f"Escritor: {self.escritor.nombre}")

# Clase Librería
class Libreria:
    def __init__(self):
        # Inicializa la librería con diccionarios para autores y obras.
        self.escritores = {}  # Guarda escritores
        self.obras = {}  # Guarda las obras

    def registrar_escritor(self, escritor):
        # Registra un nuevo escritor.
        self.escritores[escritor.nombre] = escritor

    def registrar_obra(self, obra):
        # Registra una nueva obra y la asocia con su autor.
        self.obras[obra.titulo] = obra
        obra.escritor.agregar_obra(obra)

    def mostrar_escritores(self):
        # Muestra todos los escritores registrados.
        print("\nLista de escritores:")
        for escritor in self.escritores.values():
            print(f"- {escritor.nombre}")

    def mostrar_obras(self):
        # Muestra todas las obras registradas.
        print("\nLista de obras:")
        for obra in self.obras.values():
            print(f"- {obra.titulo}")

    def buscar_obras_por_escritor(self, nombre_escritor):
        # Busca obras de un escritor específico.
        if nombre_escritor in self.escritores:
            return self.escritores[nombre_escritor].obras
        return []

    def buscar_escritor_por_obra(self, titulo_obra):
        # Busca el autor de una obra.
        if titulo_obra in self.obras:
            return self.obras[titulo_obra].escritor
        return None

# Crear una librería
libreria = Libreria()

# Crear escritores y obras
escritor1 = Escritor("Ana Gómez", "Chile", "10/10/1985", "Autora reconocida de novelas románticas.")
escritor2 = Escritor("Carlos Ruiz", "España", "22/07/1970", "Autor de literatura contemporánea.")

obra1 = Obra("La espera", "Novela", "ABC123", escritor1)
obra2 = Obra("Recuerdos del ayer", "Cuento", "XYZ987", escritor1)
obra3 = Obra("Los años perdidos", "Novela", "LMN456", escritor2)

# Registrar escritores y obras en la librería
libreria.registrar_escritor(escritor1)
libreria.registrar_escritor(escritor2)
libreria.registrar_obra(obra1)
libreria.registrar_obra(obra2)
libreria.registrar_obra(obra3)

# Añadir premios a los escritores
escritor1.agregar_distincion("Premio Nacional de Novela")
escritor2.agregar_distincion("Premio Internacional de Literatura")

# Mostrar escritores y obras
libreria.mostrar_escritores()
libreria.mostrar_obras()

# Mostrar información completa de los escritores
escritor1.mostrar_info_completa()
escritor2.mostrar_info_completa()
