# Clase base
class Autor:
    def biografia(self):
        return "Esta es la biografía general de un autor."

# Subclase Escritor que sobrescribe el método biografia
class Escritor(Autor):
    def biografia(self):
        return "Esta es la biografía específica de un escritor."

# Instancia de la clase Escritor
escritor = Escritor()

# Acceso al método biografia de ambas clases
print("Biografía en la clase Escritor:", escritor.biografia())           # Método sobrescrito en Escritor
print("Biografía en la clase Autor:", super(Escritor, escritor).biografia())  # Método de la clase Autor
