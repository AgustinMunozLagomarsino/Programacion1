# Clase Escritor
class Escritor:
    def __init__(self, nombre, origen):
        # Inicializa un escritor con su nombre y país de origen.
        self.nombre = nombre
        self.origen = origen
        self.obras = []  # Lista para almacenar las obras del escritor

    def agregar_obra(self, obra):
        # Añade una obra a la lista de obras del escritor.
        self.obras.append(obra)

    def eliminar_obra(self, titulo_obra):
        # Elimina una obra por su título.
        self.obras = [obra for obra in self.obras if obra.titulo != titulo_obra]

    def mostrar_obras(self):
        # Muestra todas las obras del escritor.
        print(f"\nObras de {self.nombre}:")
        for obra in self.obras:
            print(f"- {obra.titulo}")

# Clase Obra
class Obra:
    def __init__(self, titulo, categoria, codigo, escritor):
        # Inicializa una obra con su título, categoría, código y escritor.
        self.titulo = titulo
        self.categoria = categoria
        self.codigo = codigo
        self.escritor = escritor

    def detalles(self):
        # Muestra los detalles de la obra.
        print(f"\nTítulo: {self.titulo}")
        print(f"Categoría: {self.categoria}")
        print(f"Código: {self.codigo}")
        print(f"Escrito por: {self.escritor.nombre}")

# Clase Biblioteca
class Coleccion:
    def __init__(self):
        # Inicializa la colección con diccionarios vacíos de escritores y obras.
        self.escritores = {}
        self.obras = {}

    def añadir_escritor(self, escritor):
        # Añade un escritor a la colección.
        self.escritores[escritor.nombre] = escritor

    def añadir_obra(self, obra):
        # Añade una obra a la colección y la asocia con su escritor.
        self.obras[obra.titulo] = obra
        obra.escritor.agregar_obra(obra)

    def mostrar_escritores(self):
        # Muestra todos los escritores en la colección.
        print("\nEscritores:")
        for escritor in self.escritores.values():
            print(f"- {escritor.nombre}")

    def mostrar_obras(self):
        # Muestra todas las obras en la colección.
        print("\nObras:")
        for obra in self.obras.values():
            print(f"- {obra.titulo}")

    def buscar_obras_por_escritor(self, nombre_escritor):
        # Busca obras de un escritor por su nombre.
        if nombre_escritor in self.escritores:
            return self.escritores[nombre_escritor].obras
        return []

    def buscar_escritor_por_obra(self, titulo_obra):
        # Busca el escritor de una obra por su título.
        if titulo_obra in self.obras:
            return self.obras[titulo_obra].escritor
        return None

# Crear colección
coleccion = Coleccion()

# Crear escritores y obras
escritor1 = Escritor("Gabriel García Márquez", "Colombiano")
escritor2 = Escritor("Julio Cortázar", "Argentino")

obra1 = Obra("Cien años de soledad", "Novela", "1234567890", escritor1)
obra2 = Obra("Crónica de una muerte anunciada", "Novela", "9876543210", escritor1)
obra3 = Obra("Rayuela", "Novela", "1111111111", escritor2)

# Añadir escritores y obras a la colección
coleccion.añadir_escritor(escritor1)
coleccion.añadir_escritor(escritor2)
coleccion.añadir_obra(obra1)
coleccion.añadir_obra(obra2)
coleccion.añadir_obra(obra3)

# Mostrar escritores y obras
coleccion.mostrar_escritores()
coleccion.mostrar_obras()

# Buscar obras por escritor
obras_escritor1 = coleccion.buscar_obras_por_escritor("Gabriel García Márquez")
for obra in obras_escritor1:
    obra.detalles()

# Buscar escritor por obra
escritor_obra1 = coleccion.buscar_escritor_por_obra("Rayuela")
if escritor_obra1:
    escritor_obra1.mostrar_obras()

# Eliminar una obra de la colección
coleccion.obras.pop("Crónica de una muerte anunciada")
escritor1.eliminar_obra("Crónica de una muerte anunciada")

# Mostrar escritores y obras después de eliminar una obra
print("\nObras de la colección luego de eliminar una:")
coleccion.mostrar_escritores()
coleccion.mostrar_obras()
