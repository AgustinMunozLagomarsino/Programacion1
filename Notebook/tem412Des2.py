# Clase Escritor
class Escritor:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais
        self.obras = []

    def agregar_obra(self, obra):
        self.obras.append(obra)

    def mostrar_obras(self):
        print(f"\nObras de {self.nombre}:")
        for obra in self.obras:
            print(f"- {obra.titulo}")

# Clase Obra
class Obra:
    def __init__(self, titulo, categoria, ISBN, escritor):
        self.titulo = titulo
        self.categoria = categoria
        self.ISBN = ISBN
        self.escritor = escritor

    def mostrar_info(self):
        print(f"\nTítulo: {self.titulo}")
        print(f"Categoría: {self.categoria}")
        print(f"ISBN: {self.ISBN}")
        print(f"Escrito por: {self.escritor.nombre}")

# Crear escritores y obras
escritor1 = Escritor("Carlos Fuentes", "Mexicano")
escritor2 = Escritor("Isabel Allende", "Chilena")

obra1 = Obra("Aura", "Novela", "1020304050", escritor1)
obra2 = Obra("La muerte de Artemio Cruz", "Novela", "1122334455", escritor1)
obra3 = Obra("Paula", "Memoria", "2233445566", escritor2)

# Asignar obras a escritores
escritor1.agregar_obra(obra1)
escritor1.agregar_obra(obra2)
escritor2.agregar_obra(obra3)

# Mostrar obras de un escritor
escritor1.mostrar_obras()

# Mostrar información de una obra
obra1.mostrar_info()

# Función para buscar obras por escritor
def buscar_obras_por_escritor(escritores, nombre_escritor):
    for escritor in escritores:
        if escritor.nombre == nombre_escritor:
            return escritor.obras
    return []

# Función para buscar escritor por obra
def buscar_escritor_por_obra(obras, titulo_obra):
    for obra in obras:
        if obra.titulo == titulo_obra:
            return obra.escritor
    return None

# Crear listas de escritores y obras
escritores = [escritor1, escritor2]
obras = [obra1, obra2, obra3]

# Buscar obras por escritor
obras_escritor1 = buscar_obras_por_escritor(escritores, "Carlos Fuentes")
for obra in obras_escritor1:
    obra.mostrar_info()

# Buscar escritor por obra
escritor_obra1 = buscar_escritor_por_obra(obras, "Aura")
if escritor_obra1:
    escritor_obra1.mostrar_obras()
