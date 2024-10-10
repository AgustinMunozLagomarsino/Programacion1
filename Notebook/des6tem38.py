def es_primo(n):
    """
    Verifica si un número es primo.

    Parámetros:
    n (int): El número a verificar.

    Retorna:
    bool: True si el número es primo, False en caso contrario.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def contar_primos(lista):
    """
    Cuenta la cantidad de números primos en una lista.

    Parámetros:
    lista (list): Lista de enteros.

    Retorna:
    int: La cantidad de números primos en la lista.
    """
    return sum(1 for num in lista if es_primo(num))


def main():
    """
    Función principal que integra las funciones de verificación y conteo de números primos.
    """
    # Ejemplo de lista de números
    numeros = [2, 3, 4, 5, 10, 11, 13, 15, 17, 18, 19, 20]

    # Verificación de si un número es primo
    numero_a_verificar = 19
    if es_primo(numero_a_verificar):
        print(f"El número {numero_a_verificar} es primo.")
    else:
        print(f"El número {numero_a_verificar} no es primo.")

    # Conteo de números primos en la lista
    cantidad_primos = contar_primos(numeros)
    print(f"Hay {cantidad_primos} números primos en la lista.")


if __name__ == "__main__":
    main()

