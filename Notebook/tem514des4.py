import math

# Definición de la excepción personalizada
class NegativeNumberError(Exception):
    def __init__(self, message="Error: No se puede calcular la raíz cuadrada de un número negativo."):
        self.message = message
        super().__init__(self.message)

# Función para calcular la raíz cuadrada
def calcular_raiz_cuadrada(num):
    try:
        if num < 0:
            # Lanza la excepción personalizada si el número es negativo
            raise NegativeNumberError()
        return math.sqrt(num)
    except NegativeNumberError as e:
        print(e)

# Ejemplo de uso
try:
    num = float(input("Ingresa un número para calcular su raíz cuadrada: "))
    resultado = calcular_raiz_cuadrada(num)
    if resultado is not None:
        print(f"La raíz cuadrada de {num} es: {resultado}")
except ValueError:
    print("Error: Debes ingresar un valor numérico.")
