try:
    # Solicita los dos números enteros al usuario
    num1 = int(input("Ingresa el primer número entero: "))
    num2 = int(input("Ingresa el segundo número entero: "))
    
    # Intenta realizar la división
    resultado = num1 / num2
    print(f"El resultado de la división es: {resultado}")

except ValueError:
    # Maneja el error cuando el usuario no ingresa un número entero
    print("Error: Por favor, ingresa valores numéricos enteros.")

except ZeroDivisionError:
    # Maneja el error cuando el usuario intenta dividir por cero
    print("Error: No se puede dividir entre cero.")
