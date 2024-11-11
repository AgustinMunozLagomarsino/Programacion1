# Clase base
class Operacion:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
    
    def resultado(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")

# Subclase Suma que sobrescribe el método resultado
class Suma(Operacion):
    def resultado(self):
        return self.numero1 + self.numero2

# Subclase Multiplicacion que sobrescribe el método resultado
class Multiplicacion(Operacion):
    def resultado(self):
        return self.numero1 * self.numero2

# Ejemplo de polimorfismo
operaciones = [Suma(10, 5), Multiplicacion(10, 5)]

for operacion in operaciones:
    print(f"Resultado de {operacion.__class__.__name__}: {operacion.resultado()}")
