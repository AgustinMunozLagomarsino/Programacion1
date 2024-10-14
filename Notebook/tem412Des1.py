# Definición de la clase Escritor
class Escritor:
    # Constructor que inicializa el nombre, país y una lista vacía de obras
    def __init__(self, nombre="", pais=""):
        self.nombre = nombre
        self.pais = pais
        self.obras = []

    # Método para mostrar la información del escritor
    def mostrar_info(self):
        print(f"\nEscritor: {self.nombre}")
        print(f"\nPaís: {self.pais}")
        print("\nObras publicadas:")
        for obra in self.obras:
            print(f"- {obra}")

    # Método para agregar una obra a la lista de obras
    def agregar_obra(self, titulo):
        self.obras.append(titulo)
        print(f"\nLa obra '{titulo}' ha sido añadida.")

    # Método para eliminar una obra de la lista si existe
    def eliminar_obra(self, titulo):
        if titulo in self.obras:
            self.obras.remove(titulo)
            print(f"\nLa obra '{titulo}' ha sido eliminada.")
        else:
            print(f"\nLa obra '{titulo}' no está en la lista.")

# Ejemplo de uso básico
nombre_escritor = input("\nIntroduce el nombre del escritor: ")
pais_escritor = input("\nIntroduce el país del escritor: ")

# Crear un objeto Escritor
escritor = Escritor(nombre_escritor, pais_escritor)

# Mostrar información inicial
escritor.mostrar_info()

# Ciclo principal
while True:
    print("\nAcciones:")
    print("1. Añadir obra")
    print("2. Quitar obra")
    print("3. Ver información del escritor")
    print("4. Salir")

    eleccion = input("Elige una opción: ")

    if eleccion == "1":
        titulo = input("Título de la obra: ")
        escritor.agregar_obra(titulo)
    elif eleccion == "2":
        titulo = input("Título de la obra a quitar: ")
        escritor.eliminar_obra(titulo)
    elif eleccion == "3":
        escritor.mostrar_info()
    elif eleccion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida, intenta de nuevo.")
