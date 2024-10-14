# Clase Escritor
class Escritor:
    def __init__(self, nombre, pais_origen, fecha_nacimiento, resumen):
        # Inicializa el objeto Escritor con nombre, país de origen, fecha de nacimiento y un resumen.
        self.nombre = nombre
        self.pais_origen = pais_origen
        self.fecha_nacimiento = fecha_nacimiento
        self.resumen = resumen
        self.obras = []  # Almacena las obras del escritor
        self.distinciones = []  # Almacena premios o distinciones

    def añadir_obra(self, obra):
        # Agrega una obra a la lista de obras del escritor.
        self.obras.append(obra)

    def listar_obras(self):
        # Muestra las obras del escritor.
        print(f"\nObras de {self.nombre}:")
        for obra in self.obras:
            print(f"- {obra.titulo}")

    def añadir_distincion(self, premio):
        # Añade una distinción al escritor.
        self.distinciones.append(premio)

    def mostrar_info(self):
        # Muestra la información completa del escritor.
        print(f"\nInformación sobre {self.nombre}:")
        print(f"País de origen: {self.pais_origen}")
        print(f"Nacimiento: {self.fecha_nacimiento}")
        print(f"Resumen: {self.resumen}")
        self.listar_obras()
        if self.distinciones:
            print("Premios obtenidos:")
            for premio in self.distinciones:
                print(f"- {premio}")

# Clase Obra
class Obra:
    def __init__(self, titulo, categoria, codigo, escritor):
        # Inicializa el objeto Obra con título, categoría, código y escritor.
        self.titulo = titulo
        self.categoria = categoria
        self.codigo = codigo
        self.escritor = escritor

    def mostrar_detalle(self):
        # Muestra los detalles de la obra.
        print(f"\nTítulo: {self.titulo}")
        print(f"Categoría: {self.categoria}")
        print(f"Código: {self.codigo}")
        print(f"Escritor: {self.escritor.nombre}")

# Clase Librería
class Libreria:
    def __init__(self):
        # Inicializa una librería vacía.
        self.escritores = {}  # Almacena escritores
        self.obras = {}  # Almacena obras

    def añadir_escritor(self, escritor):
        # Añade un escritor a la librería.
        self.escritores[escritor.nombre] = escritor

    def añadir_obra(self, obra):
        # Añade una obra a la librería y la asocia con su escritor.
        self.obras[obra.titulo] = obra
        obra.escritor.añadir_obra(obra)

    def listar_escritores(self):
        # Muestra todos los escritores registrados.
        print("\nEscritores:")
        for escritor in self.escritores.values():
            print(f"- {escritor.nombre}")

    def listar_obras(self):
        # Muestra todas las obras registradas.
        print("\nObras:")
        for obra in self.obras.values():
            print(f"- {obra.titulo}")

    def buscar_obra(self, titulo_obra):
        # Busca una obra por su título.
        return self.obras.get(titulo_obra, None)

    def buscar_escritor(self, nombre_escritor):
        # Busca un escritor por su nombre.
        return self.escritores.get(nombre_escritor, None)

    def buscar_obras_por_escritor(self, nombre_escritor):
        # Busca todas las obras de un escritor.
        escritor = self.buscar_escritor(nombre_escritor)
        return escritor.obras if escritor else []

    def buscar_escritor_por_obra(self, titulo_obra):
        # Busca el escritor de una obra.
        obra = self.buscar_obra(titulo_obra)
        return obra.escritor if obra else None

# Crear una librería
libreria = Libreria()

# Crear escritores y obras
escritor1 = Escritor("Ana Sánchez", "Argentina", "15/03/1980", "Autora de cuentos infantiles.")
escritor2 = Escritor("Luis Fernández", "España", "28/07/1972", "Escritor de novelas históricas.")

obra1 = Obra("El viaje", "Cuento", "123ABC", escritor1)
obra2 = Obra("Historias del pasado", "Novela", "456DEF", escritor2)

# Añadir escritores y obras a la librería
libreria.añadir_escritor(escritor1)
libreria.añadir_escritor(escritor2)
libreria.añadir_obra(obra1)
libreria.añadir_obra(obra2)

# Buscar y mostrar información de una obra
titulo = "El viaje"
obra_encontrada = libreria.buscar_obra(titulo)
if obra_encontrada:
    print(f"\n** Obra encontrada: {titulo} **")
    obra_encontrada.mostrar_detalle()
else:
    print(f"\n** No se encontró la obra '{titulo}' **")

# Buscar y mostrar información de un escritor
nombre = "Luis Fernández"
escritor_encontrado = libreria.buscar_escritor(nombre)
if escritor_encontrado:
    print(f"\n** Escritor encontrado: {nombre} **")
    escritor_encontrado.mostrar_info()
else:
    print(f"\n** No se encontró el escritor '{nombre}' **")

# Buscar todas las obras de un escritor
obras_de_escritor = libreria.buscar_obras_por_escritor("Ana Sánchez")
if obras_de_escritor:
    print(f"\n** Obras de Ana Sánchez: **")
    for obra in obras_de_escritor:
        print(f"- {obra.titulo}")
else:
    print(f"\n** No se encontraron obras de Ana Sánchez **")

# Buscar escritor de una obra
escritor_por_obra = libreria.buscar_escritor_por_obra("Historias del pasado")
if escritor_por_obra:
    print(f"\n** Escritor de 'Historias del pasado': {escritor_por_obra.nombre} **")
else:
    print(f"\n** No se encontró el escritor de 'Historias del pasado' **")
