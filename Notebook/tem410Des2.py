# Inicializar listas vacías para almacenar los héroes y las armas
heroes = []
inventario_armas = []

# Función para agregar un arma al inventario
def agregar_arma(tipo, poder):
    # Crear un diccionario con la información del arma
    nueva_arma = {
        "tipo": tipo,
        "poder": poder
    }
    # Añadir el arma a la lista de armas
    inventario_armas.append(nueva_arma)

# Función para crear un héroe
def agregar_heroe(nombre, salud, fuerza, habilidad_especial, arma_asignada):
    # Buscar si el arma asignada está disponible en el inventario de armas
    arma_disponible = next((arma for arma in inventario_armas if arma["tipo"] == arma_asignada), None)
    if not arma_disponible:
        # Mostrar mensaje de error si el arma no se encuentra
        print("Error: El arma asignada no existe en el inventario.")
        return

    # Crear un diccionario con la información del héroe
    nuevo_heroe = {
        "nombre": nombre,
        "salud": salud,
        "fuerza": fuerza,
        "habilidad_especial": habilidad_especial,
        "arma": arma_disponible
    }
    # Añadir el héroe a la lista de héroes
    heroes.append(nuevo_heroe)

# Función para mostrar la lista de héroes creados
def listar_heroes():
    print("\nHéroes:")
    for heroe in heroes:
        # Mostrar la información del héroe junto con el arma que lleva
        print(f"{heroe['nombre']} - Salud: {heroe['salud']} - Fuerza: {heroe['fuerza']} - Habilidad: {heroe['habilidad_especial']} - Arma: {heroe['arma']['tipo']} (Poder: {heroe['arma']['poder']})")

# Función para mostrar la lista de armas disponibles
def listar_armas():
    print("\nInventario de armas:")
    for arma in inventario_armas:
        # Mostrar la información del arma
        print(f"{arma['tipo']} - Poder: {arma['poder']}")

# Crear varias armas
agregar_arma("Espada larga", 10)
agregar_arma("Báculo mágico", 8)
agregar_arma("Ballesta", 12)

# Crear varios héroes con armas asignadas
agregar_heroe("Paladín", 120, 25, "Aura protectora", "Espada larga")
agregar_heroe("Hechicero", 75, 18, "Rayo arcano", "Báculo mágico")
agregar_heroe("Cazador", 85, 22, "Tiro certero", "Ballesta")

# Mostrar los héroes y armas actuales
listar_heroes()
listar_armas()

# Agregar nuevos personajes con habilidades y armas
agregar_heroe("Ninja", 90, 28, "Ataque sorpresa", "Espada larga")

# Mostrar los héroes y armas actualizados
listar_heroes()
listar_armas()
print("este trabajo fue realizado con ayuda de Anthony martinelli")