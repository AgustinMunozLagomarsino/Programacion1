def calcular_factorial(num):
    try:
        # Verifica si el número es un entero positivo
        if not isinstance(num, int):
            raise TypeError("Error: El número debe ser un entero.")
        if num < 0:
            raise ValueError("Error: El número debe ser un entero positivo.")

        # Calcula el factorial
        resultado = 1
        for i in range(1, num + 1):
            resultado *= i
        return resultado

    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)
    except OverflowError:
        print("Error: El número es demasiado grande para calcular su factorial.")

# Ejemplo de uso
try:
    num = int(input("Ingresa un número entero positivo: "))
    factorial = calcular_factorial(num)
    if factorial is not None:
        print(f"El factorial de {num} es: {factorial}")
except ValueError:
    print("Error: Debes ingresar un número entero válido.")
