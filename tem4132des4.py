import math

# Clase base
class Figura:
    def area(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")

# Subclase Circulo que sobrescribe el método area
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

# Subclase Cuadrado que sobrescribe el método area
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

# Ejemplo de polimorfismo
figuras = [Circulo(5), Cuadrado(4)]

for figura in figuras:
    print(f"Área de {figura.__class__.__name__}: {figura.area()}")
