def verificar_multiplos(n):
    numeros = [2, 3, 5, 7, 9, 10, 11]
    for numero in numeros:
        if n % numero == 0:
            print(f"¿Es {n} múltiplo de {numero}? Sí")
        else:
            print(f"¿Es {n} múltiplo de {numero}? No")

# Probar con el número dado en el ejemplo (30)
verificar_multiplos(30)
