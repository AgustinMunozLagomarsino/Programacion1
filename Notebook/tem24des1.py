def ordenar_tres_numeros(a, b, c):
    if a < b and b < c:
        return a, b, c
    elif a < c and c < b:
        return a, c, b
    elif b < a and a < c:
        return b, a, c
    elif b < c and c < a:
        return b, c, a
    elif c < a and a < b:
        return c, a, b
    else:
        return c, b, a
