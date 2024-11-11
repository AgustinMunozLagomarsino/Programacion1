from collections import Counter
import re

def contar_palabras_comunes(archivo="libros.txt"):
    try:
        with open(archivo, "r") as f:
            texto = f.read().lower()  # Leer todo el texto y convertirlo a minúsculas

        # Utilizamos una expresión regular para extraer solo palabras
        palabras = re.findall(r'\b\w+\b', texto)

        # Contamos las palabras usando Counter
        contador_palabras = Counter(palabras)

        # Encontramos las 5 palabras más comunes
        palabras_comunes = contador_palabras.most_common(5)

        # Mostramos las 5 palabras más comunes y sus ocurrencias
        print("Las 5 palabras más comunes y sus frecuencias:")
        for palabra, frecuencia in palabras_comunes:
            print(f"{palabra}: {frecuencia}")

    except FileNotFoundError:
        print(f"El archivo '{archivo}' no fue encontrado.")

# Ejemplo de uso
contar_palabras_comunes()
