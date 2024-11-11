def determinar_mayor(num1, num2, num3):
    if num1 == num2 == num3:
        print("Todos los números son iguales.")
    elif num1 >= num2 and num1 >= num3:
        print(f"El número mayor es: {num1}")
    elif num2 >= num1 and num2 >= num3:
        print(f"El número mayor es: {num2}")
    else:
        print(f"El número mayor es: {num3}")

# Solicita los tres números al usuario y verifica si son enteros
try:
    num1 = int(input("Ingresa el primer número entero: "))
    num2 = int(input("Ingresa el segundo número entero: "))
    num3 = int(input("Ingresa el tercer número entero: "))
    # Llama a la función para determinar el mayor
    determinar_mayor(num1, num2, num3)

except ValueError:
    print("Error: Por favor, ingresa solo números enteros.")
