def realizar_operaciones(lista):
    try:
        # Suma de todos los elementos
        suma = sum(lista)
        print(f"La suma de los valores es: {suma}")

        # Promedio de los elementos
        promedio = suma / len(lista)
        print(f"El promedio de los valores es: {promedio}")

        # Producto de todos los elementos
        producto = 1
        for valor in lista:
            producto *= valor
        print(f"El producto de los valores es: {producto}")

    except ZeroDivisionError:
        print("Error: La lista está vacía, no se puede calcular el promedio.")

    except TypeError:
        print("Error: La lista contiene valores no numéricos.")

    except ValueError:
        print("Error: Hay un valor incorrecto en la lista.")

# Ejemplo de uso
try:
    # Entrada de ejemplo con posibilidad de valores no numéricos
    lista_entrada = [float(x) for x in input("Ingresa una lista de valores separados por comas: ").split(",")]
    realizar_operaciones(lista_entrada)
except ValueError:
    print("Error: Entrada inválida. Asegúrate de ingresar solo números separados por comas.")
