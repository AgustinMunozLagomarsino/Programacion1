def verificar_multiplos(numero):
    print("¿Es", numero, "múltiplo de 2?", numero % 2 == 0)
    print("¿Es", numero, "múltiplo de 3?", numero % 3 == 0)
    print("¿Es", numero, "múltiplo de 5?", numero % 5 == 0)
    print("¿Es", numero, "múltiplo de 7?", numero % 7 == 0)
    print("¿Es", numero, "múltiplo de 9?", numero % 9 == 0)
    print("¿Es", numero, "múltiplo de 10?", numero % 10 == 0)
    print("¿Es", numero, "múltiplo de 11?", numero % 11 == 0)

numero_dado = 30
verificar_multiplos(numero_dado)
